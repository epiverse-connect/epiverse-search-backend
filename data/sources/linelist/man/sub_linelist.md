# Subsetting of linelist objects

```r
## S3 method for class 'linelist'
x[i, j, drop = FALSE]

## S3 replacement method for class 'linelist'
x[i, j] <- value

## S3 replacement method for class 'linelist'
x[[i, j]] <- value

## S3 replacement method for class 'linelist'
x$name <- value
```

## Arguments

- `x`: a `linelist` object
- `i`: a vector of `integer` or `logical` to subset the rows of the `linelist`
- `j`: a vector of `character`, `integer`, or `logical` to subset the columns of the `linelist`
- `drop`: a `logical` indicating if, when a single column is selected, the `data.frame` class should be dropped to return a simple vector, in which case the `linelist` class is lost as well; defaults to `FALSE`
- `value`: the replacement to be used for the entries identified in `x`
- `name`: a literal character string or a name (possibly backtick
    
    quoted). For extraction, this is normally (see under Environments ) partially matched to the `names`
    
    of the object.

## Returns

If no drop is happening, a `linelist`. Otherwise an atomic vector.

The `[]` and `[[]]` operators for `linelist` objects behaves like for regular `data.frame` or `tibble`, but check that tagged variables are not lost, and takes the appropriate action if this is the case (warning, error, or ignore, depending on the general option set via `lost_tags_action()`) .

## Examples

```r
if (require(outbreaks) && require(dplyr)) {
  ## create a linelist
  x <- measles_hagelloch_1861 |>
    make_linelist(
      id = "case_ID",
      date_onset = "date_of_prodrome",
      age = "age",
      gender = "gender"
    ) |>
    mutate(result = if_else(is.na(date_of_death), "survived", "died")) |>
    set_tags(outcome = "result") |>
    rename(identifier = case_ID)
  x

  ## dangerous removal of a tagged column setting it to NULL issues a warning
  x[, 1] <- NULL
  x

  x[[2]] <- NULL
  x

  x$age <- NULL
  x
}
```

## See Also

 * `lost_tags_action()` to set the behaviour to adopt when tags are lost through subsetting; default is to issue a warning
 * `get_lost_tags_action()` to check the current the behaviour
