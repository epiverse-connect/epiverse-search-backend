# Agrupar por departamento y casos

```r
agrupar_dpto(data_event, col_dpto = "cod_dpto_o", porcentaje = FALSE)
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de la enfermedad o evento.
- `col_dpto`: Un `character` (cadena de caracteres) con el nombre de la columna que contiene los códigos de los departamentos en los datos de la enfermedad o evento; su valor por defecto es `"cod_dpto_o"`.
- `porcentaje`: Un `logical` (TRUE o FALSE) que indica si se debe agregar una columna con el porcentaje de casos; su valor por defecto es `FALSE`.

## Returns

Un `data.frame` con los datos de la enfermedad o evento agrupados por códigos de departamento y número de casos.

Función que agrupa los datos por códigos de departamento y número de casos.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
agrupar_dpto(
  data_event = data_limpia,
  col_dpto = "cod_dpto_o",
  porcentaje = FALSE
)
```
