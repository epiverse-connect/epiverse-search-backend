# Internal function to truncate data based on start_cohort

```r
truncate_from_start_cohort(
  data_set,
  outcome_date_col,
  censoring_date_col,
  start_cohort
)
```

## Arguments

- `data_set`: `data.frame` with cohort information.
- `outcome_date_col`: Name of the column that contains the outcome dates.
- `censoring_date_col`: Name of the column that contains the censoring date. NULL by default.

## Returns

`data.frame` with truncated data

Internal function to truncate data based on start_cohort
