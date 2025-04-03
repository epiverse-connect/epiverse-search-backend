# Get arguments for reading from Fingertips

```r
fingertips_get_args(
  args_list = list(indicator_id = NULL, indicator_name = NULL, area_type_id = NULL,
    profile_id = NULL, profile_name = NULL, domain_id = NULL, domain_name = NULL,
    parent_area_type_id = NULL)
)
```

## Arguments

- `args_list`: a `list` of user specified arguments

## Returns

a `list` of 8 elements of type `character` and `numeric` that will be used for importing data from Fingertips

Get arguments for reading from Fingertips

## Examples

```r
## Not run:

  res <- fingertips_get_args(
    list(indicator_id   = 90362L,
         area_type_id   = 202L,
         indicator_name = "Healthy life expectancy at birth",
         profile_id     = 19L)
  )
## End(Not run)
```
