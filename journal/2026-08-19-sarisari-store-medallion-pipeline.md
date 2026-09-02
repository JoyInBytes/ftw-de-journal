# Project - Sari-Sari Store Medallion Pipeline

- **Snapshot:** 2026-08-19
- **Status:** In progress
- **Source:** Private GitHub repository

## In one sentence

A Databricks SQL pipeline that turns raw sari-sari store transactions into clean, validated, and incrementally loaded datasets using the Medallion Architecture.

## What I built

- Bronze ingestion that preserves the original source values.
- Data quality checks for missing, invalid, inconsistent, and duplicate records.
- Modular Silver stages for cleaning, safe recovery, deduplication, validation, and unresolved-record handling.
- An incremental Delta Lake merge into a reusable Silver master table.

## Tools and skills

- Databricks SQL, Delta Lake, Unity Catalog, ETL/ELT, data quality, Git, and GitHub.

## What I learned

- Raw data should stay traceable before transformation.
- A repeated transaction ID is not always an exact duplicate.
- Recovery rules should be deterministic, explainable, and repeatable.
- Incremental loads should be idempotent.

## One small next step

- [ ] Complete the Gold model, final validation, dashboard queries, and reporting layer.

## Evidence

- Pipeline work is complete through Bronze, Silver validation, and incremental integration.
- Source documentation records cleaning assumptions and pipeline decisions.
