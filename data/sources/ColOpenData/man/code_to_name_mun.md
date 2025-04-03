# Retrieve municipalities' DIVIPOLA names from codes

```r
code_to_name_mun(municipality_code)
```

## Arguments

- `municipality_code`: character vector with the DIVIPOLA codes of the municipalities.

## Returns

character vector with the DIVIPOLA name of the municipalities.

Retrieve municipalities' DIVIPOLA official names from their DIVIPOLA codes.

## Examples

```r
mpios <- c("73001", "11001", "05615")
code_to_name_mun(mpios)
```
