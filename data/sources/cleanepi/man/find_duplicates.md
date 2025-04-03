# Identify and return duplicated rows in a data frame or linelist.

```r
find_duplicates(data, target_columns = NULL)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`.
- `target_columns`: A `<vector>` of columns names or indices to consider when looking for duplicates. When the input data is a `<linelist>` object, this parameter can be set to `linelist_tags` from which duplicates to be removed. Its default value is `NULL`, which considers duplicates across all columns.

## Returns

A `<data.frame>` or `<linelist>` of all duplicated rows with following 2 additional columns:

- **row_id**: The indices of the duplicated rows from the input data. Users can choose from these indices, which row they consider as redundant in each group of duplicates.
- **group_id**: a unique identifier associated to each group of duplicates.

Identify and return duplicated rows in a data frame or linelist.

## Examples

```r
dups <- find_duplicates(
  data = readRDS(
    system.file("extdata", "test_linelist.RDS", package = "cleanepi")
  ),
  target_columns = c("dt_onset", "dt_report", "sex", "outcome")
)
```
