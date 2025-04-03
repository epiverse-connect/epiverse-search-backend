# Import data from different data_sources into R

```r
readepi(
  data_source = NULL,
  records = NULL,
  fields = NULL,
  id_position = NULL,
  id_col_name = NULL,
  ...
)
```

## Arguments

- `data_source`: the URL of the HIS
- `records`: a vector or a comma-separated string of subject IDs. When specified, only these records will be imported.
- `fields`: a vector or a comma-separated string of column names. If provided, only those columns will be imported.
- `id_position`: the column position of the variable that unique identifies the subjects. When the name of the column with the subject IDs is known, this can be provided using the `id_col_name` argument
- `id_col_name`: the column name with the subject IDs.
- `...`: additional arguments passed to the `readepi()` function. These are enumerated and described in the vignette.

## Returns

a `list` of 1 or several object(s) of type `data frame`.

a `list` of 2 or more object(s) of type `data frame`.

the function allows import of data from Health Information Systems (HIS), files, and folders.The HIS consist of database management systems (DBMS) and website of public data collection.

## Examples

```r
# reading from a MySQL server
## Not run:

data <- readepi(
  data_source      = "mysql-rfam-public.ebi.ac.uk",
  credentials_file = system.file("extdata", "test.ini", package = "readepi"),
  driver_name      = "",
  from             = "author"
)
## End(Not run)
```
