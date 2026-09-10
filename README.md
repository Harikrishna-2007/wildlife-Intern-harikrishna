# Wildlife Population Intelligence System

Wildlife Population Intelligence System is a conservation operations workspace for turning camera-trap, acoustic, field, habitat, and GIS observations into action. The first vertical slice includes a populated monitoring dashboard, survey management, observations, species intelligence, alert triage, report queueing, analysis-job simulation, and GIS monitoring context.

## Product surface

- Role-aware workspace for wildlife researchers, conservation officers, forest officers, and administrators.
- Dashboard KPIs for active surveys, detections, observations, ecosystem health, alerts, and protected-area coverage.
- Survey creation, observation capture, species search, conservation alert acknowledgement, report queueing, and analysis job submission.
- OpenAPI-first contracts in `lib/api-spec/openapi.yaml`.
- Typed React Query hooks in `lib/api-client-react`.
- Shared PostgreSQL schema in `lib/db/src/schema/index.ts`.
- Architecture, database, deployment, testing, and model pipeline documentation in `docs/`.

## Run

```bash
pnpm install
pnpm --filter @workspace/api-server run dev
```

The frontend is served by the managed `artifacts/wildlife-intelligence: web` workflow. The API is served under `/api`.

## Regenerate API clients

```bash
pnpm --filter @workspace/api-spec run codegen
```

## Validate

```bash
pnpm run typecheck
pnpm --filter @workspace/api-server run typecheck
pnpm --filter @workspace/wildlife-intelligence run typecheck
```

## Architecture note

The demo vertical slice uses an Express API gateway with typed in-memory seed data so the product can be explored immediately. The persistence boundary is already modeled in Drizzle/PostgreSQL and the AI service boundaries are documented for the FastAPI/PyTorch/TensorFlow deployment described in `docs/HLD.md` and `docs/LLD.md`.
