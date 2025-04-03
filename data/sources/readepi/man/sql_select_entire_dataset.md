# Fetch entire dataset in a table

```r
sql_select_entire_dataset(
  table,
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

- `table`: the table name
- `base_url`: host server name
- `user_name`: the user name
- `password`: the user's password
- `dbms`: the database management system type
- `driver_name`: the driver name
- `database_name`: the database name
- `port`: the server port ID

## Returns

an object of type `data.frame` with the entire dataset fetched from the specified table.

Fetch entire dataset in a table

## Examples

```r
## Not run:

result <- sql_select_entire_dataset(
  table         = "author",
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
