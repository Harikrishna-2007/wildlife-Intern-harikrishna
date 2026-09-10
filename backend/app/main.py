from datetime import datetime, timezone
from uuid import uuid4

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel, Field

from app.core.scoring import ecosystem_health_score
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok"}

app = FastAPI(
    title="Wildlife Population Intelligence Inference API",
    version="0.1.0",
    description="Asynchronous model-service boundary for image, audio, biodiversity, and ecosystem scoring.",
)


class ScoreRequest(BaseModel):
    species_diversity: float = Field(ge=0, le=100)
    population_stability: float = Field(ge=0, le=100)
    habitat_quality: float = Field(ge=0, le=100)
    endangered_status: float = Field(ge=0, le=100)
    environmental_conditions: float = Field(ge=0, le=100)


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/analysis/image")
async def analyze_image(file: UploadFile = File(...)) -> dict:
    return {
        "id": str(uuid4()),
        "mode": "image",
        "status": "processing",
        "filename": file.filename,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "pipeline": "yolov8-species-classification",
    }


@app.post("/v1/analysis/audio")
async def analyze_audio(file: UploadFile = File(...)) -> dict:
    return {
        "id": str(uuid4()),
        "mode": "audio",
        "status": "processing",
        "filename": file.filename,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "pipeline": "birdnet-yamnet",
    }


@app.post("/v1/scoring/ecosystem-health")
def score_ecosystem(payload: ScoreRequest) -> dict[str, float]:
    return {"score": ecosystem_health_score(payload.model_dump())}
