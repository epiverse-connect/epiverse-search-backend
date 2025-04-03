# Build the auto-detected format

```r
date_make_format(f1, f2, f3)
```

## Arguments

- `f1`: A `<character>` with the first part of the inferred format
- `f2`: A `<character>` with the second part of the inferred format
- `f3`: A `<character>` with the third part of the inferred format

## Returns

A `<character>` that represents the inferred format from the provided elements. It returns `<NULL>` when the format was not resolved.

Put together the different date format characters that were identified from the target date column.
