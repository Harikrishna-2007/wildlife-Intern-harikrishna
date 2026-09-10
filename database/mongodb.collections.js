// MongoDB reference collections for flexible AI output and audit metadata.
db.createCollection("analysis_runs");
db.analysis_runs.createIndex({ surveyId: 1, createdAt: -1 });
db.analysis_runs.createIndex({ model: 1, status: 1 });

db.createCollection("model_versions");
db.model_versions.createIndex({ name: 1, version: 1 }, { unique: true });

db.createCollection("recommendation_explanations");
db.recommendation_explanations.createIndex({ observationId: 1, createdAt: -1 });

db.createCollection("audit_events");
db.audit_events.createIndex({ actorId: 1, createdAt: -1 });