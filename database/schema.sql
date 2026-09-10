-- Production reference schema. The Drizzle schema is the application source of truth.
CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS locations (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name text NOT NULL,
  protected_area text NOT NULL,
  latitude double precision NOT NULL,
  longitude double precision NOT NULL,
  habitat_class text,
  geom geometry(Point, 4326),
  metadata jsonb
);

CREATE INDEX IF NOT EXISTS locations_geom_gix ON locations USING gist (geom);
CREATE INDEX IF NOT EXISTS locations_protected_area_idx ON locations (protected_area);

CREATE TABLE IF NOT EXISTS species (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  common_name text NOT NULL,
  scientific_name text UNIQUE NOT NULL,
  family text NOT NULL,
  order_name text,
  conservation_status text NOT NULL,
  population_estimate integer,
  taxonomy_source text
);

CREATE TABLE IF NOT EXISTS observations (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  survey_id uuid,
  location_id uuid NOT NULL REFERENCES locations(id),
  species_id uuid NOT NULL REFERENCES species(id),
  source text NOT NULL,
  count integer NOT NULL CHECK (count > 0),
  confidence double precision NOT NULL CHECK (confidence >= 0 AND confidence <= 1),
  observed_at timestamptz NOT NULL,
  media_object_path text,
  model_version text,
  metadata jsonb
);

CREATE INDEX IF NOT EXISTS observations_species_idx ON observations (species_id);
CREATE INDEX IF NOT EXISTS observations_observed_at_idx ON observations (observed_at DESC);
