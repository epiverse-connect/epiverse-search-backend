# Replace missing values with `NA`

```r
replace_missing_values(
  data,
  target_columns = NULL,
  na_strings = cleanepi::common_na_strings
)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`
- `target_columns`: A `<vector>` of column names. If provided, missing values will be substituted only in the specified columns. When the input data is a `<linelist>` object, this parameter can be set to `linelist_tags` to replace missing values with `NA` in the tagged columns only.
- `na_strings`: A `<vector>` of characters that represent the missing values in the columns of interest. By default, it utilizes `cleanepi::common_na_strings`. However, if the missing values string in the columns of interest is not included in this predefined vector, it can be used as the value for this argument.

## Returns

The input data where missing values are replaced by `NA`.

Replace missing values with `NA`

## Examples

```r
cleaned_data <- replace_missing_values(
  data = readRDS(
    system.file("extdata", "test_df.RDS", package = "cleanepi")
  ),
  target_columns = "sex",
  na_strings = "-99"
)
```
