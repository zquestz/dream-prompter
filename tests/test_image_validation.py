"""Offline input-policy and upload-metadata tests; no image codecs required."""

import base64
import io
import mimetypes
import runpy
import tempfile
import unittest
from email import policy
from email.parser import BytesParser
from pathlib import Path
from typing import Any
from unittest.mock import Mock, patch

import gi
import httpx
from replicate.client import Client
from replicate.helpers import encode_json

gi.require_version("GdkPixbuf", "2.0")
gi.require_version("Gimp", "3.0")
gi.require_version("Gtk", "3.0")

from gi.repository import GdkPixbuf, Gtk, Pango  # noqa: E402

from api import ReplicateAPI  # noqa: E402
from dialog_events import DreamPrompterEventHandler  # noqa: E402
from dialog_gtk import DreamPrompterUI  # noqa: E402
from image_validation import (  # noqa: E402
    InputValidationError,
    detect_image_mime_type,
    prepare_reference_image,
    validate_image,
    validate_request,
)
from models import BaseModel  # noqa: E402
from models.factory import get_all_models  # noqa: E402

# Generation references, additional edit references, reference MiB, input field.
EXPECTED = {
    "black-forest-labs/flux-2-pro": (8, 7, 10, "input_images"),
    "openai/gpt-image-1.5": (10, 0, 10, "input_images"),
    "openai/gpt-image-2": (10, 0, 10, "input_images"),
    "openai/gpt-image-2.5-sunburst": (10, 9, 10, "input_images"),
    "xai/grok-imagine-image-2": (1, 0, 10, "image"),
    "google/imagen-4": (0, 0, 0, None),
    "google/nano-banana": (10, 9, 7, "image_input"),
    "google/nano-banana-2": (14, 13, 10, "image_input"),
    "google/nano-banana-pro": (14, 13, 10, "image_input"),
    "qwen/qwen-image-2-pro": (1, 0, 10, "image"),
    "qwen/qwen-image-edit-2511": (0, 9, 10, "image"),
    "bytedance/seedream-5-pro": (10, 9, 10, "image_input"),
    "stability-ai/stable-diffusion-3.5-large-turbo": (1, 0, 10, "image"),
}


class ValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.models = get_all_models()
        cls.png = base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8"
            "/x8AAwMCAO+aPd8AAAAASUVORK5CYII="
        )
        cls.formats = {
            "png": cls.png,
            "jpeg": base64.b64decode(
                "/9j/4AAQSkZJRgABAgAAAQABAAD/wAARCAADAAIDAREAAhEBAxEB/9sAQwAD"
                "AgIDAgIDAwMDBAMDBAUIBQUEBAUKBwcGCAwKDAwLCgsLDQ4SEA0OEQ4LCxAW"
                "EBETFBUVFQwPFxgWFBgSFBUU/9sAQwEDBAQFBAUJBQUJFA0LDRQUFBQUFBQU"
                "FBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQU"
                "/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIE"
                "AwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2Jy"
                "ggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlq"
                "c3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLD"
                "xMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEB"
                "AQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3"
                "AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcY"
                "GRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6"
                "goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK"
                "0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDxKvij"
                "+4D/2Q=="
            ),
            "webp": base64.b64decode(
                "UklGRpYAAABXRUJQVlA4TIoAAAAvAYAAAM1VICICHogEAAAAAIABAAAADAAA"
                "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAHggAQAAAAAA5x8AAAAAAAAA"
                "AAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAA4IEEAAAAAACcfwCAAAAAAAAAAAAA"
                "AAAAAAAAAAAAAAAAAAAAAAAAAABA5Ac="
            ),
            "gif": base64.b64decode(
                "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
            ),
        }

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "reference.png"
        self.path.write_bytes(self.png)
        self.model = self.models["google/nano-banana"]

    def make_api(self, model) -> Any:
        api = ReplicateAPI.__new__(ReplicateAPI)
        api.model = model
        api.client = Mock()
        api._execute_api_call = Mock(return_value=[b"output"])
        api._process_response = Mock(return_value=([Mock()], None))
        return api

    def make_references(self, count):
        paths = []
        expected = []
        for index in range(count):
            path = Path(self.directory.name) / f"reference-{index}.png"
            data = self.png + f"reference-{index}".encode("ascii")
            path.write_bytes(data)
            paths.append(str(path))
            expected.append((path.name, data))
        return paths, expected

    def test_registry_limits_and_modes(self):
        self.assertEqual(set(self.models), set(EXPECTED))
        for name, model in self.models.items():
            generation, editing, size, _field = EXPECTED[name]
            with self.subTest(model=name):
                self.assertEqual(model.max_reference_images, generation)
                self.assertEqual(model.max_reference_images_edit, editing)
                self.assertEqual(model.max_file_size_mb, size)
                for mode, limit in (
                    ("generate", generation),
                    ("edit", editing),
                ):
                    if model.is_mode_supported(mode):
                        validate_request(model, mode, limit)
                        with self.assertRaises(InputValidationError):
                            validate_request(model, mode, limit + 1)
                    else:
                        with self.assertRaises(InputValidationError):
                            validate_request(model, mode, 0)

    def test_zero_limit_translations_preserve_literal_braces(self):
        for name, mode in (
            ("google/imagen-4", "generate"),
            ("xai/grok-imagine-image-2", "edit"),
        ):
            for message in ("Translated {literal} text", "Translated { text"):
                with self.subTest(model=name, message=message):
                    with (
                        patch("image_validation._", return_value=message),
                        self.assertRaises(InputValidationError) as error,
                    ):
                        validate_request(self.models[name], mode, 1)
                    self.assertEqual(str(error.exception), message)

    def test_detected_formats_for_every_model(self):
        for name, model in self.models.items():
            for format_name, data in self.formats.items():
                mime = "image/" + format_name
                with self.subTest(model=name, format=format_name):
                    if mime in model.supported_mime_types:
                        self.assertEqual(
                            validate_image(model, data, "reference"), mime
                        )
                    else:
                        with self.assertRaisesRegex(
                            InputValidationError, "unsupported file format"
                        ):
                            validate_image(model, data, "reference")

    def test_exact_file_size_limits_for_every_input_model(self):
        for name, model in self.models.items():
            if not model.supported_mime_types:
                continue
            with self.subTest(model=name):
                maximum = model.max_file_size_mb * 1024 * 1024
                data = self.png.ljust(maximum, b"\0")
                self.assertTrue(model.validate_file_size(maximum))
                self.path.write_bytes(data)
                with prepare_reference_image(model, str(self.path)) as image:
                    self.assertEqual(image.read(), data)
                self.path.write_bytes(data + b"x")
                with self.assertRaisesRegex(InputValidationError, "MiB"):
                    prepare_reference_image(model, str(self.path))
                self.assertFalse(model.validate_file_size(0))
                self.assertFalse(model.validate_file_size(-1))

    def test_reference_read_is_bounded(self):
        source = Mock()
        maximum = self.model.max_file_size_mb * 1024 * 1024
        source.read.return_value = self.png.ljust(maximum + 1, b"\0")
        with patch("image_validation.Path.open") as opened:
            opened.return_value.__enter__.return_value = source
            with self.assertRaisesRegex(InputValidationError, "MiB"):
                prepare_reference_image(self.model, str(self.path))
        source.read.assert_called_once_with(maximum + 1)
        opened.return_value.__exit__.assert_called_once()

    def test_reference_uses_model_size_validation_after_empty_check(self):
        for data in (b"", self.png):
            with self.subTest(empty=not data):
                self.path.write_bytes(data)
                message = "MiB" if data else "is empty"
                with (
                    patch.object(
                        self.model, "validate_file_size", return_value=False
                    ) as check,
                    self.assertRaisesRegex(InputValidationError, message),
                ):
                    prepare_reference_image(self.model, str(self.path))
                if data:
                    check.assert_called_once_with(len(data))
                else:
                    check.assert_not_called()

    def test_empty_and_unrecognized_files(self):
        for data, message in (
            (b"", "is empty"),
            (b"not an image", "unsupported file format"),
            (b"%PDF-1.7", "unsupported file format"),
            (b"RIFF\0\0\0\0WAVE", "unsupported file format"),
        ):
            with self.subTest(data=data):
                self.path.write_bytes(data)
                with self.assertRaisesRegex(InputValidationError, message):
                    prepare_reference_image(self.model, str(self.path))

    def test_complete_and_incomplete_signatures(self):
        for signature, mime in (
            (b"\x89PNG\r\n\x1a\n", "image/png"),
            (b"\xff\xd8\xff", "image/jpeg"),
            (b"GIF87a", "image/gif"),
            (b"GIF89a", "image/gif"),
            (b"RIFF\x20\0\0\0WEBP", "image/webp"),
        ):
            with self.subTest(signature=signature):
                self.assertEqual(detect_image_mime_type(signature), mime)
                for length in range(len(signature)):
                    self.assertIsNone(
                        detect_image_mime_type(signature[:length])
                    )

    def test_filenames_do_not_determine_mime_or_change_local_files(self):
        model = self.models["black-forest-labs/flux-2-pro"]
        for format_name, data in self.formats.items():
            extension = ".jpg" if format_name == "jpeg" else "." + format_name
            for filename in (
                "reference.jpg",
                "reference.txt",
                "reference.PNG",
                "reference",
                ".reference",
                "reference.tar.gz",
            ):
                with self.subTest(format=format_name, filename=filename):
                    path = Path(self.directory.name) / filename
                    path.write_bytes(data)
                    with prepare_reference_image(model, str(path)) as image:
                        self.assertEqual(
                            image.name, path.with_suffix(extension).name
                        )
                        self.assertEqual(image.tell(), 0)
                        self.assertEqual(image.read(), data)
                    self.assertEqual(path.read_bytes(), data)

    def test_input_validation_does_not_decode_images(self):
        self.path.write_bytes(self.png[:8] + b"not decodable image data")
        with (
            patch.object(
                GdkPixbuf,
                "PixbufLoader",
                side_effect=AssertionError("Inputs must not be decoded"),
            ),
            prepare_reference_image(self.model, str(self.path)) as image,
        ):
            self.assertEqual(image.read(), self.path.read_bytes())

    def test_import_registers_missing_and_incorrect_upload_mime_types(self):
        expected = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".webp": "image/webp",
            ".gif": "image/gif",
        }
        module_path = (
            Path(__file__).resolve().parents[1] / "image_validation.py"
        )
        # Initialize the lazy database before replacing the host mappings.
        mimetypes.guess_type("initialize.png")
        for incorrect in (False, True):
            initial = (
                dict.fromkeys(expected, "application/octet-stream")
                if incorrect
                else {}
            )
            with (
                self.subTest(incorrect=incorrect),
                patch.dict(mimetypes.types_map, initial, clear=True),
            ):
                for extension, mime in expected.items():
                    self.assertNotEqual(
                        mimetypes.guess_type("upload" + extension)[0], mime
                    )
                # Keep the API's imported exception class intact.
                runpy.run_path(str(module_path))
                for extension, mime in expected.items():
                    self.assertEqual(
                        mimetypes.guess_type("upload" + extension)[0], mime
                    )

    def test_sdk_uses_detected_mime_for_data_uris_and_uploads(self):
        model = self.models["black-forest-labs/flux-2-pro"]
        url = "https://example.invalid/offline-upload"
        for format_name, data in self.formats.items():
            mime = "image/" + format_name
            for strategy in ("base64", "url"):
                with self.subTest(format=format_name, strategy=strategy):
                    self.path.write_bytes(data)
                    response = {
                        "id": "offline",
                        "name": "upload",
                        "content_type": mime,
                        "size": len(data),
                        "etag": "offline",
                        "checksums": {},
                        "metadata": {},
                        "created_at": "2026-10-06T00:00:00Z",
                        "expires_at": None,
                        "urls": {"get": url},
                    }
                    requests = []

                    def upload(
                        request,
                        requests=requests,
                        response=response,
                        mime=mime,
                        data=data,
                    ):
                        requests.append(request)
                        self.assertEqual(request.method, "POST")
                        self.assertEqual(request.url.path, "/v1/files")
                        headers = (
                            "Content-Type: "
                            + request.headers["Content-Type"]
                            + "\r\nMIME-Version: 1.0\r\n\r\n"
                        ).encode("ascii")
                        message = BytesParser(policy=policy.default).parsebytes(
                            headers + request.read()
                        )
                        parts = list(message.iter_parts())
                        self.assertEqual(len(parts), 1)
                        part = parts[0]
                        self.assertEqual(
                            part.get_param(
                                "name", header="content-disposition"
                            ),
                            "content",
                        )
                        extension = (
                            ".jpg"
                            if mime == "image/jpeg"
                            else "." + mime.split("/")[1]
                        )
                        self.assertEqual(
                            part.get_filename(), "reference" + extension
                        )
                        self.assertEqual(part.get_content_type(), mime)
                        self.assertEqual(part.get_payload(decode=True), data)
                        return httpx.Response(201, json=response)

                    with (
                        httpx.MockTransport(upload) as transport,
                        prepare_reference_image(model, str(self.path)) as image,
                    ):
                        client = Client(
                            api_token="offline-test",
                            base_url="https://example.invalid",
                            transport=transport,
                        )
                        encoded = encode_json(
                            {"image": image}, client, strategy
                        )
                        if strategy == "base64":
                            self.assertEqual(
                                encoded["image"],
                                f"data:{mime};base64,"
                                + base64.b64encode(data).decode("ascii"),
                            )
                            self.assertEqual(requests, [])
                        else:
                            self.assertEqual(encoded["image"], url)
                            self.assertEqual(len(requests), 1)

    def test_missing_directory_and_unreadable_paths(self):
        for path in (self.path.parent / "missing.png", self.path.parent):
            with self.assertRaisesRegex(InputValidationError, "Could not read"):
                prepare_reference_image(self.model, str(path))
        with (
            patch.object(Path, "open", side_effect=PermissionError),
            self.assertRaisesRegex(InputValidationError, "Could not read"),
        ):
            prepare_reference_image(self.model, str(self.path))

    def test_reference_is_an_unchanged_rewound_snapshot(self):
        with prepare_reference_image(self.model, str(self.path)) as image:
            self.path.write_bytes(b"changed after validation")
            self.assertEqual(image.tell(), 0)
            self.assertEqual(image.name, "reference.png")
            self.assertEqual(image.read(), self.png)

    def test_gif_bytes_are_preserved(self):
        gif = self.formats["gif"]
        # Two frames sharing the fixture's logical screen and color table.
        animated = gif[:19] + gif[19:-1] * 2 + gif[-1:]
        path = self.path.with_suffix(".gif")
        path.write_bytes(animated)
        for name in (
            "black-forest-labs/flux-2-pro",
            "qwen/qwen-image-edit-2511",
        ):
            with (
                self.subTest(model=name),
                prepare_reference_image(self.models[name], str(path)) as image,
            ):
                self.assertEqual(image.read(), animated)

    @patch("api.get_model_settings", return_value={})
    @patch("api.integrator.export_current_region_to_bytes")
    def test_all_model_payloads_preserve_inputs(self, export, _settings):
        export.return_value = self.png
        for name, model in self.models.items():
            for mode in ("generate", "edit"):
                if not model.is_mode_supported(mode):
                    continue
                with self.subTest(model=name, mode=mode):
                    api = self.make_api(model)
                    limit = (
                        model.max_reference_images_edit
                        if mode == "edit"
                        else model.max_reference_images
                    )
                    field = EXPECTED[name][3]
                    references, expected = self.make_references(limit)
                    if mode == "edit":
                        expected.insert(0, ("image.png", self.png))
                    uploads = []

                    def capture(
                        inputs,
                        _callback,
                        field=field,
                        uploads=uploads,
                        expected=expected,
                    ):
                        files = inputs.get(field, []) if field else []
                        if not isinstance(files, list):
                            files = [files]
                        uploads.extend(files)
                        self.assertEqual(len(files), len(expected))
                        for image in files:
                            self.assertEqual(image.tell(), 0)
                        self.assertEqual(
                            [(image.name, image.read()) for image in files],
                            expected,
                        )
                        return [b"output"]

                    api._execute_api_call.side_effect = capture
                    if mode == "edit":
                        _result, error = api.edit_image(
                            Mock(), "edit", references
                        )
                    else:
                        _result, error = api.generate_image("new", references)
                    self.assertIsNone(error)
                    api._execute_api_call.assert_called_once()
                    self.assertTrue(all(image.closed for image in uploads))

    @patch("api.get_model_settings", return_value={})
    @patch("api.integrator.export_current_region_to_bytes")
    def test_request_snapshots_references_before_validation(
        self, export, _settings
    ):
        export.return_value = self.png
        for mode in ("generate", "edit"):
            for mutation_point in ("count", "reference"):
                with self.subTest(mode=mode, mutation_point=mutation_point):
                    api = self.make_api(self.model)
                    references, expected = self.make_references(3)
                    original_paths = references.copy()
                    if mode == "edit":
                        expected.insert(0, ("image.png", self.png))
                    uploaded = []

                    def check_count(
                        model,
                        operation,
                        count,
                        mutation_point=mutation_point,
                        references=references,
                    ):
                        validate_request(model, operation, count)
                        if mutation_point == "count":
                            references.pop(0)

                    def prepare(
                        model,
                        path,
                        mutation_point=mutation_point,
                        references=references,
                        first_path=original_paths[0],
                    ):
                        snapshot = prepare_reference_image(model, path)
                        if mutation_point == "reference" and path == first_path:
                            references.pop(0)
                        return snapshot

                    def capture(inputs, _callback, uploaded=uploaded):
                        uploaded.extend(
                            (image.name, image.read())
                            for image in inputs["image_input"]
                        )
                        return [b"output"]

                    api._execute_api_call.side_effect = capture
                    with (
                        patch("api.validate_request", side_effect=check_count),
                        patch(
                            "api.prepare_reference_image", side_effect=prepare
                        ) as preparation,
                    ):
                        if mode == "edit":
                            _result, error = api.edit_image(
                                Mock(), "edit", references
                            )
                        else:
                            _result, error = api.generate_image(
                                "new", references
                            )
                    self.assertIsNone(error)
                    self.assertEqual(references, original_paths[1:])
                    self.assertEqual(
                        [args[0][1] for args in preparation.call_args_list],
                        original_paths,
                    )
                    self.assertEqual(uploaded, expected)
                    api._execute_api_call.assert_called_once()

    @patch("api.get_model_settings", return_value={})
    @patch("api.integrator.export_current_region_to_bytes")
    def test_invalid_requests_never_reach_replicate(self, export, _settings):
        export.return_value = self.png
        for name, model in self.models.items():
            for mode in ("generate", "edit"):
                limit = (
                    model.max_reference_images_edit
                    if mode == "edit"
                    else model.max_reference_images
                )
                cases = [[str(self.path)] * (limit + 1), ["/missing.png"]]
                if not model.is_mode_supported(mode):
                    cases.append([])
                for references in cases:
                    with self.subTest(model=name, mode=mode, refs=references):
                        api = self.make_api(model)
                        if mode == "edit":
                            result, error = api.edit_image(
                                Mock(), "p", references
                            )
                        else:
                            result, error = api.generate_image("p", references)
                        self.assertIsNone(result)
                        self.assertTrue(error)
                        self.assertNotIn("Unexpected error", error)
                        api._execute_api_call.assert_not_called()

    @patch("api.get_model_settings", return_value={})
    @patch("api.integrator.export_current_region_to_bytes")
    def test_edit_checks_export_without_reference_size_cap(
        self, export, _settings
    ):
        canvas = Mock()
        canvas.get_width.return_value = 10000
        canvas.get_height.return_value = 10000
        for name, model in self.models.items():
            if not model.supports_editing():
                continue
            api = self.make_api(model)
            over_limit = model.max_file_size_mb * 1024 * 1024 + 1
            for data, valid in (
                (self.png, True),
                (b"invalid PNG", False),
                (self.png.ljust(over_limit, b"\0"), True),
            ):
                with self.subTest(model=name, size=len(data)):
                    export.return_value = data
                    api._execute_api_call.reset_mock()
                    _result, error = api.edit_image(canvas, "edit selection")
                    export.assert_called_with(canvas)
                    self.assertEqual(error is None, valid)
                    if valid:
                        api._execute_api_call.assert_called_once()
                    else:
                        self.assertIn("unsupported file format", error)
                        api._execute_api_call.assert_not_called()
        canvas.get_width.assert_not_called()
        canvas.get_height.assert_not_called()

    @patch("api.get_model_settings", return_value={})
    @patch("api.integrator.export_current_region_to_bytes")
    def test_cancellation_and_api_failure_close_snapshots(
        self, export, _settings
    ):
        export.return_value = self.png
        for mode in ("generate", "edit"):
            for cancel in (True, False):
                with self.subTest(mode=mode, cancel=cancel):
                    api = self.make_api(self.model)
                    snapshot = prepare_reference_image(
                        self.model, str(self.path)
                    )
                    callback = (
                        Mock(side_effect=[True, False])
                        if mode == "edit"
                        else Mock(return_value=False)
                    )
                    api._execute_api_call.side_effect = RuntimeError(
                        "API failed"
                    )
                    main_images = []
                    bytes_io = io.BytesIO

                    def create_main(
                        data, main_images=main_images, bytes_io=bytes_io
                    ):
                        main = bytes_io(data)
                        main_images.append(main)
                        return main

                    with (
                        patch(
                            "api.prepare_reference_image", return_value=snapshot
                        ),
                        patch("api.io.BytesIO", side_effect=create_main),
                    ):
                        if mode == "edit":
                            _result, error = api.edit_image(
                                Mock(),
                                "edit",
                                [str(self.path)],
                                callback if cancel else None,
                            )
                        else:
                            _result, error = api.generate_image(
                                "new",
                                [str(self.path)],
                                callback if cancel else None,
                            )
                    self.assertTrue(snapshot.closed)
                    self.assertEqual(len(main_images), int(mode == "edit"))
                    self.assertTrue(all(main.closed for main in main_images))
                    self.assertTrue(error)
                    if cancel:
                        self.assertEqual(error, "Operation cancelled")
                        api._execute_api_call.assert_not_called()
                    else:
                        api._execute_api_call.assert_called_once()

    def test_snapshots_close_when_later_reference_fails(self):
        api = self.make_api(self.model)
        snapshot = io.BytesIO(self.png)
        with (
            patch(
                "api.prepare_reference_image",
                side_effect=[snapshot, InputValidationError("bad reference")],
            ),
            self.assertRaises(InputValidationError),
            api._prepare_reference_images(["first.png", "bad.png"]),
        ):
            self.fail("Invalid references must not yield")
        self.assertTrue(snapshot.closed)

    @patch("api.get_model_settings", return_value={})
    def test_generation_without_references(self, _settings):
        for name, model in self.models.items():
            if model.supports_generation():
                with self.subTest(model=name):
                    api = self.make_api(model)
                    _result, error = api.generate_image("text only")
                    self.assertIsNone(error)
                    api._execute_api_call.assert_called_once()

    def test_default_edit_count_reserves_main_image(self):
        model_type = type(self.model)
        for count in (0, 1, 2, 10):
            with (
                self.subTest(count=count),
                patch.object(
                    model_type,
                    "max_reference_images",
                    property(lambda _, count=count: count),
                ),
                patch.object(
                    model_type,
                    "max_reference_images_edit",
                    BaseModel.max_reference_images_edit,
                ),
            ):
                self.assertEqual(
                    self.model.max_reference_images_edit, max(0, count - 1)
                )


