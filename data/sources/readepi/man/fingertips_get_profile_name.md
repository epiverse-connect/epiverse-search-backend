# Get profile name from Fingertips

```r
fingertips_get_profile_name(
  metadata = list(indicator_profile_domain = fingertipsR::indicators(),
    indicator_ids_names = fingertipsR::indicators_unique(), area_type =
    fingertipsR::area_types()),
  profile_id = 19L,
  profile_name = "Public Health Outcomes Framework"
)
```

## Arguments

- `metadata`: the Fingertips metadata
- `profile_id`: the profile ID
- `profile_name`: the profile name

## Returns

a `list` of 2 elements of type `character` and `numeric`. These are the `profile name` and their correspondent indexes.

Get profile name from Fingertips

## Examples

```r
## Not run:

  res <- fingertips_get_profile_name(
    profile_id   = 19L,
    profile_name = "Public Health Outcomes Framework",
    metadata = list(
      indicator_profile_domain = fingertipsR::indicators(),
      indicator_ids_names      = fingertipsR::indicators_unique(),
      area_type                = fingertipsR::area_types()
    )
  )
## End(Not run)
```
