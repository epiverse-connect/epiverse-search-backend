# Translate municipality names to official municipalities' DIVIPOLA names

```r
name_to_standard_mun(department_name, municipality_name)
```

## Arguments

- `department_name`: character vector with the names of the departments containing the municipalities.
- `municipality_name`: character vector with the names to be translated.

## Returns

character vector with the DIVIPOLA name of the municipalities.

Municipality names are usually manually input, which leads to multiple errors and lack of standardization. This functions translates municipality names to their respective official names from DIVIPOLA.

## Examples

```r
dptos <- c("Bogota", "Tolima")
mpios <- c("Bogota DC", "CarmendeApicala")
name_to_standard_mun(dptos, mpios)
```
