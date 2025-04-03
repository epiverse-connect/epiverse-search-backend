# Select specified records from a table

```r
sql_select_records_only(
  table,
  base_url,
  user_name,
  password,
  dbms,
  driver_name,
  database_name,
  port = 4497L,
  record,
  id_column_name = NULL,
  id_pos = NULL
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
- `record`: a vector or a comma-separated string of subset of subject IDs.
- `id_column_name`: the column names that unique identify the records in the tables
- `id_pos`: a vector of the column positions of the variable that unique identifies the subjects in each table

## Returns

an object of type `data.frame` that contains the data fetched from the specific table with only the records of interest.

Select specified records from a table

## Examples

```r
## Not run:

result <- sql_select_records_only(
  table          = "author",
  base_url       = "mysql-rfam-public.ebi.ac.uk",
  user_name      = "rfamro",
  password       = "",
  dbms           = "MySQL",
  driver_name    = "",
  database_name  = "Rfam",
  port           = 4497,
  record         = c("1", "20", "50"),
  id_column_name = NULL,
  id_pos         = 1
)
## End(Not run)
```
