# Convert numeric to date

```r
convert_numeric_to_date(data, target_columns, ref_date, forward = TRUE)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`
- `target_columns`: A `<vector>` of columns names to be converted from numeric to date. When the input data is a `<linelist>` object, this parameter can be set to `linelist_tags` to apply the conversion exclusively to the tagged columns.
- `ref_date`: A `<Date>` value with reference date. This can also be a character string with the name of the reference column.
- `forward`: A `<logical>` to indicate whether the counts started after the reference date (`TRUE`) or not (`FALSE`). The default is `TRUE`.

## Returns

A `<data.frame>` or `<linelist>` where the column of interest are updated

Convert numeric to date

## Examples

```r
data <- readRDS(system.file("extdata", "test_df1.RDS", package = "cleanepi"))
data <- convert_numeric_to_date(
  data = data,
  target_columns = "recruited_on_day",
  ref_date = as.Date("2022-10-13"),
  forward = TRUE
)
```
