# List acceptable variable types for tags

```r
tags_types(..., allow_extra = FALSE)
```

## Arguments

- `...`: <`dynamic-dots`> A series of tags provided as `tag_name = "column_name"`, where `tag_name` indicates any of the known variables listed in 'Details' and values indicate their name in `x`; see details for a list of known variable types and their expected content
- `allow_extra`: a `logical` indicating if additional data tags not currently recognized by `linelist` should be allowed; if `FALSE`, unknown tags will trigger an error

## Returns

A named `list`.

This function returns a named list providing the acceptable data types for the default tags. If no argument is provided, it returns default values. Otherwise, provided values will be used to define the defaults.

## Examples

```r
# list default values
tags_types()

# change existing values
tags_types(date_onset = "Date") # impose a Date class

# add new types e.g. to allow genetic sequences using ape's format
tags_types(sequence = "DNAbin", allow_extra = TRUE)
```

## See Also

 * `tags_defaults()` for the default tags
 * `validate_types()` uses `tags_types()` for validating tags
 * `validate_linelist()` uses `tags_types()` for validating tags
