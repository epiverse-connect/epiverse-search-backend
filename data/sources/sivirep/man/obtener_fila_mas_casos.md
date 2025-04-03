# Obtener la fila con mayor número de casos

```r
obtener_fila_mas_casos(data_event, nomb_col = "casos", porcentaje = TRUE)
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de la enfermedad o evento.
- `nomb_col`: Un `character` (cadena de caracteres) con el nombre de la columna que contiene el número de casos en los datos de la enfermedad o evento.
- `porcentaje`: Un `logical` (`TRUE` o `FALSE`) que indica si se requiere agregar un porcentaje de casos como columna.

## Returns

Un `data.frame` que contiene la fila con mayor número de casos.

Función que obtiene la fila con el mayor número de casos.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(dengue2020)
casos_sex <- agrupar_sex(
  data_event = data_limpia,
  porcentaje = TRUE
)
obtener_fila_mas_casos(
  data_event = casos_sex,
  nomb_col = "casos",
  porcentaje = TRUE
)
```
