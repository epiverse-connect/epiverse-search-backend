# Subset columns when reading from Fingertips

```r
fingertips_subset_columns(
  data = readepi(profile_id = 19L, area_type_id = 202L)[["data"]],
  fields = c("IndicatorID", "AreaCode", "Age", "Value")
)
```

## Arguments

- `data`: the data read from Fingertips
- `fields`: a vector or a comma-separated string of column names

## Returns

an object of type `data.frame` with the Fingertips dataset that contains only the fields of interest.

Subset columns when reading from Fingertips

## Examples

```r
## Not run:

res <- fingertips_subset_columns(
  data = readepi(
    profile_id   = 19,
    area_type_id = 6
  )$data,
  fields         = c("IndicatorID", "AreaCode", "Age", "Value")
)
## End(Not run)
```
