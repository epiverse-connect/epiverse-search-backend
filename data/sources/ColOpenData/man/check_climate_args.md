# Check arguments in climate functions

```r
check_climate_args(start_date, end_date, tag)
```

## Arguments

- `start_date`: character with the first date to consult in the format `"YYYY-MM-DD"`. (First available date is `"1920-01-01"`).
- `end_date`: character with the last date to consult in the format `"YYYY-MM-DD"`. (Last available date is `"2023-05-31"`).
- `tag`: character containing climate tag to consult.

## Returns

list with the arguments in the needed formats. If the input is invalid an error will be thrown.

Climate functions have three common arguments: `start_date`, `end_date` and `tag`. This function checks that `start_date`

and `end_date` can be converted to date using the format "YYYY-MM-DD", that `end_date` is greater than `start_date`, and that the `tag` requested exists.
