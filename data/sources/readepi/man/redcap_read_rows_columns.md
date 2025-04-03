# Subset records and columns from a REDCap project

```r
redcap_read_rows_columns(
  base_url,
  token,
  fields = NULL,
  records = NULL,
  id_position = 1L,
  id_col_name = NULL
)
```

## Arguments

- `base_url`: the URI of the REDCap project
- `token`: the user-specific string that serves as the password for a project
- `fields`: a vector or a comma-separated string of column names
- `records`: a vector or a comma-separated string of subset of subject IDs
- `id_position`: the column position of the variable that unique identifies the subjects
- `id_col_name`: the column name with the subject IDs

## Returns

a `list` of 2 elements of type `data.frame` that contain the project data with only the records and fields of interest and its associated metadata.

Subset records and columns from a REDCap project

## Examples

```r
## Not run:

  result <- redcap_read_rows_columns(
    base_url    = "https://bbmc.ouhsc.edu/redcap/api/",
    token       = "9A81268476645C4E5F03428B8AC3AA7B",
    fields      = c("record_id", "name_first", "age", "bmi"),
    records     = c("1", "3", "5"),
    id_position = 1L,
    id_col_name = NULL
  )
## End(Not run)
```
