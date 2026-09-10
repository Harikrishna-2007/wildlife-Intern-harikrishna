"""Persistent stdin/stdout worker for wildlife image inference.

The API server keeps this process alive so the YOLO weights are loaded once
and reused across requests. Each input and output is one JSON line.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.ai.image_analysis import analyze_image


def main() -> None:
    for line in sys.stdin:
        if not line.strip():
            continue

        try:
            payload = json.loads(line)
            result = analyze_image(
                path=str(payload["path"]),
                confidence_threshold=float(payload.get("confidenceThreshold", 0.35)),
            )
            response = {"requestId": payload.get("requestId"), "ok": True, "result": result}
        except Exception as exc:
            response = {
                "requestId": payload.get("requestId") if isinstance(payload, dict) else None,
                "ok": False,
                "error": str(exc) or exc.__class__.__name__,
            }

        print(json.dumps(response, separators=(",", ":")), flush=True)


if __name__ == "__main__":
    main()