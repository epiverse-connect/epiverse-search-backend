# Read from Fingertips

```r
read_from_fingertips(
  indicator_id = 90362L,
  indicator_name = NULL,
  area_type_id = 202L,
  parent_area_type_id = NULL,
  profile_id = NULL,
  profile_name = NULL,
  domain_id = NULL,
  domain_name = NULL,
  fields = NULL,
  records = NULL,
  id_position = NULL,
  id_col_name = "AreaCode"
)
```

## Arguments

- `indicator_id`: a numeric vector of indicator IDs
- `indicator_name`: a vector of a comma-separated list of indicator names
- `area_type_id`: a vector of area type IDs
- `parent_area_type_id`: a vector of parent area type IDs
- `profile_id`: a vector of profile IDs
- `profile_name`: a vector or a comma-separated list of profile names
- `domain_id`: a vector of domain IDs
- `domain_name`: a vector or a comma-separated list of domain names
- `fields`: a vector or a comma-separated string of column names. If provided, only those columns will be imported.
- `records`: a vector or a comma-separated string of records. When specified, only these records will be imported.
- `id_position`: the column position of the variable that unique identifies the subjects. When the name of the column with the subject IDs is known, this can be provided using the `id_col_name` argument
- `id_col_name`: the column name with the subject IDs.

## Returns

a `list` of 1 element of type `data.frame`. This contains the imported dataset of interest.

Read from Fingertips

## Examples

```r
## Not run:

  data <- read_from_fingertips(indicator_id = 90362, area_type_id = 6)
## End(Not run)
```
