# Generate report from data cleaning operations

```r
print_report(
  data,
  report_title = "{cleanepi} data cleaning report",
  output_file_name = NULL,
  format = "html",
  print = TRUE
)
```

## Arguments

- `data`: A `<data.frame>` or `<linelist>` object returned from the `clean_data` or the main functions of each data cleaning module.
- `report_title`: A `<character>` with the title that will appear on the report
- `output_file_name`: A `<character>` used to specify the name of the report file, excluding any file extension. If no file name is supplied, one will be automatically generated with the format `cleanepi_report_YYMMDD_HHMMSS`.
- `format`: A `<character>` with the file format of the report. Currently only `"html"` is supported.
- `print`: A `<logical>` that specifies whether to print the generated HTML file or no. Default is `TRUE`.

## Returns

A `<character>` containing the name and path of the saved report

Generate report from data cleaning operations

## Examples

```r
data <- readRDS(system.file("extdata", "test_df.RDS", package = "cleanepi"))
test_dictionary <- readRDS(
  system.file("extdata", "test_dictionary.RDS", package = "cleanepi")
)

# scan through the data
scan_res <- scan_data(data)

# Perform data cleaning
cleaned_data <- data %>%
 standardize_column_names(keep = NULL, rename = c("DOB" = "dateOfBirth")) %>%
 replace_missing_values(target_columns = NULL, na_strings = "-99") %>%
 remove_constants(cutoff = 1.0) %>%
 remove_duplicates(target_columns = NULL) %>%
 standardize_dates(
   target_columns = NULL,
   error_tolerance = 0.4,
   format = NULL,
   timeframe = as.Date(c("1973-05-29", "2023-05-29"))
 ) %>%
 check_subject_ids(
   target_columns = "study_id",
   prefix = "PS",
   suffix = "P2",
   range = c(1L, 100L),
   nchar = 7L
 ) %>%
 convert_to_numeric(target_columns = "sex", lang = "en") %>%
 clean_using_dictionary(dictionary = test_dictionary)

# add the data scanning result to the report
cleaned_data <- add_to_report(
  x = cleaned_data,
  key = "scanning_result",
  value = scan_res
)

# save a report in the current directory using the previously-created objects
print_report(
  data = cleaned_data,
  report_title = "{cleanepi} data cleaning report",
  output_file_name = NULL,
  format = "html",
  print = TRUE
)
```
