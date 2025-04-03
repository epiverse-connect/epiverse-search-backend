# Add an element to the report object

```r
add_to_report(x, key, value = NULL)
```

## Arguments

- `x`: A `<data.frame>` or `<linelist>`
- `key`: A `<character>` with the name of the cleaning operation
- `value`: The object to add to the report object

## Returns

The input `<data.frame>` or `<linelist>` with an additional element to the report.

Add an element to the report object

## Examples

```r
# scan through the data
scan_res <- scan_data(
  data = readRDS(system.file("extdata", "test_df.RDS", package = "cleanepi"))
)

# Perform data cleaning
cleaned_data <- clean_data(
  data = readRDS(
    system.file("extdata", "test_df.RDS", package = "cleanepi")
  ),
  to_numeric = list(target_columns = "sex", lang = "en"),
  dictionary = NULL
)

# add the data scanning result to the report
cleaned_data <- add_to_report(
  x = cleaned_data,
  key = "scanning_result",
  value = scan_res
)
```
