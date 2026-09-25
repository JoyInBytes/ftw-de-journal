# Views

A view is a saved SQL query presented as a virtual table. A regular view usually stores the query definition, not a separate copy of the data.

```sql
create view scifi_books as
select book_title, author
from books
where genre = 'Science Fiction';
```

Query it like a table:

```sql
select * from scifi_books;
```

Views reuse common queries, simplify joins, and can hide sensitive columns.
