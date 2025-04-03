# Get ISCO-88 occupation labels from codes

```r
describe_occupation(isco_codes, sex = NULL, plot = NULL)
```

## Arguments

- `isco_codes`: A numeric vector of ISCO-88 occupation codes (major, submajor, minor, or unit)
- `sex`: A vector with the respective sex for isco_codes vector. The default value is NULL
- `plot`: A type of plot between treemap and circular packing. The default value is NULL

## Returns

A string vector of ISCO-88 labels

Function that translates a vector of ISCO-88 occupation codes into a vector of labels

## Examples

```r
demog_data <- data.frame(
  occupation_label =
    c(6111, 3221, 5113, 5133, 6111, 23, 25),
  sex = c("F", "M", "F", "F", "M", "M", "F")
)
describe_occupation(
  isco_codes = demog_data$occupation_label,
  sex = demog_data$sex, plot = "treemap"
)
```
