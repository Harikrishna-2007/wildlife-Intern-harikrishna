"""BirdNET/YAMNet model boundary with Librosa preprocessing."""


def analyze_audio(path: str, sample_rate: int = 32_000) -> dict:
    return {
        "path": path,
        "sample_rate": sample_rate,
        "models": ["birdnet", "yamnet"],
        "spectrogram": {"kind": "mel", "n_mels": 128},
        "predictions": [],
        "status": "queued",
    }
