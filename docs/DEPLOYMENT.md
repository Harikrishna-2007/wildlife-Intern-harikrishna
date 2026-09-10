# Deployment Guide

## Local

```bash
cp .env.example .env
docker compose -f docker/docker-compose.yml up --build
```

## AWS-ready topology

- ECS/Fargate or EKS for web, gateway, workers, and inference services.
- RDS PostgreSQL with PostGIS and Multi-AZ.
- DocumentDB or managed MongoDB for flexible inference metadata.
- S3 for media and report objects.
- ElastiCache/Redis for queues and aggregate caching.
- SES or a transactional email provider for alerts.
- CloudWatch/OpenTelemetry for logs, traces, and model metrics.

## Operational controls

- Run migrations as a release step, never on application startup.
- Use blue/green deployment for API and workers.
- Pin model images by digest and record model checksum in `model_versions`.
- Back up PostgreSQL daily and test restore quarterly.
