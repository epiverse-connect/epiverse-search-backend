# Changes tags of a linelist object

```r
set_tags(x, ..., allow_extra = FALSE)
```

## Arguments

- `x`: a `data.frame` or a `tibble` containing case line list data, with cases in rows and variables in columns
- `...`: <`dynamic-dots`> A series of tags provided as `tag_name = "column_name"`, where `tag_name` indicates any of the known variables listed in 'Details' and values indicate their name in `x`; see details for a list of known variable types and their expected content
- `allow_extra`: a `logical` indicating if additional data tags not currently recognized by `linelist` should be allowed; if `FALSE`, unknown tags will trigger an error

## Returns

The function returns a `linelist` object.

This function changes the `tags` of a `linelist` object, using the same syntax as the constructor `make_linelist()`. If some of the default tags are missing, they will be added to the final object.

## Examples

```r
if (require(outbreaks)) {
  ## create a linelist
  x <- make_linelist(measles_hagelloch_1861, date_onset = "date_of_rash")
  tags(x)

  ## add new tags and fix an existing one
  x <- set_tags(x,
    age = "age",
    gender = "gender",
    date_onset = "date_of_prodrome"
  )
  tags(x)

  ## add non-default tags using allow_extra
  x <- set_tags(x, severe = "complications", allow_extra = TRUE)
  tags(x)

  ## remove tags by setting them to NULL
  old_tags <- tags(x)
  x <- set_tags(x, age = NULL, gender = NULL)
  tags(x)

  ## setting tags providing a list (used to restore old tags here)
  x <- set_tags(x, !!!old_tags)
  tags(x)
}
```

## See Also

`make_linelist()` to create a `linelist` object
