# Try and guess dates from a characters

```r
date_guess(x, column_name, quiet = TRUE, orders = NULL)
```

## Arguments

- `x`: A `<vector>` of characters or factors
- `column_name`: A `<character>` with the target column name
- `quiet`: A `<logical>` indicating if messages should be displayed to the console. Default is `TRUE`; set to `FALSE` to silence messages
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

A `<list>` of following three elements: a vector of the newly reformatted dates, a data frame with the date values that were converted based on more than one format, and a Boolean that specifies whether ambiguous values were found or not. If all values comply with only one format, the second element will be NULL.

Note that THIS FEATURE IS STILL EXPERIMENTAL: we strongly recommend checking a few converted dates manually. This function tries to extract dates from a `character` vector or a `factor`. It treats each entry independently, using regular expressions to detect if a date is present, its format, and if successful it converts that entry to a standard `Date` with the **Ymd** format (e.g. `2018-01-21`). Entries which cannot be processed result in `NA`. An error threshold can be used to define the maximum number of resulting `NA`

(i.e. entries without an identified date) that can be tolerated. If this threshold is exceeded, the original vector is returned.
