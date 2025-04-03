# Subset data read from servers

```r
sql_select_data(
  table_names,
  base_url,
  user_name,
  password,
  dbms,
  driver_name,
  database_name,
  port,
  id_col_name,
  fields = NULL,
  records = NULL,
  id_position = NULL
)
```

## Arguments

- `table_names`: the name of the tables where the data was fetched from
- `base_url`: the host server name
- `user_name`: the user name
- `password`: the user's password
- `dbms`: the database management system type
- `driver_name`: the driver name
- `database_name`: the database name
- `port`: the server port ID
- `id_col_name`: the column names that unique identify the records in the tables
- `fields`: a vector of strings where each string is a comma-separated list of column names.
- `records`: a vector or a comma-separated string of subset of subject IDs.
- `id_position`: a vector of the column positions of the variable that unique identifies the subjects in each table

## Returns

a `list` of 1 or more elements of type `data.frame` where every element contains the subset of the data from the corresponding table.

Subset data read from servers

## Examples

```r
## Not run:

result <- sql_select_data(
  table_names   = "author",
  base_url      = "mysql-rfam-public.ebi.ac.uk",
  user_name     = "rfamro",
  password      = "",
  dbms          = "MySQL",
  driver_name   = "",
  database_name = "Rfam",
  port          = 4497,
  id_col_name   = "author_id",
  fields        = c("author_id", "name"),
  records       = NULL,
  id_position   = NULL
)
## End(Not run)
```
