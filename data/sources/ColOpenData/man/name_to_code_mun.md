# Retrieve municipalities' DIVIPOLA codes from names

```r
name_to_code_mun(department_name, municipality_name)
```

## Arguments

- `department_name`: character vector with the names of the departments containing the municipalities.
- `municipality_name`: character vector with the names of the municipalities.

## Returns

character vector with the DIVIPOLA codes of the municipalities.

Retrieve municipalities' DIVIPOLA codes from their names. Since there are municipalities with the same names in different departments, the input must include two vectors: one for the departments and one for the municipalities in said departments. If only one department is provided, it will try to match all municipalities in the second vector inside that department. Otherwise, the vectors must be the same length.

## Examples

```r
dptos <- c("Huila", "Antioquia")
mpios <- c("Pitalito", "Turbo")
name_to_code_mun(dptos, mpios)
```
