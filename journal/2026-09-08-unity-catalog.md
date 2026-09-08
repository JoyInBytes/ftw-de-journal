# Journal - 2026-09-08 - Unity Catalog

## Table of Contents

1. [💡 The Everyday Life Analogy](#1--the-everyday-life-analogy)
2. [🚀 The Core Purpose](#2--the-core-purpose-in-1-sentence)
3. [🛠️ How It Works](#3-️-how-it-works-3-step-by-step-bullets)
4. [🆚 Before vs. After](#4--before-vs-after-table)
5. [📘 Key Terms and Definitions](#5--key-terms-and-definitions)
6. [My Key Takeaway](#my-key-takeaway)
7. [References](#references)

## 1. 💡 THE "EVERYDAY LIFE" ANALOGY

Imagine a library with many branches.

The catalog tells you what books exist and where they are.

The librarian decides who can read, borrow, or manage each book.

Unity Catalog works like a central catalog and librarian for data and AI assets.

## 2. 🚀 THE CORE PURPOSE (IN 1 SENTENCE)

**Companies use Unity Catalog to centrally discover, govern, secure, and track access to their data and AI assets.**

## 3. 🛠️ HOW IT WORKS (3 STEP-BY-STEP BULLETS)

- **1. Organize:** Register data using catalogs, schemas, tables, views, and volumes.
- **2. Control:** Use permissions such as `GRANT` and `REVOKE` to control access.
- **3. Track:** Use lineage, auditing, and discovery to understand how assets are used.

## 4. 🆚 BEFORE VS. AFTER TABLE

| Old, hard way without Unity Catalog | New, easy way with Unity Catalog |
|---|---|
| Permissions are managed in many separate places. | Manage governance centrally. |
| Users may not know which dataset is approved. | Discover trusted data assets in one place. |
| It is difficult to trace data movement. | View lineage between data assets. |
| Access reviews take more manual work. | Use centralized permissions and audit information. |

## 5. 📘 KEY TERMS AND DEFINITIONS

### 1. Unity Catalog
The central governance layer for data and AI assets in Databricks.

### 2. Metastore
The top-level container for Unity Catalog metadata and governed objects.

### 3. Catalog
A container that groups schemas, such as a catalog for a business team.

### 4. Schema
A container inside a catalog that groups tables, views, and other objects.

### 5. Three-level namespace
An object's full name: `catalog.schema.object`. Example: `workspace.d3_mart.fact_sales`.

### 6. Table
Data organized into rows and columns, such as sales records.

### 7. View
A saved query that presents data from underlying tables.

### 8. Volume
A governed storage object for files, such as CSVs, images, and PDFs.

### 9. Managed table
A table whose governance and underlying storage lifecycle are managed by Unity Catalog.

### 10. External table
A table governed by Unity Catalog whose underlying file lifecycle is managed separately.

### 11. Data lineage
A record of how data flows between assets. It helps trace a report back to its sources.

### 12. Audit logs
Activity records that help review who performed an action and when.

### 13. Principal
A user, group, or service principal that can receive permissions. Example: the `analysts` group.

### 14. Privilege
Permission to perform an action. Reading a table requires `SELECT`, plus `USE CATALOG` and `USE SCHEMA` on its parents.

### 15. GRANT and REVOKE
SQL commands that assign or remove privileges. Removing one grant does not remove access provided through other grants or groups.

### Practical example: give a group read access

Run these commands as an owner or another principal authorized to grant the privileges. The catalog, schema, table, and group must already exist.

```sql
GRANT USE CATALOG ON CATALOG workspace TO `analysts`;
GRANT USE SCHEMA ON SCHEMA workspace.d3_mart TO `analysts`;
GRANT SELECT ON TABLE workspace.d3_mart.fact_sales TO `analysts`;
```

**Meaning:** The group can use the parent catalog and schema, then read the specified table.

## My key takeaway

Unity Catalog is the governance layer of the lakehouse. It helps teams use the right data with the right access.

## References

- [Databricks: What is Unity Catalog?](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)
- [Databricks: Unity Catalog privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference)
