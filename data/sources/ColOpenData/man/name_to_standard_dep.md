# Translate department names to official departments' DIVIPOLA names

```r
name_to_standard_dep(department_name)
```

## Arguments

- `department_name`: character vector with the names to be translated.

## Returns

character vector with the DIVIPOLA name of the departments.

Department names are usually manually input, which leads to multiple errors and lack of standardization. This functions translates department names to their respective official names from DIVIPOLA.

## Examples

```r
dptos <- c("Bogota DC", "San Andres")
name_to_standard_dep(dptos)
```
