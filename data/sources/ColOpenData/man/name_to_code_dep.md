# Retrieve departments' DIVIPOLA codes from names

```r
name_to_code_dep(department_name)
```

## Arguments

- `department_name`: character vector with the names of the departments.

## Returns

character vector with the DIVIPOLA codes of the departments.

Retrieve departments' DIVIPOLA codes from their names.

## Examples

```r
dptos <- c("Tolima", "Huila", "Amazonas")
name_to_code_dep(dptos)
```
