# Source Inventory

Last updated: 2026-03-10

## Purpose
This document registers all external data sources ingested by the UK Health Data Platform.

The platform exists to give analysts clean, validated, reconciled inputs for assessing 
whether primary care access is keeping pace with population growth and demographic pressure 
across English geographies. Every source registered here serves that analytical purpose 
directly.

This document is the authoritative reference for source identity, location, format, 
cadence, and known quality characteristics. It is the contract that ingestion and 
validation logic will eventually enforce.

## Source 1: NHS England — Appointments in General Practice

| Field | Detail |
|---|---|
| Publisher | NHS England (digital.nhs.uk) |
| Domain | GP appointment activity by practice, PCN, and ICB |
| URL | https://digital.nhs.uk/data-and-information/publications/statistical/appointments-in-general-practice |
| Format | CSV (practice-level summary + daily counts) |
| Cadence | Monthly |
| Typical lag | ~6 weeks after reference month |
| Geographic grain | GP Practice → PCN → ICB sub-location → ICB → NHS Region |
| Key fields | appointment counts, attendance status, HCP type, mode, booking lead time |
| Business key | TBD — to be confirmed on first file inspection (likely PRACTICE_CODE + appointment_month) |
| Known quirks | Coverage is ~99% of practices, not 100%. COVID vaccination activity removed from Dec 2020 onwards. HCP Type being phased out in favour of SDS Role Groups. Schema has changed over time. |
| First downloaded | Not yet |

---

## Source 2: ONS — Population Estimates for Health Geographies

| Field | Detail |
|---|---|
| Publisher | Office for National Statistics |
| Domain | Mid-year resident population estimates by ICB and sub-ICB geography |
| URL | https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/clinicalcommissioninggroupmidyearpopulationestimates |
| Format | CSV / Excel (zipped) |
| Cadence | Annual (mid-year, published ~12 months after reference date) |
| Geographic grain | ICB (formerly CCG) — aligns to NHS appointment geography |
| Key fields | population estimates by age band and sex, ICB code |
| Business key | TBD — likely ICB code + reference year |
| Known quirks | Geography codes change on 1 April each year as NHS restructures. CCG → ICB transition in 2022 means historical files use different codes. Must handle code mapping carefully. |
| First downloaded | Not yet |

---

## Source 3: OHID / Fingertips — GP Access and Deprivation Indicators

| Field | Detail |
|---|---|
| Publisher | Office for Health Inequalities and Disparities |
| Domain | Primary care access and deprivation indicators by ICB and GP practice |
| URL | https://fingertips.phe.org.uk |
| Format | CSV (bulk download) / REST API |
| Cadence | Varies by indicator — some annual, some quarterly |
| Geographic grain | GP Practice, PCN, ICB sub-location, ICB |
| Key fields | indicator ID, area code, area type, value, time period |
| Business key | TBD — likely indicator_id + area_code + time_period |
| Known quirks | Indicator definitions change over time. Not all indicators available at all geographic levels. API rate limits apply for bulk pulls. |
| First downloaded | Not yet |