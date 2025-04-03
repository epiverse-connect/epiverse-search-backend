# Agrupar por sexo y casos

```r
agrupar_sex(data_event, col_sex = "sexo", porcentaje = TRUE)
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de la enfermedad o evento.
- `col_sex`: Un `character` (cadena de caracteres) con el nombre de la columna que contiene el sexo en los datos de la enfermedad o evento; su valor por defecto es `"sexo"`.
- `porcentaje`: Un `logical` (TRUE o FALSE) que indica si se debe agregar una columna con el porcentaje de casos; su valor por defecto es `TRUE`.

## Returns

Un `data.frame` con los datos de la enfermedad o evento agrupados por sexo y número de casos.

Función que agrupa los datos de una enfermedad o evento por sexo y número de casos.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
agrupar_sex(
  data_event = data_limpia,
  col_sex = "sexo",
  porcentaje = TRUE
)
```
