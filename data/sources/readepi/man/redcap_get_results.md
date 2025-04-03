# Check and return data fetch from redcap

```r
redcap_get_results(redcap_data, metadata)
```

## Arguments

- `redcap_data`: the object with redcap data
- `metadata`: the object with redcap metadata

## Returns

a `list` of 2 elements of type `data.frame`. These are the dataset of interest and its associated metadata.

Check and return data fetch from redcap

## Examples

```r
## Not run:

result <- redcap_get_results(
  redcap_data = REDCapR::redcap_read(
    redcap_uri  = "https://bbmc.ouhsc.edu/redcap/api/",
    token       = "9A81268476645C4E5F03428B8AC3AA7B",
    records     = c("1", "3", "5"),
    fields      = c("record_id", "name_first", "age", "bmi"),
    verbose     = FALSE,
    id_position = 1L
  ),
  metadata = REDCapR::redcap_metadata_read(
    redcap_uri = "https://bbmc.ouhsc.edu/redcap/api/",
    token      = "9A81268476645C4E5F03428B8AC3AA7B",
    fields     = NULL,
    verbose    = FALSE
  )
)
## End(Not run)
```
