# Get column names

```r
retrieve_column_names(data, target_columns)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`
- `target_columns`: A `<vector>` of column names. For `<linelist>` data, this can be set to `linelist_tags`

## Returns

A `<vector>` of column names to be used for the target cleaning operations

When performing several data cleaning operations using the `clean_data()` function, the input column names might be altered by after the column names cleaning. As a consequence of this, some cleaning operations will fail due to the column names mismatch. This function is provided to anticipate on this scenario, hence providing continuity between the cleaning operations.
