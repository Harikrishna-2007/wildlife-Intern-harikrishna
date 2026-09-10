"""YOLOv8 wildlife inference.

The default YOLOv8 weights are useful for common COCO wildlife classes. For
the full wildlife taxonomy, set WILDLIFE_MODEL_PATH to a trained YOLOv8
checkpoint whose class names include the supported species below.
"""

from __future__ import annotations

import contextlib
import io
import os
from functools import lru_cache
from pathlib import Path
from typing import Any


SUPPORTED_SPECIES = {
    "elephant": ("Elephant", "Loxodonta africana"),
    "tiger": ("Tiger", "Panthera tigris"),
    "lion": ("Lion", "Panthera leo"),
    "leopard": ("Leopard", "Panthera pardus"),
    "deer": ("Deer", "Cervidae"),
    "bear": ("Bear", "Ursidae"),
    "wolf": ("Wolf", "Canis lupus"),
    "fox": ("Fox", "Vulpes vulpes"),
    "monkey": ("Monkey", "Simiiformes"),
    "zebra": ("Zebra", "Equus quagga"),
    "giraffe": ("Giraffe", "Giraffa camelopardalis"),
    "rhino": ("Rhinoceros", "Rhinocerotidae"),
    "peacock": ("Peacock", "Pavo cristatus"),
    "eagle": ("Eagle", "Accipitridae"),
}

ALIASES = {
    "african elephant": "elephant",
    "asian elephant": "elephant",
    "common zebra": "zebra",
    "rhinoceros": "rhino",
    "white rhinoceros": "rhino",
    "black rhinoceros": "rhino",
    "peafowl": "peacock",
}


@lru_cache(maxsize=1)
def _load_model() -> Any:
    from ultralytics import YOLO

    model_path = os.getenv("WILDLIFE_MODEL_PATH", "yolov8n.pt")
    return YOLO(model_path)


def _canonical_species(label: str) -> str | None:
    normalized = " ".join(label.strip().lower().replace("_", " ").split())
    canonical = ALIASES.get(normalized, normalized)
    if canonical in SUPPORTED_SPECIES:
        return canonical
    return None


def _image_size(path: str) -> tuple[int, int]:
    from PIL import Image

    with Image.open(path) as image:
        return image.width, image.height


def analyze_image(path: str, confidence_threshold: float = 0.35) -> dict:
    image_path = Path(path)
    if not image_path.is_file():
        raise FileNotFoundError(f"Uploaded image does not exist: {path}")

    # Ultralytics writes progress and model download messages to stdout. The
    # worker protocol uses stdout for JSON only, so keep those logs isolated.
    with contextlib.redirect_stdout(io.StringIO()):
        model = _load_model()
        predictions = model.predict(
            source=str(image_path),
            conf=confidence_threshold,
            verbose=False,
        )

    width, height = _image_size(str(image_path))
    detections: list[dict] = []

    for prediction in predictions:
        names = prediction.names
        boxes = prediction.boxes
        if boxes is None:
            continue

        for box in boxes:
            class_id = int(box.cls[0].item())
            raw_label = str(names[class_id])
            canonical = _canonical_species(raw_label)
            if canonical is None:
                continue

            coordinates = [float(value) for value in box.xyxy[0].tolist()]
            x1, y1, x2, y2 = coordinates
            confidence = float(box.conf[0].item())
            common_name, scientific_name = SUPPORTED_SPECIES[canonical]
            detections.append(
                {
                    "species": common_name,
                    "scientificName": scientific_name,
                    "confidence": round(confidence, 4),
                    "boundingBox": {
                        "x": round(max(0, x1), 2),
                        "y": round(max(0, y1), 2),
                        "width": round(max(1, min(width, x2) - max(0, x1)), 2),
                        "height": round(max(1, min(height, y2) - max(0, y1)), 2),
                    },
                }
            )

    average_confidence = (
        sum(item["confidence"] for item in detections) / len(detections)
        if detections
        else 0
    )
    return {
        "model": os.getenv("WILDLIFE_MODEL_PATH", "yolov8n.pt"),
        "confidenceThreshold": confidence_threshold,
        "imageWidth": width,
        "imageHeight": height,
        "animalCount": len(detections),
        "confidence": round(average_confidence, 4),
        "animals": detections,
    }
