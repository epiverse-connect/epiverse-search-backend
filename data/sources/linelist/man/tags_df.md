# Extract a data.frame of all tagged variables

```r
tags_df(x)
```

## Arguments

- `x`: a `linelist` object

## Returns

A `data.frame` of tagged variables.

This function returns a `data.frame` of all the tagged variables stored in a `linelist`. Note that the output is no longer a `linelist`, but a regular `data.frame`.

## Examples

```r
if (require(outbreaks)) {

  ## create a linelist
  x <- measles_hagelloch_1861 |>
    make_linelist(
      id = "case_ID",
      date_onset = "date_of_prodrome",
      age = "age",
      gender = "gender"
    )
  x

  ## get a data.frame of all tagged variables
  tags_df(x)
}
```
