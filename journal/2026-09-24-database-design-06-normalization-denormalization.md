# Normalization and Denormalization

## Normalization

Divide data into smaller related tables to reduce repetition and improve consistency.

## Denormalization

Combine information into wider tables to reduce joins and speed up reading.

- Write-heavy OLTP systems commonly prefer normalization.
- Read-heavy OLAP systems commonly use denormalization.

**Key takeaway:** Normalize for data quality; denormalize when faster reads are the priority.
