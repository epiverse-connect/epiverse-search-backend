# Get the list of tags in a linelist

```r
tags(x, show_null = FALSE)
```

## Arguments

- `x`: a `linelist` object
- `show_null`: a `logical` indicating if the complete list of tags, including `NULL` ones, should be returned; if `FALSE`, only tags with a non-NULL value are returned; defaults to `FALSE`

## Returns

The function returns a named `list` where names indicate generic types of data, and values indicate which column they correspond to.

This function returns the list of tags identifying specific variable types in a `linelist`.

## Details

Tags are stored as the `tags` attribute of the object.

## Examples

```r
if (require(outbreaks)) {
  ## make a linelist
  x <- make_linelist(measles_hagelloch_1861, date_onset = "date_of_prodrome")

  ## check non-null tags
  tags(x)

  ## get a list of all tags, including NULL ones
  tags(x, TRUE)
}
```
