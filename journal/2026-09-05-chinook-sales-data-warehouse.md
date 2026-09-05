# Project - Chinook Sales Data Warehouse

- **Snapshot:** 2026-09-05
- **Status:** Complete
- **Repository or demo:** [Team repository](https://github.com/ItsYangCoder/d3-chinook-dimensional-model)

## In one sentence

A team-built Databricks data warehouse that transforms Chinook music-store data into clean, validated, analytics-ready tables for sales reporting.

## What I built

- Contributed to a Medallion pipeline with Raw, Clean, and Mart layers.
- Helped organize the Git and GitHub workflow for branches, commits, pull requests, and team review.
- Worked with a star schema containing `fact_sales`, `dim_customer`, `dim_date`, `dim_track`, and `dim_employee`.
- Created and presented a Tableau sales dashboard supported by Gold-layer data.
- Prepared simple business answers for revenue, customers, music performance, time trends, and employee performance.
- Reviewed the CI/CD setup using GitHub Actions and Databricks Declarative Automation Bundles.

## Tools and skills

- Databricks SQL, Delta Lake, Unity Catalog, dimensional modeling, Tableau, Git, GitHub, GitHub Actions, and Databricks Bundles.

## What I learned

- A fact table stores measurable events, while dimensions provide the descriptive context for analysis.
- The grain of `fact_sales` is one purchased track per invoice line.
- Data validation is required before Gold-layer tables are used in a dashboard.
- Git branches and pull requests help teammates review changes safely before merging.
- Declarative CI/CD defines the desired deployment in configuration, while imperative CI/CD lists the commands to execute step by step.

## One small next step

- [ ] Add final dashboard screenshots and verified KPI results when the published Tableau views are available.

## Evidence

- [Star schema and technical README](https://github.com/ItsYangCoder/d3-chinook-dimensional-model#dimensional-model)
- [Raw, Clean, Mart, and Analytics SQL](https://github.com/ItsYangCoder/d3-chinook-dimensional-model/tree/main/src/sql)
- [Data-quality validation queries](https://github.com/ItsYangCoder/d3-chinook-dimensional-model/tree/main/tests)
- [GitHub Actions workflows](https://github.com/ItsYangCoder/d3-chinook-dimensional-model/tree/main/.github/workflows)
