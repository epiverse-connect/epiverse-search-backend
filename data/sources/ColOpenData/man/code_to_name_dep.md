# Retrieve departments' DIVIPOLA names from codes

```r
code_to_name_dep(department_code)
```

## Arguments

- `department_code`: character vector with the DIVIPOLA codes of the departments.

## Returns

character vector with the DIVIPOLA name of the departments.

Retrieve departments' DIVIPOLA official names from their DIVIPOLA codes.

## Examples

```r
dptos <- c("73", "05", "11")
code_to_name_dep(dptos)
```
