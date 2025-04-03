# Scan through a data frame and return the proportion of `missing`, `numeric`, `Date`, `character`, `logical` values.

```r
scan_data(data)
```

## Arguments

- `data`: A `<data.frame>` or `<linelist>`

## Returns

A `<data.frame>` if the input data contains columns of type character. It invisibly returns `NA` otherwise. The returned data frame will have the same number of rows as the number of character columns, and six columns representing their column names, proportion of missing, numeric, date, character, and logical values.

The function checks for the existence of character columns in the data. When found, it reports back the proportion of the data types mentioned above in those columns. See the details section to know more about how it works.

## Details

How does it work? The `<character>` columns are identified first. If no `<character>`

columns are found, the function returns a message.

For each `<character>` column, the function counts:

1. The number of missing values (`NA`).
2. The number of numeric values. A process is initiated to detect valid dates among these numeric values using `lubridate::as_date()` and `date_guess()` functions. If valid dates are found, a warning is triggered to alert about ambiguous numeric values potentially representing dates. Note: A date is considered valid if it falls within the range from today's date to 50 years in the past.
3. The detection of `\<Date\>` values from non-numeric data using the `date_guess()` function. The total date count includes dates from today's from both numeric and non-numeric values. Due to overlap, the sum of counts across rows in the scanning result may exceed 1.
4. The count of `\<logical\>` values.

Remaining values are categorized as `<character>`.

## Examples

```r
# scan through a data frame of characters
scan_result <- scan_data(
  data = readRDS(
    system.file("extdata", "messy_data.RDS", package = "cleanepi")
  )
)

# scan through a data frame with two character columns
scan_result <- scan_data(
  data = readRDS(system.file("extdata", "test_linelist.RDS",
                             package = "cleanepi"))
)

# scan through a data frame with no character columns
data(iris)
iris[["fct"]] <- as.factor(sample(c("gray", "orange"), nrow(iris),
                           replace = TRUE))
iris[["lgl"]] <- sample(c(TRUE, FALSE), nrow(iris), replace = TRUE)
iris[["date"]] <- as.Date(seq.Date(from = as.Date("2024-01-01"),
                                   to = as.Date("2024-08-30"),
                                   length.out = nrow(iris)))
iris[["posit_ct"]] <- as.POSIXct(iris[["date"]])
scan_result <- scan_data(data = iris)
```
