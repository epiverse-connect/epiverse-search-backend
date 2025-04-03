# Agrupar por semana epidemiológica y casos

```r
agrupar_semanaepi(data_event, col_semanaepi = "semana")
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de una enfermedad o evento.
- `col_semanaepi`: Un `character` (cadena de caracteres) con el nombre de la columna que contiene las semanas epidemiológicas en los datos de la enfermedad o evento; su valor por defecto es `"semana"`.

## Returns

Un `data.frame` con los datos de una enfermedad o evento agrupados por semana epidemiológica y número de casos.

Función que agrupa los datos de una enfermedad o evento por semana epidemiológica y número de casos.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
agrupar_semanaepi(
  data_event = data_limpia,
  col_semanaepi = "semana"
)
```
