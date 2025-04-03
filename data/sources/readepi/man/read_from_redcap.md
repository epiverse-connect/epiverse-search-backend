# Import data from REDCap

```r
read_from_redcap(
  base_url,
  token,
  records = NULL,
  fields = NULL,
  id_position = 1L,
  id_col_name = NULL
)
```

## Arguments

- `base_url`: the URI of the server
- `token`: the user-specific string that serves as the password for a project
- `records`: a vector or a comma-separated string of subset of subject IDs. When specified, only the records that correspond to these subjects will be imported.
- `fields`: a vector or a comma-separated string of column names. If provided, only those columns will be imported.
- `id_position`: the column position of the variable that unique identifies the subjects. When the column name with the subject IDs is known, use the `id_col_name` argument instead. default is 1
- `id_col_name`: the column name with the subject IDs

## Returns

a `list` of 2 elements of type `data.frame`. They include a data frame of the dataset of interest and its associated metadata.

Import data from REDCap

## Examples

```r
## Not run:

redcap_data <- read_from_redcap(
  base_url    = "https://bbmc.ouhsc.edu/redcap/api/",
  token       = "9A81268476645C4E5F03428B8AC3AA7B",
  records     = NULL,
  fields      = NULL,
  id_position = 1,
  id_col_name = NULL
)
## End(Not run)
```
