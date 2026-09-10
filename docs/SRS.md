# Software Requirements Specification

## Actors

- **Wildlife researcher:** create surveys, register observations, upload image/audio evidence, and export reports.
- **Conservation officer:** monitor threatened species, biodiversity indicators, recommendations, and alerts.
- **Forest department officer:** inspect protected-area activity, patrol context, movement analytics, and habitat signals.
- **Administrator:** manage users, roles, datasets, model versions, and system analytics.

## Functional requirements

1. The system shall authenticate users through an OAuth2/OIDC provider and issue short-lived JWT access tokens with refresh-token rotation.
2. The system shall enforce role-based permissions on every write endpoint.
3. The system shall store survey, location, device, and observation provenance.
4. The system shall accept image and audio evidence and create asynchronous analysis jobs.
5. The system shall present species, population, biodiversity, habitat, GIS, alert, recommendation, and report views.
6. The system shall support PDF and Excel report generation.
7. The system shall notify authorized users about endangered detections, population declines, and habitat degradation.

## Quality requirements

- p95 dashboard API latency below 500 ms for cached aggregates.
- 99.5% monthly availability for the dashboard API.
- All sensitive routes audited.
- All model outputs include confidence and model version.
- Accessibility target: WCAG 2.2 AA for the operational UI.
