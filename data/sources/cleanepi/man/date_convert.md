# Convert characters to dates

```r
date_convert(data, cols, error_tolerance, timeframe = NULL, orders)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`
- `cols`: A `<Date>` column name(s)
- `error_tolerance`: A `<numeric>` between 0 and 1 indicating the proportion of entries which cannot be identified as dates to be tolerated; if this proportion is exceeded, the original vector is returned, and a message is issued; defaults to 0.4 (40 percent).
- `timeframe`: A `<vector>` of 2 values of type `<Date>`. If provided, date values that do not fall within this timeframe will be set to `NA`.
- `orders`: A `<list>` or `<vector>` of characters with the date codes for fine-grained parsing of dates. This allows for parsing of mixed dates. If a `<list>` is supplied, that `<list>` will be used for successive tries in parsing. When this is not provided (`orders = NULL`), the function will use the following order defined in the guesser:
    
     
    
    ```
    list(
      quarter_partial_dates = c("Y", "Ym", "Yq"),
      world_digit_months = c("Yq", "ymd", "ydm", "dmy", "mdy", "myd", "dym",
                        "Ymd", "Ydm", "dmY", "mdY", "mYd", "dYm"),
      world_named_months = c("dby", "dyb", "bdy", "byd", "ybd", "ydb",
                        "dbY", "dYb", "bdY", "bYd", "Ybd", "Ydb"),
      us_format = c("Omdy", "YOmd")
    )
    ```

## Returns

A `<list>` with the following two elements: a data frame where the specified columns have been converted into `<Date>` values, a boolean that tells whether numeric values that can also be of type `<Date>` are found in the specified columns.

Convert characters to dates
