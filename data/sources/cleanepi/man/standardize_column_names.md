# Standardize column names of a data frame or line list

```r
standardize_column_names(data, keep = NULL, rename = NULL)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`.
- `keep`: A `<vector>` of column names to maintain as they are. When dealing with a `<linelist>`, this can be set to `linelist_tags`, to maintain the tagged column names. The Default is `NULL`.
- `rename`: A named `<vector>` of column names to be renamed. This should be in the form of `c(new_name1 = "old_name1", new_name2 = "old_name2")` for example.

## Returns

A `<data.frame>` or `<linelist>` with easy to work with column names.

All columns names will be reformatted to snake_case. When the conversion to snakecase does not work as expected, use the `keep` and/or `rename` arguments to reformat the column name properly.

## Examples

```r
# do not rename 'date.of.admission'
cleaned_data <- standardize_column_names(
  data = readRDS(
    system.file("extdata", "test_df.RDS", package = "cleanepi")
  ),
  keep = "date.of.admission"
)

# do not rename 'date.of.admission', but rename 'dateOfBirth' and 'sex' to
# 'DOB' and 'gender' respectively
cleaned_data <- standardize_column_names(
  data = readRDS(
    system.file("extdata", "test_df.RDS", package = "cleanepi")
  ),
  keep = "date.of.admission",
  rename = c(DOB = "dateOfBirth", gender = "sex")
)
```
