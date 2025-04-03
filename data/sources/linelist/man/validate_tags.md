# Checks the tags of a linelist object

```r
validate_tags(x, allow_extra = FALSE)
```

## Arguments

- `x`: a `linelist` object
- `allow_extra`: a `logical` indicating if additional data tags not currently recognized by `linelist` should be allowed; if `FALSE`, unknown tags will trigger an error

## Returns

If checks pass, a `linelist` object; otherwise issues an error.

This function evaluates the validity of the tags of a `linelist` object by checking that: i) tags are present ii) tags is a `list` of `character` iii) that all default tags are present iv) tagged variables exist v) that no extra tag exists (if `allow_extra` is `FALSE`).

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
  validate_tags(x)

  ## hack to create an invalid tags (missing defaults)
  attr(x, "tags") <- list(id = "case_ID")

  ## the below issues an error
  ## note: tryCatch is only used to avoid a genuine error in the example
  tryCatch(validate_tags(x), error = paste)
}
```

## See Also

`validate_types()` to check if tagged variables have the right classes
