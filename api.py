"""
Replicate API integration for Dream Prompter plugin.

This module provides the ReplicateAPI class for communicating with Replicate's
API to perform image generation and editing operations using various AI models.
"""

import io
import time
import urllib.request
from collections.abc import Callable
from contextlib import ExitStack, contextmanager

from gi.repository import GdkPixbuf, Gimp

import integrator
from i18n import _
from image_validation import (
    InputValidationError,
    prepare_reference_image,
    validate_image,
    validate_request,
)
from models.factory import get_default_model, get_model_by_name
from settings import get_model_settings

DOWNLOAD_TIMEOUT_SECONDS = 60
PROGRESS_COMPLETE = 1.0
PROGRESS_DOWNLOAD = 0.9
PROGRESS_PREPARE = 0.1
PROGRESS_PROCESS = 0.7
PROGRESS_UPLOAD = 0.5

try:
    import httpx
    from replicate.client import Client
    from replicate.exceptions import ModelError, ReplicateError

    REPLICATE_AVAILABLE = True
except ImportError:
    REPLICATE_AVAILABLE = False
    print(
        "Warning: replicate package not installed. Run: pip install replicate"
    )


class ReplicateAPI:
    """Handles Replicate API communication for image generation and editing."""

    def __init__(self, api_key: str, model_name: str | None = None) -> None:
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

        if not api_key or not api_key.strip():
            raise ValueError(_("API key is required"))

        self.api_key = api_key.strip()
        self.client = Client(api_token=self.api_key)

        if model_name:
            model = get_model_by_name(model_name)
            if not model:
                raise ValueError(f"Model '{model_name}' not found")
            self.model = model
        else:
            self.model = get_default_model()

    def edit_image(
        self,
        image: Gimp.Image,
        prompt: str,
        reference_images: list[str] | None = None,
        progress_callback: Callable[[str, float | None], bool] | None = None,
    ) -> tuple[list[GdkPixbuf.Pixbuf] | None, str | None]:
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
            - If successful: (list[GdkPixbuf.Pixbuf], None)
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
            # Validate and prepare the same snapshot of the request.
            reference_images = list(reference_images or [])
            validate_request(self.model, "edit", len(reference_images))
            if progress_callback and not progress_callback(
                _("Preparing current image for Replicate..."), PROGRESS_PREPARE
            ):
                return None, _("Operation cancelled")

            current_image_data = integrator.export_current_region_to_bytes(
                image
            )
            if not current_image_data:
                return None, _("Failed to export current image")

            validate_image(
                self.model,
                current_image_data,
                _("Current image or selection"),
            )

            with (
                self._prepare_reference_images(reference_images) as ref_files,
                io.BytesIO(current_image_data) as main_image,
            ):
                if progress_callback and not progress_callback(
                    _("Building Replicate edit request..."), PROGRESS_UPLOAD
                ):
                    return None, _("Operation cancelled")

                user_settings = get_model_settings(self.model.name)
                # Uploads inherit this name; some model runners (Grok)
                # validate the file extension and reject unnamed buffers
                main_image.name = "image.png"
                model_input = self.model.build_edit_input(
                    prompt=prompt,
                    main_image=main_image,
                    reference_images=ref_files if ref_files else None,
                    user_settings=user_settings,
                )

                if progress_callback and not progress_callback(
                    _("Sending edit request to Replicate..."), PROGRESS_PROCESS
                ):
                    return None, _("Operation cancelled")

                output = self._execute_api_call(model_input, progress_callback)
                if isinstance(output, str):
                    return None, output

            return self._process_response(
                output, progress_callback, is_edit=True
            )

        except InputValidationError as e:
            return None, str(e)
        except Exception as e:
            return None, _("Unexpected error: {error}").format(error=str(e))

    def generate_image(
        self,
        prompt: str,
        reference_images: list[str] | None = None,
        progress_callback: Callable[[str, float | None], bool] | None = None,
    ) -> tuple[list[GdkPixbuf.Pixbuf] | None, str | None]:
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
            - If successful: (list[GdkPixbuf.Pixbuf], None)
            - If failed: (None, error_message)
            - If cancelled: (None, "Operation cancelled")
        """
        if not self.client:
            return None, _(
                "Replicate API not available. Please install replicate"
            )

        try:
            reference_images = list(reference_images or [])
            validate_request(self.model, "generate", len(reference_images))
            with self._prepare_reference_images(reference_images) as ref_files:
                if progress_callback and not progress_callback(
                    _("Generating image with Replicate..."), PROGRESS_PREPARE
                ):
                    return None, _("Operation cancelled")

                user_settings = get_model_settings(self.model.name)
                model_input = self.model.build_generation_input(
                    prompt=prompt,
                    reference_images=ref_files if ref_files else None,
                    user_settings=user_settings,
                )

                if progress_callback and not progress_callback(
                    _("Sending request to Replicate..."), PROGRESS_PROCESS
                ):
                    return None, _("Operation cancelled")

                output = self._execute_api_call(model_input, progress_callback)
                if isinstance(output, str):
                    return None, output

            return self._process_response(output, progress_callback)

        except InputValidationError as e:
            return None, str(e)
        except Exception as e:
            return None, _("Unexpected error: {error}").format(error=str(e))

    def _bytes_to_pixbuf(self, image_bytes: bytes) -> GdkPixbuf.Pixbuf | None:
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

    def _download_from_url(self, url: str) -> bytes | None:
        """
        Download image data from URL.

        Args:
            url: Image URL to download

        Returns:
            Image data as bytes, or None if download failed
        """
        try:
            with urllib.request.urlopen(
                url, timeout=DOWNLOAD_TIMEOUT_SECONDS
            ) as url_response:
                return url_response.read()
        except Exception as e:
            print(f"Error downloading from URL {url}: {e}")
            return None

    def _execute_api_call(
        self,
        model_input: dict,
        progress_callback: Callable[[str, float | None], bool] | None = None,
    ) -> object | str:
        """
        Create a prediction and poll it until it completes.

        Polling with short requests instead of one long blocking call
        avoids the HTTP read timeout on slow generations and lets the
        user cancel a running prediction between polls.

        Args:
            model_input: Input parameters for the model
            progress_callback: Progress callback function; returning
                False cancels the prediction on Replicate

        Returns:
            API response output or error message string
        """
        try:
            strategy = self.model.file_encoding_strategy
            if strategy:
                prediction = self.client.models.predictions.create(
                    model=self.model.name,
                    input=model_input,
                    wait=False,
                    file_encoding_strategy=strategy,
                )
            else:
                prediction = self.client.models.predictions.create(
                    model=self.model.name,
                    input=model_input,
                    wait=False,
                )

            while prediction.status not in (
                "succeeded",
                "failed",
                "canceled",
            ):
                if progress_callback and not progress_callback(
                    _("Waiting for Replicate..."), PROGRESS_PROCESS
                ):
                    try:
                        prediction.cancel()
                    except Exception as e:
                        print(f"Error cancelling prediction: {e}")
                    return _("Operation cancelled")

                time.sleep(self.client.poll_interval)
                prediction.reload()

            if prediction.status == "canceled":
                return _("Operation cancelled")

            if prediction.status == "failed":
                error_detail = str(prediction.error or "prediction failed")
                error_msg = _("Model error: {error}").format(error=error_detail)
                if prediction.logs:
                    error_msg += f"\n{_('Logs')}: {prediction.logs}"
                return error_msg

            if isinstance(prediction.output, str):
                # Callers treat string results as error messages, so a
                # bare URL output must be wrapped in a list
                return [prediction.output]

            return prediction.output

        except ModelError as e:
            error_msg = _("Model error: {error}").format(error=str(e))
            if (
                hasattr(e, "prediction")
                and e.prediction
                and hasattr(e.prediction, "logs")
                and e.prediction.logs
            ):
                error_msg += f"\n{_('Logs')}: {e.prediction.logs}"
            return error_msg

        except ReplicateError as e:
            return _("Replicate API error: {error}").format(error=str(e))

        except httpx.HTTPError as e:
            return _("Network error: {error}").format(error=str(e))

    @contextmanager
    def _prepare_reference_images(self, reference_images: list[str] | None):
        """Keep validated snapshots alive through upload; never omit inputs."""
        with ExitStack() as stack:
            file_handles = [
                stack.enter_context(prepare_reference_image(self.model, path))
                for path in reference_images or []
            ]
            yield file_handles

    def _process_api_response(self, output) -> list[bytes]:
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
        progress_callback: Callable[[str, float | None], bool] | None = None,
        is_edit: bool = False,
    ) -> tuple[list[GdkPixbuf.Pixbuf] | None, str | None]:
        """
        Process API response and convert to pixbufs.

        Args:
            output: API response object
            progress_callback: Progress callback function
            is_edit: Whether this response completes an edit operation

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
                if is_edit
                else _("Image generation complete!")
            )
            progress_callback(operation_complete_msg, PROGRESS_COMPLETE)

        return pixbufs, None
