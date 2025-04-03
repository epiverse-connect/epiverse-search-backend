# Checks the content of a linelist object

```r
validate_linelist(x, allow_extra = FALSE, ref_types = tags_types())
```

## Arguments

- `x`: a `linelist` object
- `allow_extra`: a `logical` indicating if additional data tags not currently recognized by `linelist` should be allowed; if `FALSE`, unknown tags will trigger an error
- `ref_types`: a `list` providing allowed types for all tags, as returned by `tags_types()`

## Returns

If checks pass, a `linelist` object (invisibly); otherwise issues an error.

This function evaluates the validity of a `linelist` object by checking the object class, its tags, and the types of the tagged variables. It combines validations checks made by `validate_types()` and `validate_tags()`. See 'Details' section for more information on the checks performed.

## Details

The following checks are performed:

 * `x` is a `linelist` object
 * `x` has a well-formed `tags` attribute
 * all default tags are present (even if `NULL`)
 * all tagged variables correspond to existing columns
 * all tagged variables have an acceptable class
 * (optional) `x` has no extra tag beyond the default tags

## Examples

```r
if (require(outbreaks)) {

  ## create a valid linelist
  x <- measles_hagelloch_1861 |>
    make_linelist(
      id = "case_ID",
      date_onset = "date_of_prodrome",
      age = "age",
      gender = "gender"
    )
  x

  ## validation
  validate_linelist(x)

  ## create an invalid linelist - onset date is a factor
  x <- measles_hagelloch_1861 |>
    make_linelist(
      id = "case_ID",
      date_onset = "gender",
      age = "age"
    )
  x

  ## the below issues an error
  ## note: tryCatch is only used to avoid a genuine error in the example
  tryCatch(validate_linelist(x), error = paste)
}
```

## See Also

 * `tags_types()` to change allowed types
 * `validate_types()` to check if tagged variables have the right classes
 * `validate_tags()` to perform a series of checks on the tags
