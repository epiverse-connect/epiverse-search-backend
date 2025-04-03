# Select specified fields from a table

```r
sql_select_fields_only(
  table,
  base_url,
  user_name,
  password,
  dbms,
  driver_name,
  database_name,
  port,
  field
)
```

## Arguments

- `table`: the table name
- `base_url`: the host server name
- `user_name`: the user name
- `password`: the user's password
- `dbms`: the database management system type
- `driver_name`: the driver name
- `database_name`: the database name
- `port`: the server port ID
- `field`: a vector of column names of interest

## Returns

an object of type `data.frame` that contains the data fetched from the specific table with only the fields of interest.

Select specified fields from a table

## Examples

```r
## Not run:

result <- sql_select_fields_only(
  table         = "author",
  base_url      = "mysql-rfam-public.ebi.ac.uk",
  user_name     = "rfamro",
  password      = "",
  dbms          = "MySQL",
  driver_name   = "",
  database_name = "Rfam",
  port          = 4497,
  field         = c("author_id", "name", "last_name")
)
## End(Not run)
```
