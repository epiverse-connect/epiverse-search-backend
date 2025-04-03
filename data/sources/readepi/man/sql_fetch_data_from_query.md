# Fetch data from server using an SQL query

```r
sql_fetch_data_from_query(
  src,
  tables,
  base_url,
  user_name,
  password,
  dbms,
  driver_name,
  database_name,
  port
)
```

## Arguments

- `src`: the SQL query
- `tables`: the list of tables from the database
- `base_url`: the host server name
- `user_name`: the user name
- `password`: the user's password
- `dbms`: the database management system type
- `driver_name`: the driver name
- `database_name`: the database name
- `port`: the server port ID

## Returns

a `list` of 1 or more objects of type `data.frame` containing each data fetched from one table.

Fetch data from server using an SQL query

## Examples

```r
## Not run:

result <- sql_fetch_data_from_query(
  src           = "select author_id, name, last_name from author",
  tables        = c("family_author", "author"),
  base_url      = "mysql-rfam-public.ebi.ac.uk",
  user_name     = "rfamro",
  password      = "",
  dbms          = "MySQL",
  driver_name   = "",
  database_name = "Rfam",
  port          = 4497
)
## End(Not run)
```
