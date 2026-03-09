# UK Health Data Platform

A local-first batch data platform that ingests and standardises multiple UK public health
and population sources to produce validated, period-based datasets suitable for operational
and analytical use.

Built as a companion platform to [batch-data-platform](https://github.com/brett-me/batch-data-platform).
Same engineering backbone, real-source complexity.

## What this platform does

Ingests from three public sources:
- NHS England operational statistics (monthly)
- ONS population and geography reference data (annual)
- OHID / Fingertips public health indicators (varies)

Produces validated, period-based, reconciled datasets with full provenance tracking.

## Quickstart

Requirements: Docker, Docker Compose, Python 3.10+, WSL (Windows)
```bash
git clone <repo-url>
cd uk-health-data-platform
cp .env.example .env
docker compose up -d
docker compose ps   # confirm postgres is healthy
```

## Repository structure

| Path | Purpose |
|---|---|
| `data/raw/` | Local landing zone for raw source files (not committed) |
| `docs/sources/` | Source inventory and provenance notes |
| `sql/ddl/` | Table definitions |
| `scripts/` | Operator scripts (smoke checks, etc.) |
| `src/uk_health_platform/` | Python package |
| `tests/` | Automated tests |

## Current State

- Local PostgreSQL environment via Docker Compose
- Repository structure and source inventory established
- No data ingested yet

See `docs/sources/source-inventory.md` for registered sources.