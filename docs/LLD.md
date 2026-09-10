# Low-Level Design

## API contract

The authoritative contract is `lib/api-spec/openapi.yaml`. Current vertical-slice routes:

`GET /dashboard/summary`, `GET /dashboard/trends`, `GET /dashboard/activity`, `GET/POST /surveys`, `GET /surveys/{id}`, `GET/POST /observations`, `GET /species`, `GET /alerts`, `POST /alerts/{id}/acknowledge`, `GET/POST /reports`, `GET /map/points`, `POST /analysis/image`, and `POST /analysis/audio`.

## Model pipeline boundaries

- `ImageIngestor`: MIME/type validation, object-storage handoff, EXIF/GPS extraction.
- `DetectionPipeline`: YOLOv8 boxes, confidence thresholding, NMS, crop extraction.
- `SpeciesClassifier`: taxonomy lookup, classifier score calibration, endangered-status enrichment.
- `AudioPreprocessor`: resampling, channel normalization, noise floor estimation, Librosa spectrogram.
- `BioacousticPipeline`: BirdNET primary prediction, YAMNet fallback, top-k score aggregation.
- `PopulationService`: count correction, effort normalization, density, richness, and trend windows.
- `RecommendationService`: weighted risk signals mapped to conservation actions with explanations.

## Security

- JWT audience and issuer are verified at the gateway.
- Refresh tokens are hashed and rotated; reuse revokes the session family.
- Object paths are private and accessed with short-lived signed URLs.
- Model services never receive browser tokens; workers use service identity.
