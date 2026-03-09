# Source Inventory

Last updated: 2026-03-09

## Purpose
This document registers all external data sources ingested by the UK Health Data Platform.
It is the authoritative reference for source identity, location, format, cadence, and known quality characteristics.

---

## Source 1: NHS England Operational Statistics

| Field | Detail |
|---|---|
| Publisher | NHS England |
| Domain | Primary care, appointments, workforce |
| URL | https://www.england.nhs.uk/statistics/statistical-work-areas/ |
| Format | CSV / XLSX |
| Cadence | Monthly |
| Typical lag | ~6 weeks after reference month |
| Business key | TBD — to be confirmed on first file inspection |
| Known quirks | None documented yet |
| First downloaded | Not yet |

---

## Source 2: ONS Population and Geography Reference Data

| Field | Detail |
|---|---|
| Publisher | Office for National Statistics |
| Domain | Population estimates, geography lookups |
| URL | https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration |
| Format | CSV |
| Cadence | Annual (some reference files static) |
| Typical lag | ~12 months after reference year |
| Business key | TBD |
| Known quirks | None documented yet |
| First downloaded | Not yet |

---

## Source 3: OHID / Fingertips Indicators

| Field | Detail |
|---|---|
| Publisher | Office for Health Inequalities and Disparities |
| Domain | Public health indicators by geography |
| URL | https://fingertips.phe.org.uk |
| Format | CSV / API |
| Cadence | Varies by indicator |
| Typical lag | Varies |
| Business key | TBD |
| Known quirks | None documented yet |
| First downloaded | Not yet |

---

## Notes
- All raw source files are stored locally under `data/raw/` and are not committed to version control.
- Source provenance (download date, URL, file hash) will be recorded per-file once ingestion begins in Week 2.