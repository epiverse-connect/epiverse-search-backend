# Remove constant data, including empty rows, empty columns, and columns with constant values.

```r
remove_constants(data, cutoff = 1)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`
- `cutoff`: A `<numeric>` value specifying the cut-off for removing empty rows and columns. If provided, only rows and columns with a percentage of missing data greater than this cut-off will be removed. The default is 1.

## Returns

The input dataset with empty rows, empty columns, and constant columns removed.

The function iteratively removes constant data until none remain. It records details of the removed constant data as a data frame within the report object.

## Examples

```r
data <- readRDS(system.file("extdata", "test_df.RDS", package = "cleanepi"))

# introduce an empty column
data$empty_column <- NA
# inject some missing values across some columns
data$study_id[3] = NA_character_
data$date.of.admission[3] = NA_character_
data$date.of.admission[4] = NA_character_
data$dateOfBirth[3] = NA_character_
data$dateOfBirth[4] = NA_character_
data$dateOfBirth[5] = NA_character_

# with cutoff = 1, line 3, 4, and 5 are not removed
test <- remove_constants(
  data = data,
  cutoff = 1
)

# drop rows or columns with a percentage of constant values
# equal to or more than 50%
test <- remove_constants(
  data = test,
  cutoff = 0.5
)

# drop rows or columns with a percentage of constant values
# equal to or more than 25%
test <- remove_constants(
  data = test,
  cutoff = 0.25
)

# drop rows or columns with a percentage of constant values
# equal to or more than 15%
test <- remove_constants(
  data = test,
  cutoff = 0.15
)

# check the report to see what has happened
report <- attr(test, "report")
report$constant_data
```
