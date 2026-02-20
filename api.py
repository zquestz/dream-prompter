#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
API integration for Dream Prompter plugin.

This module provides API classes for communicating with different AI platforms
(Replicate, Google Cloud) to perform image generation and editing operations.
"""

import io
import mimetypes
import os
import urllib.request
from abc import ABC, abstractmethod
from contextlib import contextmanager
from enum import Enum
from typing import Callable, List, Optional, Tuple, Union
from concurrent.futures import ThreadPoolExecutor, as_completed

from gi.repository import GdkPixbuf, Gimp

import integrator
from i18n import _
from models.factory import get_default_model, get_model_by_name
from settings import get_model_settings


class APIProvider(Enum):
    """Supported API providers"""
    REPLICATE = "replicate"
    GOOGLE_CLOUD = "google_cloud"

PROGRESS_COMPLETE = 1.0
PROGRESS_DOWNLOAD = 0.9
PROGRESS_PREPARE = 0.1
PROGRESS_PROCESS = 0.7
PROGRESS_UPLOAD = 0.5

try:
    from replicate.client import Client
    from replicate.exceptions import ModelError, ReplicateError

    REPLICATE_AVAILABLE = True
except ImportError:
    REPLICATE_AVAILABLE = False
    print(
        "Warning: replicate package not installed. Run: pip install replicate"
    )

try:
    from google import genai
    from google.genai import types as genai_types
    
    GOOGLE_CLOUD_AVAILABLE = True
except ImportError:
    GOOGLE_CLOUD_AVAILABLE = False
    print(
        "Warning: Google Cloud packages not installed. "
        "Run: pip install google-genai"
    )


class BaseAPI(ABC):
    """Abstract base class for all API providers"""

    def __init__(self, api_key: str, model_name: Optional[str] = None) -> None:
        """
        Initialize the API client.

        Args:
            api_key: API key from user settings
            model_name: Model to use (defaults to default model)

        Raises:
            ValueError: If API key is invalid or model not found
        """
        if not api_key or not api_key.strip():
            raise ValueError(_("API key is required"))

        self.api_key = api_key.strip()

        if model_name:
            model = get_model_by_name(model_name)
            if not model:
                raise ValueError(f"Model '{model_name}' not found")
            self.model = model
        else:
            self.model = get_default_model()

    @abstractmethod
    def edit_image(
        self,
        image: Gimp.Image,
        prompt: str,
        reference_images: Optional[List[str]] = None,
        progress_callback: Optional[
            Callable[[str, Optional[float]], bool]
        ] = None,
    ) -> Tuple[Optional[List[GdkPixbuf.Pixbuf]], Optional[str]]:
        """Edit an image using AI model based on text prompt."""
        pass

    @abstractmethod
    def generate_image(
        self,
        prompt: str,
        reference_images: Optional[List[str]] = None,
        progress_callback: Optional[
            Callable[[str, Optional[float]], bool]
        ] = None,
    ) -> Tuple[Optional[List[GdkPixbuf.Pixbuf]], Optional[str]]:
        """Generate a new image using AI model based on text prompt."""
        pass

    def _bytes_to_pixbuf(
        self, image_bytes: bytes
    ) -> Optional[GdkPixbuf.Pixbuf]:
        """
        Convert image bytes to GdkPixbuf.

        Args:
            image_bytes: Image data as bytes

        Returns:
            GdkPixbuf.Pixbuf object, or None if conversion failed
        """
        try:
            loader = GdkPixbuf.PixbufLoader()
            loader.write(image_bytes)
            loader.close()
            return loader.get_pixbuf()

        except Exception as e:
            print(f"Error converting bytes to pixbuf: {e}")
            return None

    def _download_from_url(self, url: str) -> Optional[bytes]:
        """
        Download image data from URL.

        Args:
            url: Image URL to download

        Returns:
            Image data as bytes, or None if download failed
        """
        try:
            with urllib.request.urlopen(url) as url_response:
                return url_response.read()
        except Exception as e:
            print(f"Error downloading from URL {url}: {e}")
            return None

    def _validate_reference_image(self, img_path: str) -> bool:
        """
        Validate a reference image file.

        Args:
            img_path: Path to the image file

        Returns:
            True if valid, False otherwise
        """
        try:
            if not os.path.exists(img_path):
                print(
                    f"Warning: Image file {img_path} does not exist. Skipping."
                )
                return False

            file_size = os.path.getsize(img_path)
            if not self.model.validate_file_size(file_size):
                file_size_mb = file_size / (1024 * 1024)
                max_size_mb = self.model.max_file_size_mb
                print(
                    f"Warning: Image {img_path} is {file_size_mb:.1f} MB, "
                    f"exceeds {max_size_mb} MB limit. Skipping."
                )
                return False

            mime_type, encoding = mimetypes.guess_type(img_path)
            if not mime_type:
                print(
                    f"Warning: Could not determine MIME type for "
                    f"{img_path}. Skipping."
                )
                return False

            if not self.model.validate_mime_type(mime_type):
                print(
                    f"Warning: Image {img_path} has unsupported MIME type "
                    f"{mime_type}. Skipping."
                )
                return False

            return True

        except Exception as e:
            print(
                f"Warning: Could not validate reference image {img_path}: {e}"
            )
            return False


class ReplicateAPI(BaseAPI):
    """Handles Replicate API communication for image generation and editing."""

    def __init__(self, api_key: str, model_name: Optional[str] = None) -> None:
        """
        Initialize the Replicate API client.

        Args:
            api_key: Replicate API key from user settings
            model_name: Model to use (defaults to default model)

        Raises:
            ImportError: If Replicate API is not available
            ValueError: If API key is invalid or model not found
        """
        if not REPLICATE_AVAILABLE:
            raise ImportError(
                _("Replicate API not available. Please install replicate")
            )

        super().__init__(api_key, model_name)
        self.client = Client(api_token=self.api_key)

    def edit_image(
        self,
        image: Gimp.Image,
        prompt: str,
        reference_images: Optional[List[str]] = None,
        progress_callback: Optional[
            Callable[[str, Optional[float]], bool]
        ] = None,
    ) -> Tuple[Optional[List[GdkPixbuf.Pixbuf]], Optional[str]]:
        """
        Edit an image using AI model based on text prompt.

        Args:
            image: GIMP image to edit
            prompt: Text description of the edits to make
            reference_images: List of image file paths for reference
            progress_callback: Progress callback function that receives
                (message: str, percentage: float | None) and returns
                True to continue, False to cancel

        Returns:
            Tuple of (pixbufs, error_message):
            - If successful: (List[GdkPixbuf.Pixbuf], None)
            - If failed: (None, error_message)
            - If cancelled: (None, "Operation cancelled")
        """
        if not self.client:
            return None, _(
                "Replicate API not available. Please install replicate"
            )

        if not image:
            return None, _("No GIMP image provided for editing")

        try:
            if progress_callback and not progress_callback(
                _("Preparing current image for Replicate..."), PROGRESS_PREPARE
            ):
                return None, _("Operation cancelled")

            current_image_data = integrator.export_current_region_to_bytes(
                image
            )
            if not current_image_data:
                return None, _("Failed to export current image")

            with self._prepare_reference_images(
                reference_images, self.model.max_reference_images_edit
            ) as ref_files:
                if progress_callback and not progress_callback(
                    _("Building Replicate edit request..."), PROGRESS_UPLOAD
                ):
                    return None, _("Operation cancelled")

                user_settings = get_model_settings(self.model.name)
                model_input = self.model.build_edit_input(
                    prompt=prompt,
                    main_image=io.BytesIO(current_image_data),
                    reference_images=ref_files if ref_files else None,
                    user_settings=user_settings,
                )

                if progress_callback and not progress_callback(
                    _("Sending edit request to Replicate..."), PROGRESS_PROCESS
                ):
                    return None, _("Operation cancelled")

                output = self._execute_api_call(model_input)
                if isinstance(output, str):
                    return None, output

            return self._process_response(output, progress_callback)

        except Exception as e:
            return None, _("Unexpected error: {error}").format(error=str(e))

    def generate_image(
        self,
        prompt: str,
        reference_images: Optional[List[str]] = None,
        progress_callback: Optional[
            Callable[[str, Optional[float]], bool]
        ] = None,
    ) -> Tuple[Optional[List[GdkPixbuf.Pixbuf]], Optional[str]]:
        """
        Generate a new image using AI model based on text prompt.

        Args:
            prompt: Text description of the image to generate
            reference_images: List of image file paths for reference
            progress_callback: Progress callback function that receives
                (message: str, percentage: float | None) and returns
                True to continue, False to cancel

        Returns:
            Tuple of (pixbufs, error_message):
            - If successful: (List[GdkPixbuf.Pixbuf], None)
            - If failed: (None, error_message)
            - If cancelled: (None, "Operation cancelled")
        """
        if not self.client:
            return None, _(
                "Replicate API not available. Please install replicate"
            )

        try:
            with self._prepare_reference_images(
                reference_images, self.model.max_reference_images
            ) as ref_files:
                if progress_callback and not progress_callback(
                    _("Generating image with Replicate..."), PROGRESS_PREPARE
                ):
                    return None, _("Operation cancelled")

                user_settings = get_model_settings(self.model.name)
                model_input = self.model.build_generation_input(
                    prompt=prompt,
                    reference_images=ref_files if reference_images else None,
                    user_settings=user_settings,
                )

                if progress_callback and not progress_callback(
                    _("Sending request to Replicate..."), PROGRESS_PROCESS
                ):
                    return None, _("Operation cancelled")

                output = self._execute_api_call(model_input)
                if isinstance(output, str):
                    return None, output

            return self._process_response(output, progress_callback)

        except Exception as e:
            return None, _("Unexpected error: {error}").format(error=str(e))

    def _execute_api_call(self, model_input: dict) -> Union[object, str]:
        """
        Execute API call with proper error handling.

        Args:
            model_input: Input parameters for the model

        Returns:
            API response object or error message string
        """
        try:
            return self.client.run(self.model.name, input=model_input)

        except ModelError as e:
            error_msg = _("Model error: {error}").format(error=str(e))
            if hasattr(e, "prediction") and e.prediction:
                if hasattr(e.prediction, "logs") and e.prediction.logs:
                    error_msg += f"\n{_('Logs')}: {e.prediction.logs}"
            return error_msg

        except ReplicateError as e:
            return _("Replicate API error: {error}").format(error=str(e))

    @contextmanager
    def _prepare_reference_images(
        self, reference_images: Optional[List[str]], max_count: int
    ):
        """
        Context manager for preparing reference images.

        Args:
            reference_images: List of image file paths
            max_count: Maximum number of images to process

        Yields:
            List of file objects for Replicate API
        """
        if not reference_images:
            yield []
            return

        file_handles = []
        try:
            for img_path in reference_images[:max_count]:
                if self._validate_reference_image(img_path):
                    try:
                        file_handle = open(img_path, "rb")
                        file_handles.append(file_handle)
                    except (OSError, IOError) as e:
                        print(
                            f"Warning: Could not open reference image "
                            f"{img_path}: {e}"
                        )

            yield file_handles

        finally:
            for file_handle in file_handles:
                try:
                    file_handle.close()
                except Exception as e:
                    print(f"Error closing file handle: {e}")

    def _process_api_response(self, output) -> List[bytes]:
        """
        Process API response and extract image bytes.

        Args:
            output: API response object

        Returns:
            List of image data as bytes
        """
        image_bytes_list = []

        if isinstance(output, str):
            image_bytes_list.append(self._download_from_url(output))
        elif isinstance(output, bytes):
            image_bytes_list.append(output)
        elif isinstance(output, (list, tuple)):
            for item in output:
                if isinstance(item, str):
                    downloaded_bytes = self._download_from_url(item)
                    if downloaded_bytes:
                        image_bytes_list.append(downloaded_bytes)
                elif isinstance(item, bytes):
                    image_bytes_list.append(item)
                elif hasattr(item, "read"):
                    try:
                        image_bytes_list.append(item.read())
                    except Exception as e:
                        print(f"Error reading from file-like object: {e}")
        elif hasattr(output, "__iter__"):
            try:
                chunk_bytes = b"".join(chunk for chunk in output)
                if chunk_bytes:
                    image_bytes_list.append(chunk_bytes)
            except (TypeError, ValueError) as e:
                print(f"Error processing iterable output: {e}")

        return [img_bytes for img_bytes in image_bytes_list if img_bytes]

    def _process_response(
        self,
        output,
        progress_callback: Optional[
            Callable[[str, Optional[float]], bool]
        ] = None,
    ) -> Tuple[Optional[List[GdkPixbuf.Pixbuf]], Optional[str]]:
        """
        Process API response and convert to pixbufs.

        Args:
            output: API response object
            progress_callback: Progress callback function

        Returns:
            Tuple of (pixbufs, error_message)
        """
        if progress_callback and not progress_callback(
            _("Processing Replicate response..."), PROGRESS_DOWNLOAD
        ):
            return None, _("Operation cancelled")

        if not output:
            return None, _("No output received from API")

        if progress_callback and not progress_callback(
            _("Downloading result..."), PROGRESS_DOWNLOAD
        ):
            return None, _("Operation cancelled")

        image_bytes_list = self._process_api_response(output)
        if not image_bytes_list:
            return None, _("No valid image data in API response")

        pixbufs = []
        for image_bytes in image_bytes_list:
            if image_bytes and isinstance(image_bytes, bytes):
                pixbuf = self._bytes_to_pixbuf(image_bytes)
                if pixbuf:
                    pixbufs.append(pixbuf)

        if not pixbufs:
            return None, _("Failed to convert any images from API response")

        if progress_callback:
            operation_complete_msg = (
                _("Image editing complete!")
                if hasattr(self, "_is_edit_operation")
                else _("Image generation complete!")
            )
            progress_callback(operation_complete_msg, PROGRESS_COMPLETE)

        return pixbufs, None


class GoogleCloudAPI(BaseAPI):
    """Handles Google Cloud API communication for image generation and editing."""

    def __init__(self, api_key: str, model_name: Optional[str] = None) -> None:
        """
        Initialize the Google Cloud API client.

        Args:
            api_key: Google API key from user settings
            model_name: Model to use (defaults to default model)

        Raises:
            ImportError: If Google Cloud API is not available
            ValueError: If API key is invalid or model not found
        """
        if not GOOGLE_CLOUD_AVAILABLE:
            raise ImportError(
                _("Google Cloud API not available. Please install "
                  "google-cloud-aiplatform and google-generativeai")
            )

        super().__init__(api_key, model_name)
        
        # Create the genai client with API key
        self.client = genai.Client(api_key=self.api_key)
        
        # Map our model names to Google's actual model names
        self.gemini_model_name = self._get_gemini_model_name()
    
    def _get_gemini_model_name(self) -> str:
        """Get the correct Gemini model name based on the selected model"""
        if self.model.name == "google/nano-banana-pro":
            return "gemini-3-pro-image-preview"
        elif self.model.name == "google/nano-banana":
            return "gemini-2.5-flash-image"
        else:
            # Default fallback
            return "gemini-2.5-flash-image"

    def edit_image(
        self,
        image: Gimp.Image,
        prompt: str,
        reference_images: Optional[List[str]] = None,
        progress_callback: Optional[
            Callable[[str, Optional[float]], bool]
        ] = None,
        num_images: int = 3,
    ) -> Tuple[Optional[List[GdkPixbuf.Pixbuf]], Optional[str]]:
        """
        Edit an image using Google's AI model based on text prompt.

        Args:
            image: GIMP image to edit
            prompt: Text description of the edits to make
            reference_images: List of image file paths for reference
            progress_callback: Progress callback function
            num_images: Number of images to generate in parallel

        Returns:
            Tuple of (pixbufs, error_message)
        """
        if not image:
            return None, _("No GIMP image provided for editing")

        try:
            print(f"[DEBUG] Starting Google Cloud image editing")
            print(f"[DEBUG] Model name: {self.gemini_model_name}")
            
            if progress_callback and not progress_callback(
                _("Preparing current image for Google Cloud..."), PROGRESS_PREPARE
            ):
                return None, _("Operation cancelled")

            current_image_data = integrator.export_current_region_to_bytes(
                image
            )
            if not current_image_data:
                return None, _("Failed to export current image")

            if progress_callback and not progress_callback(
                _("Sending edit request to Google Cloud..."), PROGRESS_PROCESS
            ):
                return None, _("Operation cancelled")

            # Use Gemini for image editing
            print(f"[DEBUG] Using model: {self.gemini_model_name}")
            
            # Upload the main image using PIL
            print(f"[DEBUG] Loading image with PIL")
            import PIL.Image
            try:
                image_pil = PIL.Image.open(io.BytesIO(current_image_data))
                print(f"[DEBUG] Image loaded: {image_pil.size}, {image_pil.mode}")
            except Exception as pil_error:
                print(f"[ERROR] PIL error: {pil_error}")
                import traceback
                traceback.print_exc()
                return None, f"Failed to load image with PIL: {str(pil_error)}"
            
            # Build content list with prompt and images
            # Store images as bytes to avoid thread-safety issues
            content_parts_data = [prompt]  # Start with prompt
            
            # Convert main image to bytes for thread-safe sharing
            image_bytes = io.BytesIO()
            image_pil.save(image_bytes, format='PNG')
            image_bytes.seek(0)
            content_parts_data.append(('main_image', image_bytes.getvalue()))
            print(f"[DEBUG] Main image saved as bytes")
            
            # Add reference images as bytes if provided
            if reference_images:
                max_refs = self.model.max_reference_images_edit
                for ref_path in reference_images[:max_refs]:
                    if self._validate_reference_image(ref_path):
                        try:
                            ref_image = PIL.Image.open(ref_path)
                            ref_bytes = io.BytesIO()
                            ref_image.save(ref_bytes, format='PNG')
                            ref_bytes.seek(0)
                            content_parts_data.append(('ref_image', ref_bytes.getvalue()))
                            print(f"[DEBUG] Added reference image: {ref_path}")
                        except Exception as e:
                            print(f"[WARNING] Could not load reference image {ref_path}: {e}")
            
            # Get user settings for resolution and aspect ratio
            user_settings = get_model_settings(self.model.name)
            resolution = user_settings.get("resolution", "2K")
            # For edit mode, if aspect ratio is "original", omit it to keep original dimensions
            aspect_ratio = user_settings.get("aspect_ratio", "original")
            
            # Build generation config using proper types
            # If aspect_ratio is "original", don't pass it (keeps original image dimensions)
            if aspect_ratio == "original":
                generation_config = genai_types.GenerateContentConfig(
                    image_config=genai_types.ImageConfig(
                        image_size=resolution,
                    )
                )
                print(f"[DEBUG] Resolution: {resolution}, Aspect Ratio: Original (Auto)")
            else:
                generation_config = genai_types.GenerateContentConfig(
                    image_config=genai_types.ImageConfig(
                        aspect_ratio=aspect_ratio,
                        image_size=resolution,
                    )
                )
                print(f"[DEBUG] Resolution: {resolution}, Aspect Ratio: {aspect_ratio}")
            
            # Make parallel API calls
            num_images = num_images if num_images else 3
            print(f"[DEBUG] Starting {num_images} parallel API calls")
            
            def make_single_call(call_number):
                """Make a single API call with independent image copies"""
                print(f"[DEBUG] API call {call_number}/{num_images} starting")
                try:
                    # Recreate content_parts from bytes for thread safety
                    import PIL.Image
                    content_parts = [content_parts_data[0]]  # Add prompt
                    
                    # Recreate PIL images from bytes for this thread
                    for img_type, img_bytes in content_parts_data[1:]:
                        pil_img = PIL.Image.open(io.BytesIO(img_bytes))
                        content_parts.append(pil_img)
                    
                    print(f"[DEBUG] Call {call_number}: Created {len(content_parts)} content parts")
                    
                    response = self.client.models.generate_content(
                        model=self.gemini_model_name,
                        contents=content_parts,
                        config=generation_config
                    )
                    print(f"[DEBUG] API call {call_number}/{num_images} completed")
                    return (call_number, response, None)
                except Exception as e:
                    print(f"[ERROR] API call {call_number}/{num_images} failed: {e}")
                    import traceback
                    traceback.print_exc()
                    return (call_number, None, str(e))
            
            # Execute calls in parallel using thread pool
            all_responses = []
            with ThreadPoolExecutor(max_workers=num_images) as executor:
                futures = {executor.submit(make_single_call, i+1): i+1 
                          for i in range(num_images)}
                
                for future in as_completed(futures):
                    call_num, response, error = future.result()
                    
                    if progress_callback:
                        completed = len(all_responses) + 1
                        progress = 0.5 + (0.3 * completed / num_images)  # 50% to 80%
                        msg = _("Completed API call {num} of {total}...").format(
                            num=completed, total=num_images
                        )
                        if not progress_callback(msg, progress):
                            return None, _("Operation cancelled")
                    
                    all_responses.append((call_num, response, error))
            
            # Sort by call number to maintain order
            all_responses.sort(key=lambda x: x[0])
            print(f"[DEBUG] All {num_images} API calls completed")
            
            # Sort by call number to maintain order
            all_responses.sort(key=lambda x: x[0])
            print(f"[DEBUG] All {num_images} API calls completed")
            
            if progress_callback and not progress_callback(
                _("Processing {num} responses...").format(num=num_images), 0.8
            ):
                return None, _("Operation cancelled")

            # Process all responses and extract images
            all_pixbufs = []
            errors = []
            
            for call_num, response, error in all_responses:
                if error:
                    errors.append(f"Call {call_num}: {error}")
                    continue
                
                if not response:
                    errors.append(f"Call {call_num}: No response")
                    continue
                
                print(f"[DEBUG] Processing response {call_num}")
                print(f"[DEBUG] Response type: {type(response)}")
                print(f"[DEBUG] Response.parts: {response.parts}")
                
                # Print full response details for debugging
                print(f"[DEBUG] Response attributes: {dir(response)}")
                if hasattr(response, 'text'):
                    print(f"[DEBUG] Response.text: {response.text}")
                if hasattr(response, 'candidates'):
                    print(f"[DEBUG] Response.candidates: {response.candidates}")
                    if response.candidates:
                        for idx, candidate in enumerate(response.candidates):
                            print(f"[DEBUG] Candidate {idx}: {candidate}")
                            if hasattr(candidate, 'finish_reason'):
                                print(f"[DEBUG] Candidate {idx} finish_reason: {candidate.finish_reason}")
                            if hasattr(candidate, 'safety_ratings'):
                                print(f"[DEBUG] Candidate {idx} safety_ratings: {candidate.safety_ratings}")
                
                # Check if parts exist
                if not response.parts:
                    print(f"[ERROR] Response {call_num} has no parts")
                    # Try to get more info about why
                    if hasattr(response, 'prompt_feedback'):
                        print(f"[DEBUG] Prompt feedback: {response.prompt_feedback}")
                    errors.append(f"Call {call_num}: No parts in response - possibly blocked by safety filters")
                    continue
                
                # Extract images from this response
                print(f"[DEBUG] Response {call_num} has {len(response.parts)} parts")
                
                for i, part in enumerate(response.parts):
                    if part.text is not None:
                        print(f"[DEBUG] Call {call_num}, Part {i} has text: {part.text[:100]}")
                        
                    if part.inline_data is not None:
                        print(f"[DEBUG] Call {call_num}, Part {i} has inline_data, converting")
                        try:
                            # Use the new API's as_image() method
                            genai_image = part.as_image()
                            print(f"[DEBUG] Got genai Image object: {type(genai_image)}")
                            
                            # Convert to PIL Image
                            import PIL.Image
                            if hasattr(genai_image, '_pil_image'):
                                pil_image = genai_image._pil_image
                                print(f"[DEBUG] Got PIL image: {pil_image.size}, {pil_image.mode}")
                            else:
                                # Save to BytesIO and reload
                                print(f"[DEBUG] Saving genai image to BytesIO")
                                img_byte_arr = io.BytesIO()
                                genai_image.save(img_byte_arr)
                                img_byte_arr.seek(0)
                                pil_image = PIL.Image.open(img_byte_arr)
                                print(f"[DEBUG] Loaded PIL image: {pil_image.size}, {pil_image.mode}")
                            
                            # Convert PIL image to PNG bytes
                            img_byte_arr = io.BytesIO()
                            pil_image.save(img_byte_arr, format='PNG')
                            image_bytes = img_byte_arr.getvalue()
                            print(f"[DEBUG] Converted to {len(image_bytes)} bytes")
                            
                            # Convert to pixbuf
                            pixbuf = self._bytes_to_pixbuf(image_bytes)
                            if pixbuf:
                                print(f"[DEBUG] Successfully converted call {call_num} to pixbuf")
                                all_pixbufs.append(pixbuf)
                        except Exception as img_error:
                            print(f"[ERROR] Failed to process image from call {call_num}, part {i}: {img_error}")
                            import traceback
                            traceback.print_exc()
                            errors.append(f"Call {call_num}, Part {i}: {str(img_error)}")

            if not all_pixbufs:
                error_summary = "\n".join(errors) if errors else "No images generated"
                return None, _("No images generated. Errors:\n{errors}").format(errors=error_summary)

            print(f"[DEBUG] Successfully generated {len(all_pixbufs)} images from {num_images} calls")
            
            if progress_callback:
                msg = _("Generated {count} images!").format(count=len(all_pixbufs))
                progress_callback(msg, PROGRESS_COMPLETE)

            return all_pixbufs, None

        except Exception as e:
            print(f"[ERROR] Exception in edit_image: {e}")
            import traceback
            traceback.print_exc()
            return None, _("Google Cloud API error: {error}").format(error=str(e))

    def generate_image(
        self,
        prompt: str,
        reference_images: Optional[List[str]] = None,
        progress_callback: Optional[
            Callable[[str, Optional[float]], bool]
        ] = None,
        num_images: int = 3,
    ) -> Tuple[Optional[List[GdkPixbuf.Pixbuf]], Optional[str]]:
        """
        Generate a new image using Google's AI model based on text prompt.

        Args:
            prompt: Text description of the image to generate
            reference_images: List of image file paths for reference
            progress_callback: Progress callback function
            num_images: Number of images to generate in parallel

        Returns:
            Tuple of (pixbufs, error_message)
        """
        try:
            print(f"[DEBUG] Starting Google Cloud image generation")
            print(f"[DEBUG] Model name: {self.gemini_model_name}")
            
            if progress_callback and not progress_callback(
                _("Generating image with Google Cloud..."), PROGRESS_PREPARE
            ):
                return None, _("Operation cancelled")

            if progress_callback and not progress_callback(
                _("Sending request to Google Cloud..."), PROGRESS_PROCESS
            ):
                return None, _("Operation cancelled")

            # Use Gemini for image generation
            print(f"[DEBUG] Using model: {self.gemini_model_name}")
            
            user_settings = get_model_settings(self.model.name)
            resolution = user_settings.get("resolution", "2K")
            # For generation mode, if aspect ratio is "original", default to 1:1
            aspect_ratio = user_settings.get("aspect_ratio", "1:1")
            if aspect_ratio == "original":
                aspect_ratio = "1:1"  # Default to 1:1 for generation
            
            # Build generation config using proper types
            generation_config = genai_types.GenerateContentConfig(
                image_config=genai_types.ImageConfig(
                    aspect_ratio=aspect_ratio,
                    image_size=resolution,
                )
            )
            print(f"[DEBUG] Resolution: {resolution}, Aspect Ratio: {aspect_ratio}")
            
            # Build content list with prompt and reference images
            # Store images as bytes to avoid thread-safety issues
            import PIL.Image
            content_parts_data = [prompt]  # Start with prompt
            print(f"[DEBUG] Starting with prompt: {prompt[:100]}")
            
            # Add reference images as bytes if provided
            if reference_images:
                max_refs = self.model.max_reference_images
                print(f"[DEBUG] Processing {len(reference_images)} reference images (max: {max_refs})")
                for ref_path in reference_images[:max_refs]:
                    if self._validate_reference_image(ref_path):
                        try:
                            ref_image = PIL.Image.open(ref_path)
                            ref_bytes = io.BytesIO()
                            ref_image.save(ref_bytes, format='PNG')
                            ref_bytes.seek(0)
                            content_parts_data.append(('ref_image', ref_bytes.getvalue()))
                            print(f"[DEBUG] Added reference image: {ref_path}")
                        except Exception as e:
                            print(f"[WARNING] Could not load reference image {ref_path}: {e}")
            
            # Make parallel API calls
            num_images = num_images if num_images else 3
            print(f"[DEBUG] Starting {num_images} parallel API calls")
            
            def make_single_call(call_number):
                """Make a single API call with independent image copies"""
                print(f"[DEBUG] API call {call_number}/{num_images} starting")
                try:
                    # Recreate content_parts from bytes for thread safety
                    import PIL.Image
                    content_parts = [content_parts_data[0]]  # Add prompt
                    
                    # Recreate PIL images from bytes for this thread
                    for img_type, img_bytes in content_parts_data[1:]:
                        pil_img = PIL.Image.open(io.BytesIO(img_bytes))
                        content_parts.append(pil_img)
                    
                    print(f"[DEBUG] Call {call_number}: Created {len(content_parts)} content parts")
                    
                    response = self.client.models.generate_content(
                        model=self.gemini_model_name,
                        contents=content_parts,
                        config=generation_config
                    )
                    print(f"[DEBUG] API call {call_number}/{num_images} completed")
                    return (call_number, response, None)
                except Exception as e:
                    print(f"[ERROR] API call {call_number}/{num_images} failed: {e}")
                    import traceback
                    traceback.print_exc()
                    return (call_number, None, str(e))
            
            # Execute calls in parallel using thread pool
            all_responses = []
            with ThreadPoolExecutor(max_workers=num_images) as executor:
                futures = {executor.submit(make_single_call, i+1): i+1 
                          for i in range(num_images)}
                
                for future in as_completed(futures):
                    call_num, response, error = future.result()
                    
                    if progress_callback:
                        completed = len(all_responses) + 1
                        progress = 0.5 + (0.3 * completed / num_images)  # 50% to 80%
                        msg = _("Completed API call {num} of {total}...").format(
                            num=completed, total=num_images
                        )
                        if not progress_callback(msg, progress):
                            return None, _("Operation cancelled")
                    
                    all_responses.append((call_num, response, error))
            
            # Sort by call number to maintain order
            all_responses.sort(key=lambda x: x[0])
            print(f"[DEBUG] All {num_images} API calls completed")

            if progress_callback and not progress_callback(
                _("Processing {num} responses...").format(num=num_images), 0.8
            ):
                return None, _("Operation cancelled")

            # Process all responses and extract images
            all_pixbufs = []
            errors = []
            
            for call_num, response, error in all_responses:
                if error:
                    errors.append(f"Call {call_num}: {error}")
                    continue
                
                if not response:
                    errors.append(f"Call {call_num}: No response")
                    continue
                
                print(f"[DEBUG] Processing response {call_num}")
                print(f"[DEBUG] Response type: {type(response)}")
                print(f"[DEBUG] Response.parts: {response.parts}")
                
                # Print full response details for debugging
                print(f"[DEBUG] Response attributes: {dir(response)}")
                if hasattr(response, 'text'):
                    print(f"[DEBUG] Response.text: {response.text}")
                if hasattr(response, 'candidates'):
                    print(f"[DEBUG] Response.candidates: {response.candidates}")
                    if response.candidates:
                        for idx, candidate in enumerate(response.candidates):
                            print(f"[DEBUG] Candidate {idx}: {candidate}")
                            if hasattr(candidate, 'finish_reason'):
                                print(f"[DEBUG] Candidate {idx} finish_reason: {candidate.finish_reason}")
                            if hasattr(candidate, 'safety_ratings'):
                                print(f"[DEBUG] Candidate {idx} safety_ratings: {candidate.safety_ratings}")
                
                # Check if parts exist
                if not response.parts:
                    print(f"[ERROR] Response {call_num} has no parts")
                    # Try to get more info about why
                    if hasattr(response, 'prompt_feedback'):
                        print(f"[DEBUG] Prompt feedback: {response.prompt_feedback}")
                    errors.append(f"Call {call_num}: No parts in response - possibly blocked by safety filters")
                    continue
                
                # Extract images from this response
                print(f"[DEBUG] Response {call_num} has {len(response.parts)} parts")
                
                for i, part in enumerate(response.parts):
                    if part.text is not None:
                        print(f"[DEBUG] Call {call_num}, Part {i} has text: {part.text[:100]}")
                        
                    if part.inline_data is not None:
                        print(f"[DEBUG] Call {call_num}, Part {i} has inline_data, converting")
                        try:
                            # Use the new API's as_image() method
                            genai_image = part.as_image()
                            print(f"[DEBUG] Got genai Image object: {type(genai_image)}")
                            
                            # Convert to PIL Image
                            import PIL.Image
                            if hasattr(genai_image, '_pil_image'):
                                pil_image = genai_image._pil_image
                                print(f"[DEBUG] Got PIL image: {pil_image.size}, {pil_image.mode}")
                            else:
                                # Save to BytesIO and reload
                                print(f"[DEBUG] Saving genai image to BytesIO")
                                img_byte_arr = io.BytesIO()
                                genai_image.save(img_byte_arr)
                                img_byte_arr.seek(0)
                                pil_image = PIL.Image.open(img_byte_arr)
                                print(f"[DEBUG] Loaded PIL image: {pil_image.size}, {pil_image.mode}")
                            
                            # Convert PIL image to PNG bytes
                            img_byte_arr = io.BytesIO()
                            pil_image.save(img_byte_arr, format='PNG')
                            image_bytes = img_byte_arr.getvalue()
                            print(f"[DEBUG] Converted to {len(image_bytes)} bytes")
                            
                            # Convert to pixbuf
                            pixbuf = self._bytes_to_pixbuf(image_bytes)
                            if pixbuf:
                                print(f"[DEBUG] Successfully converted call {call_num} to pixbuf")
                                all_pixbufs.append(pixbuf)
                        except Exception as img_error:
                            print(f"[ERROR] Failed to process image from call {call_num}, part {i}: {img_error}")
                            import traceback
                            traceback.print_exc()
                            errors.append(f"Call {call_num}, Part {i}: {str(img_error)}")

            if not all_pixbufs:
                error_summary = "\n".join(errors) if errors else "No images generated"
                return None, _("No images generated. Errors:\n{errors}").format(errors=error_summary)

            print(f"[DEBUG] Successfully generated {len(all_pixbufs)} images from {num_images} calls")
            
            if progress_callback:
                msg = _("Generated {count} images!").format(count=len(all_pixbufs))
                progress_callback(msg, PROGRESS_COMPLETE)

            return all_pixbufs, None

        except Exception as e:
            print(f"[ERROR] Exception in generate_image: {e}")
            import traceback
            traceback.print_exc()
            return None, _("Google Cloud API error: {error}").format(error=str(e))


def create_api_client(
    provider: APIProvider,
    api_key: str,
    model_name: Optional[str] = None
) -> BaseAPI:
    """
    Factory function to create the appropriate API client.

    Args:
        provider: The API provider to use
        api_key: API key for the provider
        model_name: Optional model name

    Returns:
        Instance of the appropriate API class

    Raises:
        ValueError: If the provider is not supported
    """
    if provider == APIProvider.REPLICATE:
        return ReplicateAPI(api_key, model_name)
    elif provider == APIProvider.GOOGLE_CLOUD:
        return GoogleCloudAPI(api_key, model_name)
    else:
        raise ValueError(f"Unsupported API provider: {provider}")
