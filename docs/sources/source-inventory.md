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
| URL | https://digital.nhs.uk/data-and-information/publications/statistical/appointments-in-general-practice | Format | CSV |
| Files | Practice_Level_Crosstab_Dec_25.csv (fact), Mapping.csv (geography reference) |
| Geographic grain | GP Practice → PCN → Sub-ICB → ICB → Region (full hierarchy in Mapping.csv) |
| Key fields | APPOINTMENT_MONTH_START_DATE, GP_CODE, HCP_TYPE, APPT_MODE, NATIONAL_CATEGORY, TIME_BETWEEN_BOOK_AND_APPT, APPT_STATUS, COUNT_OF_APPOINTMENTS |
| Business key | GP_CODE + APPOINTMENT_MONTH_START_DATE + HCP_TYPE + APPT_MODE + NATIONAL_CATEGORY + TIME_BETWEEN_BOOK_AND_APPT + APPT_STATUS |
| Known quirks | Date format is 01DEC2025 — needs parsing in staging. Geography hierarchy requires join to Mapping.csv to reach ICB level for ONS join. 185MB file — largest source by volume. |
| First downloaded | 2026-03-10 |

---

## Source 2: ONS — Population Estimates for Health Geographies

| Field | Detail |
|---|---|
| Publisher | Office for National Statistics |
| Domain | Mid-year resident population estimates by ICB and sub-ICB geography |
| URL | https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/clinicalcommissioninggroupmidyearpopulationestimates |
| Format | CSV |
| Files | Practice_Level_Crosstab_Dec_25.csv (fact), Mapping.csv (geography reference) |
| Geographic grain | GP Practice → PCN → Sub-ICB → ICB → Region (full hierarchy in Mapping.csv) |
| Key fields | APPOINTMENT_MONTH_START_DATE, GP_CODE, HCP_TYPE, APPT_MODE, NATIONAL_CATEGORY, TIME_BETWEEN_BOOK_AND_APPT, APPT_STATUS, COUNT_OF_APPOINTMENTS |
| Business key | GP_CODE + APPOINTMENT_MONTH_START_DATE + HCP_TYPE + APPT_MODE + NATIONAL_CATEGORY + TIME_BETWEEN_BOOK_AND_APPT + APPT_STATUS |
| Known quirks | Date format is 01DEC2025 — needs parsing in staging. Geography hierarchy requires join to Mapping.csv to reach ICB level for ONS join. 185MB file — largest source by volume. |
| First downloaded | 2026-03-10 |

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