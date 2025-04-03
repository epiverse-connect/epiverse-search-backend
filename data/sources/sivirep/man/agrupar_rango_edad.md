# Agrupar por rango de edad y casos

```r
agrupar_rango_edad(
  data_event,
  col_edad = "edad",
  col_adicional = NULL,
  min_val,
  max_val,
  paso,
  porcentaje = TRUE
)
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de la enfermedad o evento.
- `col_edad`: Un `character` (cadena de caracteres) con el nombre de la columna que contiene las edades en los datos de la enfermedad o evento.
- `col_adicional`: Un `character` (cadena de caracteres) con el nombre de la columna adicional para agrupar con las edades en los datos de la enfermedad o evento; su valor por defecto es `NULL`.
- `min_val`: Un `numeric` (numérico) que contiene la edad mínima con la que debe iniciar el rango de edades.
- `max_val`: Un `numeric` (numérico) que contiene la edad máxima con la que debe finalizar el rango de edades.
- `paso`: Un `numeric` (numérico) que contiene el valor del paso para generar el rango de edades.
- `porcentaje`: Un `logical` (TRUE o FALSE) que indica si se debe agregar una columna con el porcentaje de casos; su valor por defecto es `TRUE`.

## Returns

Un `data.frame` con los datos de la enfermedad o evento agrupados por el rango de edad y número de casos.

Función que agrupa los datos de una enfermedad o evento por rango de edad y número de casos.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
data_edad <- agrupar_cols_casos(
  data_event = data_limpia,
  c("edad", "semana"),
  porcentaje = TRUE
)
agrupar_rango_edad(
  data_event = data_edad,
  col_edad = "edad",
  min_val = 0,
  max_val = max(data_edad$edad, na.rm = TRUE),
  paso = 10,
  porcentaje = TRUE
)
```
