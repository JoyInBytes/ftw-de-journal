# Database Roles and Access Control

A database role is an identity that can hold permissions and login settings. Roles can represent individual users or groups.

```sql
create role data_analyst;
grant select on ratings to data_analyst;
grant data_analyst to alex;
```

Remove access with `revoke`.

Roles simplify onboarding, offboarding, and consistent permissions. Follow least privilege: give users only the access they need.
