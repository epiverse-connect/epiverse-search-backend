# Get the names of the columns from which duplicates will be found

```r
get_target_column_names(data, target_columns, cols)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`
- `target_columns`: A `<vector>` of column names. For `<linelist>` data, this can be set to `linelist_tags`
- `cols`: A `<vector>` of empty and constant columns

## Returns

A `<vector>` with the target column names or indexes

Get the names of the columns from which duplicates will be found
