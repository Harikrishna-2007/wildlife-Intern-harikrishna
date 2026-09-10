# High-Level Design

## Services

| Service | Responsibility |
| --- | --- |
| Web | React dashboard, role-aware navigation, maps, charts, workflows |
| API gateway | Auth middleware, validation, CRUD, dashboard aggregates |
| Inference service | FastAPI endpoints for image/audio jobs |
| Worker | Queue consumers for inference, reports, alerts, and notifications |
| PostgreSQL/PostGIS | Transactional entities and geographic primitives |
| MongoDB | Flexible inference metadata and model payloads |
| Object storage | Original media, derived crops, spectrograms, and exports |

## Request flow

1. User authenticates through OAuth2/OIDC.
2. Web sends a typed request through the `/api` gateway.
3. Gateway validates the payload and checks role permissions.
4. Metadata is committed to PostgreSQL; media is stored by object path.
5. A job is enqueued for model inference.
6. Worker calls the FastAPI inference service and writes output metadata.
7. Aggregates invalidate and alerts/recommendations are emitted.

## Scoring

`Ecosystem Health = diversity * 0.30 + population stability * 0.25 + habitat quality * 0.20 + endangered status * 0.15 + environmental conditions * 0.10`

Shannon diversity: `H = -Σ(pᵢ ln pᵢ)`. Simpson diversity: `1 - Σ(pᵢ²)`. Each component is normalized to 0–100 before weighting.
