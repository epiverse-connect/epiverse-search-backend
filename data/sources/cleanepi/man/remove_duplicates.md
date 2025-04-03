# Remove duplicates

```r
remove_duplicates(data, target_columns = NULL)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`.
- `target_columns`: A `<vector>` of column names to use when looking for duplicates. When the input data is a `linelist` object, this parameter can be set to `linelist_tags` if you wish to look for duplicates on tagged columns only. Default is `NULL`.

## Returns

The input data `<data.frame>` or `<linelist>` without the duplicated rows identified from all or the specified columns.

When removing duplicates, users can specify a set columns to consider with the `target_columns` argument.

## Examples

```r
no_dups <- remove_duplicates(
  data = readRDS(
    system.file("extdata", "test_linelist.RDS", package = "cleanepi")
  ),
  target_columns = "linelist_tags"
)
```