class DialogValidationTests(unittest.TestCase):
    def setUp(self):
        settings_patcher = patch("dialog_events.store_settings")
        self.store_settings = settings_patcher.start()
        self.addCleanup(settings_patcher.stop)
        self.handler: Any = DreamPrompterEventHandler.__new__(
            DreamPrompterEventHandler
        )
        self.handler.model = get_all_models()["google/nano-banana"]
        self.handler.ui = Mock()
        self.handler.ui.selected_files = [f"{i}.png" for i in range(10)]
        self.handler.dialog = Mock()
        self.handler.dialog.get_current_mode.return_value = "edit"
        self.handler.show_error = Mock()
        self.handler.threads = Mock()
        self.handler.drawable = Mock()

    def test_mode_and_model_changes_preserve_all_references(self):
        files = self.handler.ui.selected_files.copy()
        self.handler.on_mode_changed(Mock())
        self.assertEqual(self.handler.ui.selected_files, files)
        self.handler.on_model_changed(
            Mock(get_active_id=Mock(return_value="google/imagen-4"))
        )
        self.assertEqual(self.handler.ui.selected_files, files)
        self.handler.ui.update_files_display.assert_called()

    def test_excess_references_block_submission(self):
        self.handler.on_generate(Mock())
        self.handler.show_error.assert_called_once()
        self.handler.threads.start_edit_thread.assert_not_called()
        self.store_settings.assert_not_called()

    def test_settings_remain_mocked_when_validation_is_bypassed(self):
        self.handler.ui.selected_files = [f"{i}.png" for i in range(11)]
        for mode in ("generate", "edit"):
            with self.subTest(mode=mode):
                self.handler.dialog.get_current_mode.return_value = mode
                self.store_settings.reset_mock()
                with (
                    patch("dialog_events.validate_request") as validate,
                    patch(
                        "settings.get_config_file",
                        side_effect=AssertionError(
                            "Tests must not access the real settings path"
                        ),
                    ) as config_path,
                ):
                    self.handler.on_generate(Mock())
                validate.assert_called_once_with(self.handler.model, mode, 11)
                self.store_settings.assert_called_once()
                config_path.assert_not_called()
                self.handler.show_error.assert_not_called()
                start = getattr(self.handler.threads, f"start_{mode}_thread")
                start.assert_called_once()

    def test_submission_snapshots_references(self):
        for mode in ("generate", "edit"):
            with self.subTest(mode=mode):
                self.handler.dialog.get_current_mode.return_value = mode
                self.handler.ui.selected_files = ["first.png", "second.png"]
                expected = self.handler.ui.selected_files.copy()
                self.handler.on_generate(Mock())
                start = getattr(self.handler.threads, f"start_{mode}_thread")
                start.assert_called_once()
                submitted = start.call_args.args[2]
                self.assertIsNot(submitted, self.handler.ui.selected_files)
                self.handler.ui.selected_files.pop(0)
                self.assertEqual(submitted, expected)

    def test_processing_disables_reference_removal(self):
        ui = DreamPrompterUI()
        files_listbox = Mock()
        ui.files_listbox = files_listbox
        for enabled in (False, True):
            with self.subTest(enabled=enabled):
                ui.set_ui_enabled(enabled)
                files_listbox.set_sensitive.assert_called_once_with(enabled)
                files_listbox.reset_mock()

    def test_status_label_fills_available_width_and_wraps(self):
        ui = DreamPrompterUI()
        with (
            patch("dialog_gtk.Gtk.Box"),
            patch("dialog_gtk.Gtk.Label") as create_label,
            patch("dialog_gtk.Gtk.ProgressBar"),
        ):
            ui._create_status_section()

        label = create_label.return_value
        label.set_halign.assert_called_once_with(Gtk.Align.FILL)
        label.set_xalign.assert_called_once_with(0)
        label.set_line_wrap.assert_called_once_with(True)
        label.set_line_wrap_mode.assert_called_once_with(
            Pango.WrapMode.WORD_CHAR
        )
        label.set_max_width_chars.assert_called_once_with(70)

    def test_chooser_rejects_entire_excess_batch(self):
        self.handler.ui.selected_files = ["existing.png"]
        chooser = Mock()
        chooser.run.return_value = Gtk.ResponseType.OK
        chooser.get_filenames.return_value = [f"{i}.png" for i in range(9)]
        with patch("dialog_events.Gtk.FileChooserDialog", return_value=chooser):
            self.handler.on_select_files(Mock())
        self.assertEqual(self.handler.ui.selected_files, ["existing.png"])
        self.handler.show_error.assert_called_once()
        message = self.handler.show_error.call_args.args[0]
        self.assertIn("No files were added", message)
        self.assertIn(
            "Already selected: 1; requested: 9; available slots: 8", message
        )
        chooser.destroy.assert_called_once()

    def test_chooser_accepts_exact_capacity_and_cancel_preserves_selection(
        self,
    ):
        for response in (Gtk.ResponseType.OK, Gtk.ResponseType.CANCEL):
            with self.subTest(response=response):
                self.handler.ui.selected_files = ["existing.png"]
                chooser = Mock()
                chooser.run.return_value = response
                files = [f"{i}.png" for i in range(8)]
                chooser.get_filenames.return_value = files
                supported_filter, all_files = Mock(), Mock()
                with (
                    patch(
                        "dialog_events.Gtk.FileChooserDialog",
                        return_value=chooser,
                    ),
                    patch(
                        "dialog_events.Gtk.FileFilter",
                        side_effect=[supported_filter, all_files],
                    ),
                ):
                    self.handler.on_select_files(Mock())
                expected = ["existing.png"]
                if response == Gtk.ResponseType.OK:
                    expected += files
                else:
                    chooser.get_filenames.assert_not_called()
                self.assertEqual(self.handler.ui.selected_files, expected)
                self.handler.show_error.assert_not_called()
                all_files.set_name.assert_called_once_with("All Files")
                all_files.add_pattern.assert_called_once_with("*")
                chooser.add_filter.assert_any_call(all_files)
                chooser.destroy.assert_called_once()

    def test_zero_references_have_mode_specific_errors_and_help(self):
        edit_message = "This model accepts no additional images in edit mode."
        for name, mode, error_message in (
            ("xai/grok-imagine-image-2", "edit", edit_message),
            ("qwen/qwen-image-2-pro", "edit", edit_message),
            (
                "stability-ai/stable-diffusion-3.5-large-turbo",
                "edit",
                edit_message,
            ),
            (
                "google/imagen-4",
                "generate",
                "This model does not support reference images",
            ),
        ):
            with self.subTest(model=name):
                self.handler.model = get_all_models()[name]
                self.handler.dialog.get_current_mode.return_value = mode
                self.handler.ui.selected_files = ["reference"]
                self.handler.update_ui_limits()
                message = (
                    self.handler.ui.images_help_label.set_markup.call_args.args[
                        0
                    ]
                )
                self.assertIn(error_message, message)
                self.assertIn("Remove the selected reference images", message)
                self.assertNotIn("Maximum 0", message)
                with self.assertRaises(InputValidationError) as error:
                    validate_request(self.handler.model, mode, 1)
                self.assertEqual(str(error.exception), error_message)
                validate_request(self.handler.model, mode, 0)
                self.handler.show_error.reset_mock()
                self.handler.on_generate(Mock())
                self.handler.show_error.assert_called_once_with(error_message)
                self.handler.threads.start_generate_thread.assert_not_called()
                self.handler.threads.start_edit_thread.assert_not_called()
                self.store_settings.assert_not_called()
                if mode == "edit":
                    validate_request(self.handler.model, "generate", 1)

    def test_help_escapes_errors(self):
        with patch(
            "dialog_events.validate_request",
            side_effect=InputValidationError("<bad> & invalid"),
        ):
            self.handler.update_ui_limits()
        message = self.handler.ui.images_help_label.set_markup.call_args.args[0]
        self.assertIn("&lt;bad&gt; &amp; invalid", message)
        self.assertNotIn("<bad>", message)

    def test_clear_and_remove_refresh_limits(self):
        self.handler.ui.selected_files = ["first", "second"]
        with patch.object(self.handler, "update_ui_limits") as update:
            self.handler.on_remove_file(Mock(), "first")
            self.assertEqual(self.handler.ui.selected_files, ["second"])
            update.assert_called_once()
            update.reset_mock()
            self.handler.on_clear_files(Mock())
            self.assertEqual(self.handler.ui.selected_files, [])
            update.assert_called_once()

    def test_size_warning_uses_selected_model(self):
        ui = DreamPrompterUI.__new__(DreamPrompterUI)
        with (
            patch("dialog_gtk.os.path.getsize", return_value=8 * 1024 * 1024),
            patch.object(ui, "get_selected_model") as selected,
        ):
            selected.return_value = "google/nano-banana"
            self.assertIn(
                "Max Size Exceeded", ui._get_display_filename("a.png")
            )
            selected.return_value = "google/nano-banana-pro"
            self.assertNotIn(
                "Max Size Exceeded", ui._get_display_filename("a.png")
            )


if __name__ == "__main__":
    unittest.main()
