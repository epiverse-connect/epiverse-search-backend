# Printing method for linelist objects

```r
## S3 method for class 'linelist'
print(x, ...)
```

## Arguments

- `x`: a `linelist` object
- `...`: further arguments to be passed to 'print'

## Returns

Invisibly returns the object.

This function prints linelist objects.

## Examples

```r
if (require(outbreaks)) {

  ## dataset we'll create a linelist from
  measles_hagelloch_1861

  ## create linelist
  x <- make_linelist(measles_hagelloch_1861,
    id = "case_ID",
    date_onset = "date_of_prodrome",
    age = "age",
    gender = "gender"
  )

  ## print object - using only the first few entries
  head(x)

  # version with a tibble
  if (require(tibble)) {
    measles_hagelloch_1861 |>
      tibble() |>
      make_linelist(
        id = "case_ID",
        date_onset = "date_of_prodrome",
        age = "age",
        gender = "gender"
      )
  }
}
```
