# Database Design and Data Modeling

Database design determines how data is stored, related, queried, and updated.

- **Database model:** General rules for organizing data.
- **Schema:** Detailed blueprint of tables, columns, keys, relationships, indexes, and views.

## Modeling levels

1. Conceptual: What entities and relationships exist?
2. Logical: How do they map to tables?
3. Physical: How are they stored?

## Facts and dimensions

- **Fact:** Business events, measures, and foreign keys.
- **Dimension:** Descriptive context such as date, customer, product, or location.
- **Grain:** What one row represents.

**Key takeaway:** Identify the business process and grain before creating tables.
