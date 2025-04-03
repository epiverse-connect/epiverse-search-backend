# Perform dictionary-based cleaning

```r
clean_using_dictionary(data, dictionary)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`
- `dictionary`: A `<data.frame>` with the dictionary associated with the input data. This is expected to be compatible with the `matchmaker` package and must contain the following four columns:
    
    - **`options`**: This column contains the current values used to represent the different groups in the input data frame (required).
    - **`values`**: The values that will be used to replace the current options (required).
    - **`grp`**: The name of the columns where every option belongs to (required).
    - **`orders`**: This defines the user-defined order of different options (optional).

## Returns

A `<data.frame>` or `<linelist>` where the target options have been replaced with their corresponding values in the columns specified in the data dictionary.

Perform dictionary-based cleaning

## Examples

```r
data <- readRDS(
  system.file("extdata", "messy_data.RDS", package = "cleanepi")
)
dictionary <- readRDS(
  system.file("extdata", "test_dict.RDS", package = "cleanepi")
)

# adding an option that is not defined in the dictionary to the 'gender'
# column
data$gender[2] <- "homme"
cleaned_df <- clean_using_dictionary(
  data = data,
  dictionary = dictionary
)
```
