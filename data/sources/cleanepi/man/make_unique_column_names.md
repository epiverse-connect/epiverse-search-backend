# Make column names unique when duplicated column names are found after the transformation

```r
make_unique_column_names(after, kept, before, rename)
```

## Arguments

- `after`: A `<vector>` with the transformed column names
- `kept`: A `<logical>` vector where column names to keep are set to TRUE
- `before`: A `<vector>` with the initial column names
- `rename`: A `<vector>` with the indices of the column names to be renamed

## Returns

An adjusted `<vector>` if there were duplicated names introduced due to the transformation

Make column names unique when duplicated column names are found after the transformation
