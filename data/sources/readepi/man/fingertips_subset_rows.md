# Subset records when reading from Fingertips

```r
fingertips_subset_rows(data, records, id_col_name = "AreaCode")
```

## Arguments

- `data`: the data read from Fingertips
- `records`: a vector or a comma-separated string of records
- `id_col_name`: the column name with the subject IDs

## Returns

an object of type `data.frame` with the Fingertips dataset that contains only the records of interest.

Subset records when reading from Fingertips

## Examples

```r
## Not run:

res <- fingertips_subset_rows(
  data = readepi(
    profile_id   = 19,
    area_type_id = 6
  )$data,
  records        = c("E92000001", "E12000002", "E12000009"),
  id_col_name    = "AreaCode"
)
## End(Not run)
```
