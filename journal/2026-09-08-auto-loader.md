# Journal - 2026-09-08 - Auto Loader

## Table of Contents

1. [💡 The Everyday Life Analogy](#-the-everyday-life-analogy)
2. [🚀 The Core Purpose](#-the-core-purpose-in-1-sentence)
3. [🛠️ How It Works](#️-how-it-works-3-step-by-step-bullets)
4. [🆚 Before vs. After](#-before-vs-after-table)
5. [🎓 Practice Exam Questions](#-2-practice-exam-questions)

## 1. 💡 THE "EVERYDAY LIFE" ANALOGY

Imagine a supermarket receiving deliveries every day.

Without Auto Loader, a worker must check every box again and remember which boxes were already processed.

With Auto Loader, a smart receiving system notices only the new boxes and records what has already arrived.

## 2. 🚀 THE CORE PURPOSE (IN 1 SENTENCE)

**Companies use Auto Loader to ingest only new files from cloud storage efficiently and incrementally.**

## 3. 🛠️ HOW IT WORKS (3 STEP-BY-STEP BULLETS)

- **1. Watch:** Auto Loader monitors a cloud storage location for new files.
- **2. Ingest:** It reads only the files that have not been processed yet.
- **3. Store:** It writes the new data into a Delta table for downstream use.

## 4. 🆚 BEFORE VS. AFTER TABLE

| Old, hard way without Auto Loader | New, easy way with Auto Loader |
|---|---|
| Recheck the whole folder repeatedly. | Track and process only new files. |
| Manually remember which files were loaded. | Use checkpoint information to track progress. |
| More scanning and slower ingestion. | Efficient incremental ingestion. |
| More risk of duplicate processing. | Safer and more reliable file processing. |

## 5. 🎓 2 PRACTICE EXAM QUESTIONS

### Question 1

A company receives new JSON files continuously in cloud storage. Which Databricks feature is most appropriate for processing only newly arrived files?

A. Model Registry  
B. Auto Loader  
C. SQL Dashboard  
D. Unity Catalog  

### Question 2

Which option correctly starts Auto Loader for JSON files?

A.
```python
spark.read.format("json").load(path)
```

B.
```python
spark.readStream.format("cloudFiles") \
    .option("cloudFiles.format", "json") \
    .load(path)
```

C.
```python
spark.read.format("postgresql").load(path)
```

D.
```python
spark.sql("SELECT * FROM cloudFiles")
```

### Answers and Why They Are Correct

1. **B — Auto Loader.** It incrementally detects and processes new files in cloud storage.
2. **B.** The `cloudFiles` format tells Databricks to use Auto Loader, and `readStream` supports continuous ingestion.

## My key takeaway

Auto Loader is useful when files arrive over time. It helps the pipeline find new data without repeatedly processing old files.
