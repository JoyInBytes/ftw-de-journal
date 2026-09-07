# Journal - 2026-09-08 - Databricks Review and Practice Test

## Lesson summary

- SQL examples help Genie follow exact business formulas.
- Monitoring helps identify failed or unclear user questions.
- Synonyms, table relationships, and SQL examples improve response accuracy.
- Trusted Assets show that a calculation was reviewed and approved.
- Benchmarks help measure whether curation changes improve the Genie space.

## Practice questions and answers

### 1. Why is a SQL example important for Top-Rated Destination?

**Answer:** It has a specific business formula that Genie may interpret differently without guidance.

**Key idea:** A SQL example keeps complex calculations consistent.

### 2. Which question benefits most from a SQL example?

**Answer:** What is the guest retention rate for each destination?

**Key idea:** Custom formulas such as retention rate need a clear SQL example.

### 3. Why should the Monitoring page be reviewed regularly?

**Answer:** It shows patterns in failed questions and helps identify what needs improvement.

**Key idea:** Monitoring reveals where users get stuck.

### 4. What is the correct feedback loop?

1. **Review:** Check unanswered or thumbs-down questions.
2. **Diagnose:** Find the cause, such as a missing synonym, broken relationship, or complex logic.
3. **Curate:** Apply the correct fix.
4. **Verify:** Run the question again and confirm the fix.

**Key idea:** Review → Diagnose → Curate → Verify.

### 5. What does an empty SQL field usually mean?

**Answer:** Genie does not recognize “nodes” as another term for franchise locations, so a synonym is needed.

**Key idea:** Blank SQL often means Genie cannot connect a business term to a table or column.

### 6. What does the Trusted badge mean?

**Answer:** The result came from a verified, human-approved query.

**Key idea:** The calculation was reviewed instead of relying only on AI interpretation.

### 7. How is a Trusted Asset different from a regular SQL example?

**Answer:** A Trusted Asset displays a **Trusted** badge to show that the calculation is officially approved.

**Key idea:** It gives users confidence in important business results.

### 8. How should benchmark results be used?

**Answer:** Review failed questions, fix the curation gaps, and run the benchmark again.

**Key idea:** Reusing the same test questions measures improvement.

### 9. What is the correct priority for curation tasks?

1. Create a Trusted Asset for quarterly revenue in Australia used in board reports.
2. Add synonyms for franchise, store, and shop terminology with 50 or more failed questions each week.
3. Define the relationship between `salessuppliers` and `salestransactions` with 10 failed questions each week.
4. Add a SQL example for a legacy inventory metric used once a month.

**Key idea:** Protect executive reporting first, then fix the most frequent user problems.

### 10. What should be prioritized first based on the benchmark?

**Answer:** Add synonyms for unrecognized business terms because terminology gaps cause most failures.

**Key idea:** Fix the issue that affects the largest number of questions.

## My key takeaway

A high-quality Genie space needs regular human review. Clear SQL examples, synonyms, relationships, Trusted Assets, and benchmarks help keep answers accurate and reliable.

## What I practiced

- Identifying when a SQL example is needed.
- Using Monitoring results to diagnose failures.
- Prioritizing curation tasks based on business importance and failure volume.
- Understanding the purpose of Trusted Assets and benchmarks.

## One small next step

- [ ] Review more Genie practice questions and explain why each answer is correct.

## Git checkpoint

- [x] I created or updated a file
- [x] I wrote a commit
- [x] I pushed my changes
