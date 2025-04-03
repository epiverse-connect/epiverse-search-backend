# Get indicator ID from domain ID

```r
fingertips_get_id_from_dm_id(
  metadata = list(indicator_profile_domain = fingertipsR::indicators(),
    indicator_ids_names = fingertipsR::indicators_unique(), area_type =
    fingertipsR::area_types()),
  domain_id = 1000041L,
  indicator_name = NULL
)
```

## Arguments

- `metadata`: a list with the fingertips metadata
- `domain_id`: the domain ID
- `indicator_name`: the indicator name

## Returns

an object of type `numeric` that contains the indicator ID.

Get indicator ID from domain ID

## Examples

```r
## Not run:

indicator_id <- fingertips_get_id_from_dm_id(
  metadata       = list(
    indicator_profile_domain = fingertipsR::indicators(),
    indicator_ids_names      = fingertipsR::indicators_unique(),
    area_type                = fingertipsR::area_types()
  ),
  domain_id      = 1000041,
  indicator_name = NULL
)
## End(Not run)
```
