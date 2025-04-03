# Get indicator ID from indicator name

```r
fingertips_get_id_from_name(
  metadata = list(indicator_profile_domain = fingertipsR::indicators(),
    indicator_ids_names = fingertipsR::indicators_unique(), area_type =
    fingertipsR::area_types()),
  indicator_name = "Pupil absence"
)
```

## Arguments

- `metadata`: a list with the fingertips metadata
- `indicator_name`: the indicator name

## Returns

an object of type `numeric` that contains the indicator ID.

Get indicator ID from indicator name

## Examples

```r
## Not run:

indicator_id <- fingertips_get_id_from_name(
  metadata       = list(
    indicator_profile_domain = fingertipsR::indicators(),
    indicator_ids_names      = fingertipsR::indicators_unique(),
    area_type                = fingertipsR::area_types()
  ),
  indicator_name = "Pupil absence"
)
## End(Not run)
```
