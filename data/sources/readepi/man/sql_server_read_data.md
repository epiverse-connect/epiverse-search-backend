# Read data from database management systems (DBMS).

```r
sql_server_read_data(
  base_url,
  user_name,
  password,
  dbms,
  driver_name,
  database_name,
  port,
  src = NULL,
  records = NULL,
  fields = NULL,
  id_position = NULL,
  id_col_name = NULL
)
```

## Arguments

- `base_url`: the name of the host server
- `user_name`: the user name
- `password`: the user password
- `dbms`: the SQL server type
- `driver_name`: the name of the MS driver. Use `odbc::odbcListDrivers()`
    
    to display the list of installed drivers
- `database_name`: the name of the database that contains the table from which the data should be pulled
- `port`: the port ID
- `src`: an SQL query or a vector of table names from the project or database. When this is not specified, the function will extract data from all tables in the database.
- `records`: a vector or a comma-separated string of subset of subject IDs. When specified, only the records that correspond to these subjects will be imported.
- `fields`: a vector of strings where each string is a comma-separated list of column names. The element of this vector should be a list of column names from the first table specified in the `table_names` argument and so on...
- `id_position`: a vector of the column positions of the variable that unique identifies the subjects in each table. When the column name with the subject IDs is known, use the `id_col_name` argument instead. default is 1.
- `id_col_name`: the column name with the subject IDs

## Returns

a `list` of 1 or several objects of type `data.frame`. The number of elements in the list depends on the number of tables from which the data is fetched.

The function assumes the user has read access to the database. Importing data stored in DBMS into R requires the installation of the appropriate `driver` that is compatible with the server version hosting the database. See the `vignette` for how to install the driver

## Examples

```r
## Not run:

data <- sql_server_read_data(
  base_url      = "mysql-rfam-public.ebi.ac.uk",
  user_name     = "rfamro",
  password      = "",
  dbms          = "MySQL",
  driver_name   = "",
  database_name = "Rfam",
  port          = 4497,
  src           = "author",
  records       = NULL,
  fields        = NULL,
  id_position   = NULL,
  id_col_name   = NULL
)
## End(Not run)
```
