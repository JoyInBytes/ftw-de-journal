# Journal - 2026-09-08 - Unity Catalog

## Table of Contents

1. [💡 The Everyday Life Analogy](#-the-everyday-life-analogy)
2. [🚀 The Core Purpose](#-the-core-purpose-in-1-sentence)
3. [🛠️ How It Works](#️-how-it-works-3-step-by-step-bullets)
4. [🆚 Before vs. After](#-before-vs-after-table)
5. [🎓 Practice Exam Questions](#-2-practice-exam-questions)

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

## 5. 🎓 2 PRACTICE EXAM QUESTIONS

### Question 1

What is the primary purpose of Unity Catalog?

A. To train machine learning models automatically  
B. To provide centralized governance for data and AI assets  
C. To replace Apache Spark  
D. To create visualizations only  

### Question 2

Which command is used to give a group permission to read a table?

A.
```sql
GRANT SELECT ON TABLE catalog.schema.table TO `analysts`;
```

B.
```sql
DROP TABLE catalog.schema.table;
```

C.
```sql
START MODEL catalog.schema.table;
```

D.
```sql
CREATE CLUSTER analysts;
```

### Answers and Why They Are Correct

1. **B.** Unity Catalog provides centralized governance, access control, discovery, lineage, and auditing.
2. **A.** `GRANT SELECT` gives the `analysts` group permission to read the table.

## My key takeaway

Unity Catalog is the governance layer of the lakehouse. It helps teams use the right data with the right access.
