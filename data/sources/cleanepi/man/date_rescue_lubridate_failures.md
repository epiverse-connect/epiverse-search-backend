# Find the dates that lubridate couldn't

```r
date_rescue_lubridate_failures(date_a_frame, original_dates, column_name)
```

## Arguments

- `date_a_frame`: A `<data.frame>` where each column contains a different parsing of the same date vector
- `original_dates`: A `<vector>` of original dates
- `column_name`: A `<character>` with the target column name

## Returns

A `<list>` with the following two elements: the input data frame where the values that do not match the proposed formats have been converted into Date, and a boolean that informs about the presence of ambiguous values or not.

Find the dates that lubridate couldn't
