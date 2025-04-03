# Convert columns into numeric

```r
convert_to_numeric(data, target_columns = NULL, lang = c("en", "fr", "es"))
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`
- `target_columns`: A `<vector>` of the target column names. When the input data is a `<linelist>` object, this parameter can be set to `linelist_tags` to apply the conversion exclusively to the tagged columns. .
- `lang`: A `<character>` with the text's language. Currently one of `"en"`, `"fr"`, `"es"`.

## Returns

A `<data.frame>` or `<linelist>` wherein all the specified or detected columns have been transformed into numeric format after the conversion process.

When this function is invoked without specifying the column names to be converted, the target columns are the ones returned by the `scan_data()`

function. Furthermore, it identifies columns where the proportion of numeric values is at least twice the percentage of character values and performs the conversion in them. The function internally makes call of the main function from the `numberize` package.

## Examples

```r
dat <- convert_to_numeric(
  data = readRDS(
    system.file("extdata", "messy_data.RDS", package = "cleanepi")
  ),
  target_columns = "age",
  lang = "en"
)
```
