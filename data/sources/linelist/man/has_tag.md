# A selector function to use in `tidyverse` functions

```r
has_tag(tags)
```

## Arguments

- `tags`: A character vector of tags listing the variables you want to operate on

## Returns

A numeric vector containing the position of the columns with the requested tags

A selector function to use in `tidyverse` functions

## Examples

```r
if (require(outbreaks) && require(dplyr)) {

  ## dataset we'll create a linelist from
  measles_hagelloch_1861

  ## create linelist
  x <- make_linelist(measles_hagelloch_1861,
    id = "case_ID",
    date_onset = "date_of_prodrome",
    age = "age",
    gender = "gender"
  )
  head(x)

  x |>
    select(has_tag(c("id", "age"))) |>
    head()
}
```
