# Guess if a character vector contains Date values, and convert them to date

```r
date_guess_convert(data, error_tolerance, timeframe, orders)
```

## Arguments

- `data`: A `<data.frame>`
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

A `<list>` with the following two elements: the input data frame where the character columns with date values have been converted into `<Date>`, and a vector of column names where there are numeric values that can also be of type Date.

Guess if a character vector contains Date values, and convert them to date
