# Get indicator ID from profile ID and/or profile name

```r
fingertips_get_id_from_profile(
  metadata = list(indicator_profile_domain = fingertipsR::indicators(),
    indicator_ids_names = fingertipsR::indicators_unique(), area_type =
    fingertipsR::area_types()),
  domain_id = NULL,
  domain_name = NULL,
  indicator_name = NULL,
  profile_name = NULL,
  profile_id = 19L
)
```

## Arguments

- `metadata`: a list with the fingertips metadata
- `domain_id`: the domain ID
- `domain_name`: the domain name
- `indicator_name`: the indicator name
- `profile_name`: the profile name
- `profile_id`: the profile ID

## Returns

an object of type `numeric` that contains the indicator ID.

Get indicator ID from profile ID and/or profile name

## Examples

```r
## Not run:

res <- fingertips_get_id_from_profile(
  metadata   = list(
    indicator_profile_domain = fingertipsR::indicators(),
    indicator_ids_names      = fingertipsR::indicators_unique(),
    area_type                = fingertipsR::area_types()
  ),
  profile_id = 19
)
## End(Not run)
```
