"""Validate image uploads locally before creating a Replicate prediction."""

import io
import mimetypes
from pathlib import Path

from i18n import _, ngettext
from models import BaseModel

MIME_EXTENSIONS = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/webp": ".webp",
    "image/gif": ".gif",
}

# Replicate derives MIME from upload names; do not rely on host MIME tables.
for _mime_type, _extension in MIME_EXTENSIONS.items():
    mimetypes.add_type(_mime_type, _extension)


class InputValidationError(ValueError):
    """An actionable input error that should be shown without a traceback."""


def validate_request(model: BaseModel, mode: str, reference_count: int) -> None:
    """Check the operation and additional references, before reading files."""
    if not model.is_mode_supported(mode):
        raise InputValidationError(
            _("The selected model does not support this operation.")
        )

    if mode == "edit":
        maximum = model.max_reference_images_edit
        message = ngettext(
            "Maximum {max} reference image allowed in edit mode.",
            "Maximum {max} reference images allowed in edit mode.",
            maximum,
        )
    else:
        maximum = model.max_reference_images
        message = ngettext(
            "Maximum {max} reference image allowed.",
            "Maximum {max} reference images allowed.",
            maximum,
        )
    if reference_count > maximum:
        if maximum == 0:
            message = (
                _("This model accepts no additional images in edit mode.")
                if mode == "edit"
                else _("This model does not support reference images")
            )
            raise InputValidationError(message)
        raise InputValidationError(message.format(max=maximum))


def detect_image_mime_type(data: bytes) -> str | None:
    """Identify supported image signatures without decoding their contents."""
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "image/png"
    if data.startswith(b"\xff\xd8\xff"):
        return "image/jpeg"
    if data.startswith((b"GIF87a", b"GIF89a")):
        return "image/gif"
    if data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        return "image/webp"
    return None


def validate_image(
    model: BaseModel,
    data: bytes,
    image_name: str,
) -> str:
    """Check nonempty content and supported MIME type, not image integrity."""
    if not data:
        raise InputValidationError(
            _("Image '{image}' is empty.").format(image=image_name)
        )
    mime_type = detect_image_mime_type(data)
    if not mime_type or not model.validate_mime_type(mime_type):
        raise InputValidationError(
            _("Image '{image}' has an unsupported file format.").format(
                image=image_name
            )
        )

    return mime_type


def prepare_reference_image(model: BaseModel, path: str) -> io.BytesIO:
    """Snapshot a reference with an upload suffix matching its detected MIME."""
    image_path = Path(path)
    try:
        if not image_path.is_file():
            raise OSError("Not a regular file")
        with image_path.open("rb") as source:
            data = source.read(model.max_file_size_mb * 1024 * 1024 + 1)
    except OSError as error:
        raise InputValidationError(
            _("Could not read image '{image}'.").format(image=str(image_path))
        ) from error

    mime_type = validate_image(model, data, str(image_path))
    if not model.validate_file_size(len(data)):
        raise InputValidationError(
            _("Image '{image}' exceeds the {max} MiB size limit.").format(
                image=str(image_path), max=model.max_file_size_mb
            )
        )
    image = io.BytesIO(data)
    # Replicate infers upload/data-URI MIME from this name, not the bytes.
    image.name = image_path.with_suffix(MIME_EXTENSIONS[mime_type]).name
    return image
