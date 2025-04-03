# Choose the first non-missing date from a data frame of dates

```r
date_choose_first_good(date_a_frame, column_name)
```

## Arguments

- `date_a_frame`: A `<data.frame>` where each column contains a different parsing of the same date vector
- `column_name`: A `<character>` with the target column name

## Returns

The chosen first `<Date>` value. When there other possible values for a given date, this will be registered in the report object.

Choose the first non-missing date from a data frame of dates
