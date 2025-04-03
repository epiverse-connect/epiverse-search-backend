# Display the list of tables in a database

```r
show_tables(data_source, driver_name, credentials_file = NULL)
```

## Arguments

- `data_source`: the URL of the server of interest
- `driver_name`: the name of the MS driver. use `odbc::odbcListDrivers()`
    
    to display the list of installed drivers
- `credentials_file`: the path to the file with the user-specific credential details for the projects of interest. See the help of the `readepi` function for more details.

## Returns

a `character` that contains the list of all tables found in the specified database.

Display the list of tables in a database

## Examples

```r
## Not run:

show_tables(
  data_source      = "mysql-rfam-public.ebi.ac.uk",
  credentials_file = system.file("extdata", "test.ini", package = "readepi"),
  driver_name      = ""
)
## End(Not run)
```
