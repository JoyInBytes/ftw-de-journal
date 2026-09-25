# Advanced Views and Access Control

Views can contain joins, filters, calculations, and aggregations, but complex queries may take longer to run.

Use `grant` to give access and `revoke` to remove it:

```sql
grant select on view_name to role_name;
revoke select on view_name from role_name;
```

Some simple views can be updated, but changes affect the underlying table. Views are commonly used for read-only reporting and analysis.

**Key takeaway:** Views simplify access, but permissions and update behavior must be understood.
