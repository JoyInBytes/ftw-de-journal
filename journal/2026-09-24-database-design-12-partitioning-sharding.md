# Partitioning and Sharding

Partitioning divides a large table into smaller physical parts while keeping the same logical table.

- **Vertical partitioning:** Split by columns.
- **Horizontal partitioning:** Split by rows, often by date or quarter.

Benefits include scanning less data, improving query speed, and keeping indexes smaller.

**Sharding** distributes table partitions across multiple machines.

**Key takeaway:** Partitioning divides storage; sharding also distributes data across servers.
