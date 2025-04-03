# Remove constant data.

```r
perform_remove_constants(data, cutoff)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`
- `cutoff`: A `<numeric>` value specifying the cut-off for removing empty rows and columns. If provided, only rows and columns with a percentage of missing data greater than this cut-off will be removed. The default is 1.

## Returns

A `<list>` with the input dataset where all empty rows and columns as well as constant columns have been removed.

This function is called at each iteration of the constant data removal process until no constant data remains.
