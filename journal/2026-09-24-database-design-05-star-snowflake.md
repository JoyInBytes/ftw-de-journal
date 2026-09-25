# Star and Snowflake Schemas

## Star schema

One fact table connects directly to dimension tables. It is simpler and usually needs fewer joins.

## Snowflake schema

Dimension tables are split into smaller normalized tables. It reduces repetition but requires more joins.

| Star | Snowflake |
|---|---|
| Simpler | More normalized |
| Fewer tables | More tables |
| Fewer joins | More joins |

**Key takeaway:** Star schemas prioritize simplicity and query speed; snowflake schemas prioritize reduced duplication.
