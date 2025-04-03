# Subset fields from a REDCap project

```r
redcap_read_fields(base_url, token, fields, id_position = 1L)
```

## Arguments

- `base_url`: the URI of the REDCap project
- `token`: the user-specific string that serves as the password for a project
- `fields`: a vector or a comma-separated string of column names
- `id_position`: the column position of the variable that unique identifies the subjects

## Returns

a `list` of 2 elements of type `data.frame` that contain the project data with the fields of interest and its associated metadata.

Subset fields from a REDCap project

## Examples

```r
## Not run:

  result <- redcap_read_fields(
    base_url    = "https://bbmc.ouhsc.edu/redcap/api/",
    token       = "9A81268476645C4E5F03428B8AC3AA7B",
    fields      = c("record_id", "name_first", "age", "bmi"),
    id_position = 1L
  )
## End(Not run)
```
