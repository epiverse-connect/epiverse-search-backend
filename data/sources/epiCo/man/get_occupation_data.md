# Auxiliary function to obtain the information of the occupations

```r
get_occupation_data(
  valid_codes,
  isco_codes,
  isco88_table,
  name_occupation,
  sex = NULL
)
```

## Arguments

- `valid_codes`: A numeric vector with the valid codes from the ISCO-88 table
- `isco_codes`: A numeric vector of ISCO-88 occupation codes (major, submajor, minor, or unit)
- `isco88_table`: The ISCO-88 table columns of the information for that group of occupations
- `name_occupation`: The category of occupations to be consulted. These can be: major, submajor, minor, or unit
- `sex`: A vector with the respective sex for isco_codes vector. The default value is NULL

## Returns

A dataframe with the information of the occupations

Auxiliary function to obtain the information of the occupations
