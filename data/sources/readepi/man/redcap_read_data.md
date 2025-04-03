# Read all rows and columns from redcap

```r
redcap_read_data(base_url, token, id_position = 1L)
```

## Arguments

- `base_url`: the URI of the REDCap project
- `token`: the user-specific string that serves as the password for a project
- `id_position`: the column position of the variable that unique identifies the subjects

## Returns

a `list` of 2 elements of type `data.frame` that contain the project data and its associated metadata.

Read all rows and columns from redcap

## Examples

```r
## Not run:

  result <- redcap_read_data(
    base_url    = "https://bbmc.ouhsc.edu/redcap/api/",
    token       = "9A81268476645C4E5F03428B8AC3AA7B",
    id_position = 1L
  )
## End(Not run)
```
