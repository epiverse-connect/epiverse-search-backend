# Check whether the subject IDs comply with the expected format. When incorrect IDs are found, the function sends a warning and the user can call the `correct_subject_ids` function to correct them.

```r
check_subject_ids(
  data,
  target_columns,
  prefix = NULL,
  suffix = NULL,
  range = NULL,
  nchar = NULL
)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`
- `target_columns`: A `<vector>` of column names with the subject ids.
- `prefix`: A `<character>` with the expected prefix used in the subject IDs
- `suffix`: A `<character>` with the expected suffix used in the subject IDs
- `range`: A `<vector>` with the expected range of numbers in the subject IDs
- `nchar`: An `<integer>` that represents the expected number of characters in the subject ids.

## Returns

The input dataset with a warning if incorrect subject ids were found

Check whether the subject IDs comply with the expected format. When incorrect IDs are found, the function sends a warning and the user can call the `correct_subject_ids` function to correct them.

## Examples

```r
dat <- check_subject_ids(
  data = readRDS(
    system.file("extdata", "test_df.RDS", package = "cleanepi")
  ),
  target_columns = "study_id",
  prefix = "PS",
  suffix = "P2",
  range = c(1, 100),
  nchar = 7
)
```
