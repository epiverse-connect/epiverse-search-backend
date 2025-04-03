# Convert and update date values

```r
date_check_outsiders(data, timeframe, new_dates, cols)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`
- `timeframe`: A `<vector>` of 2 values of type `<Date>`. If provided, date values that do not fall within this timeframe will be set to `NA`.
- `new_dates`: A `<vector>` of the converted date values
- `cols`: A `<character>` with the names of the date column to be converted

## Returns

A `<list>` of 2 data frames: the updated input data (if some columns were converted to Date) and a data frame of date values that are not within the specified timeframe.

Convert and update date values
