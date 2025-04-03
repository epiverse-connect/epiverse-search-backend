# Calculate time span between dates

```r
timespan(
  data,
  target_column = NULL,
  end_date = Sys.Date(),
  span_unit = c("years", "months", "weeks", "days"),
  span_column_name = "span",
  span_remainder_unit = NULL
)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`
- `target_column`: A `<vector>` of character used to specify the name of the date column of interest. The values in this column should be of type `<Date>` in ISO8601 format, e.g., 2024-01-31.
- `end_date`: The end date. It can be either a `<character>` that is the name of another column of type `<Date>` from the input data or a `<vector>` of Dates or a single `<Date>` value. This should also be in the ISO8601 format, e.g., 2024-01-31. Default is today's date `Sys.Date()`.
- `span_unit`: A `<character>` that specifies the units in which the time span between the dates will be returned. The possible units are: 'years', 'months', 'weeks' or 'days'.
- `span_column_name`: A `<character>` that specifies the name of the new column to be used to store the calculated time span in the input data frame.
- `span_remainder_unit`: A `<character>` that specifies the unit in which the remainder of the time span should be calculated. May be one of "months", "weeks", and "days". Remainders requested in the same unit as the age will return values of 0. Default is `NULL` for decimal time span.

## Returns

The input `<data.frame>` with one or two additional columns:

- **span**: or any other name chosen by the user. This will contain the calculated time span in the desired units.
- **"*_remainder"**: a column with the number of the remaining days or weeks or months depending on the value of the 'span_remainder_unit' parameter. The star represents here the value of the 'span_column_name' argument.

Calculate time span between dates

## Examples

```r
# In the below example, this function is used to calculate patient's age from
# their dates of birth

# import the data, replace missing values with NA and convert date into ISO
# format
data <- readRDS(system.file("extdata", "test_df.RDS", package = "cleanepi"))
data <- data %>%
  replace_missing_values(target_columns = "dateOfBirth",
                         na_strings = "-99") %>%
  standardize_dates(target_columns = "dateOfBirth",
                    error_tolerance = 0.0)

# calculate the age in 'years' and return the remainder in 'months'
age <- timespan(
  data = data,
  target_column = "dateOfBirth",
  end_date = Sys.Date(),
  span_unit = "years",
  span_column_name = "age_in_years",
  span_remainder_unit = "months"
)
```
