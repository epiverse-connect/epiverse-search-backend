# Add an element to the data dictionary

```r
add_to_dictionary(dictionary, option, value, grp, order = NULL)
```

## Arguments

- `dictionary`: A `<data.frame>` with the dictionary associated with the input data. This is expected to be compatible with the `matchmaker` package and must contain the following four columns:
    
    - **`options`**: This column contains the current values used to represent the different groups in the input data frame (required).
    - **`values`**: The values that will be used to replace the current options (required).
    - **`grp`**: The name of the columns where every option belongs to (required).
    - **`orders`**: This defines the user-defined order of different options (optional).
- `option`: A `<vector>` of characters with the new options that need to be added to the dictionary.
- `value`: A `<vector>` of characters with the values to be used when replacing the new options.
- `grp`: A `<vector>` of characters with the name of the column that contains the option of interest.
- `order`: A `<vector>` of numeric values with the order of the new option.

## Returns

A `<data.frame>`. This is the new data dictionary with an additional line that contains the details about the new options.

Add an element to the data dictionary

## Examples

```r
test <- add_to_dictionary(
  dictionary = readRDS(
    system.file("extdata", "test_dict.RDS", package = "cleanepi")
  ),
  option = "ml",
  value = "male",
  grp = "gender",
  order = NULL
 )
```
