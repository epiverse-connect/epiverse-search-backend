# Visualize the first 5 rows of the data from a table

```r
visualise_table(data_source, credentials_file, from, driver_name)
```

## Arguments

- `data_source`: the the URL of the HIS
- `credentials_file`: the path to the file with the user-specific credential details for the projects of interest
- `from`: the table name
- `driver_name`: the name of the MS driver

## Returns

prints the first 5 rows of the specified table.

Visualize the first 5 rows of the data from a table

## Examples

```r
## Not run:

  result <- visualise_table(
    data_source      = "mysql-rfam-public.ebi.ac.uk",
    credentials_file = system.file("extdata", "test.ini",
                                   package = "readepi"),
    from             = "author",
    driver_name      = ""
  )
## End(Not run)
```
