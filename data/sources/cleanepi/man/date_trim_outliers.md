# Trim dates outside of the defined timeframe

```r
date_trim_outliers(new_dates, dmin, dmax, cols, original_dates)
```

## Arguments

- `new_dates`: A `<vector>` of the new date values
- `dmin`: A `<Date>` value with the minimum date
- `dmax`: A `<Date>` value with the maximum date
- `cols`: A `<character>` with the name of the date column of interest
- `original_dates`: A `<vector>` of the original date values

## Returns

A `<list>` of 2 elements: the update input vector where date values that are out of the specified timeframe are replaced by `NA`, and a vector of the out of timeframe values.

Trim dates outside of the defined timeframe
