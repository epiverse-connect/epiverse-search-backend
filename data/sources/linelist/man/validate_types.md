# Check tagged variables are the right class

```r
validate_types(x, ref_types = tags_types())
```

## Arguments

- `x`: a `linelist` object
- `ref_types`: a `list` providing allowed types for all tags, as returned by `tags_types()`

## Returns

A named `list`.

This function checks the class of each tagged variable in a `linelist`

against pre-defined accepted classes in `tags_types()`.

## Examples

```r
if (require(outbreaks)) {

  ## create an invalid linelist - gender is a numeric
  x <- measles_hagelloch_1861 |>
    make_linelist(
      id = "case_ID",
      gender = "infector"
    )
  x

  ## the below would issue an error
  ## note: tryCatch is only used to avoid a genuine error in the example
  tryCatch(validate_types(x), error = paste)

  ## to allow other types, e.g. gender to be integer, character or factor
  validate_types(x, tags_types(gender = c("integer", "character", "factor")))
}
```

## See Also

 * `tags_types()` to change allowed types
 * `validate_tags()` to perform a series of checks on the tags
 * `validate_linelist()` to combine `validate_tags` and `validate_types`
