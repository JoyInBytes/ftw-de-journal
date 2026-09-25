# Materialized Views

A materialized view stores the result of a query on disk.

- Regular view: runs the query when accessed.
- Materialized view: reads a stored result.

Use materialized views for expensive queries that are run repeatedly. They provide faster reads, but the data may be outdated.

```sql
refresh materialized view view_name;
```

If views depend on one another, refresh upstream views first.

**Key takeaway:** Materialized views trade real-time freshness for faster query results.
