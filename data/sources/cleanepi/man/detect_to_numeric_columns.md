# Detect the numeric columns that appears as characters due to the presence of some character values in the column.

```r
detect_to_numeric_columns(scan_res, data)
```

## Arguments

- `scan_res`: A `<data.frame>` that corresponds to the result from the `scan_data` function
- `data`: The input `<data.frame>` or `<linelist>`

## Returns

a `<vector>` of column names to be converted into numeric

Detect the numeric columns that appears as characters due to the presence of some character values in the column.
