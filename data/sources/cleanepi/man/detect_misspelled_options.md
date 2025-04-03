# Detect misspelled options in columns to be cleaned

```r
detect_misspelled_options(data, dictionary)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`
- `dictionary`: A `<data.frame>` with the dictionary associated with the input data. This is expected to be compatible with the `matchmaker` package and must contain the following four columns:
    
    - **`options`**: This column contains the current values used to represent the different groups in the input data frame (required).
    - **`values`**: The values that will be used to replace the current options (required).
    - **`grp`**: The name of the columns where every option belongs to (required).
    - **`orders`**: This defines the user-defined order of different options (optional).

## Returns

A `<list>` with the indexes of the misspelled values in every column that needs to be cleaned.

Detect misspelled options in columns to be cleaned
