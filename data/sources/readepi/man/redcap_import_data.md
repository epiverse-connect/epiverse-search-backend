# Import data from REDCap under all scenario

```r
redcap_import_data(
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
- `records`: a vector or a comma-separated string of subset of subject IDs
- `fields`: a vector or a comma-separated string of column names
- `id_position`: the column position of the variable that unique identifies the subjects
- `id_col_name`: the column name with the subject IDs

## Returns

a `list` of 2 elements of type `data.frame`. These are the dataset of interest and its associated metadata.

This is a wrapper across all the use case of reading data from REDCap i.e. around the function that all records and fields from the project, around the function that read specific records/fields or both at the same time

## Examples

```r
## Not run:

  result <- redcap_import_data(
    base_url    = file.path("https:/", "bbmc.ouhsc.edu",
                            "redcap", "api", ""),
    token       = "9A81268476645C4E5F03428B8AC3AA7B",
    records     = c("1", "3", "5"),
    fields      = c("record_id", "name_first", "age", "bmi"),
    id_position = 1L,
    id_col_name = NULL
  )
## End(Not run)
```
