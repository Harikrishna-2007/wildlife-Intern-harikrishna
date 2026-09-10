# Testing Strategy

## Unit

- Validate Shannon, Simpson, density, trend, and ecosystem-health formulas with fixed fixtures.
- Test input schemas for survey, observation, analysis, and report payloads.
- Test role-policy matrices and alert severity mapping.

## Integration

- Run API contract tests against generated OpenAPI clients.
- Exercise survey creation, observation creation, alert acknowledgement, report queueing, and analysis job creation.
- Verify PostGIS spatial filtering and Mongo model-payload persistence.

## End-to-end

- Researcher: create survey -> record observation -> view species -> queue report.
- Conservation officer: open dashboard -> filter endangered species -> acknowledge decline alert.
- Forest officer: open map -> switch layers -> inspect protected-area activity.
- Administrator: inspect system health and dataset/model metadata.

## Model evaluation

- Image: mAP50, mAP50-95, precision, recall, confusion matrix by species.
- Audio: macro F1, top-1/top-5 accuracy, false-positive rate by habitat noise profile.
- Production: confidence drift, data drift, latency, and queue age.
