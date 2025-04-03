# Agrupar por edad y casos

```r
agrupar_edad(
  data_event,
  col_edad = "edad",
  interval_edad = 10,
  porcentaje = FALSE
)
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de la enfermedad o evento.
- `col_edad`: Un `character` (cadena de caracteres) con el nombre de la columna que contiene las edades en los datos de la enfermedad o evento; su valor por defecto es `"edad"`.
- `interval_edad`: Un `numeric` (numérico) que contiene el intervalo del rango de edades; su valor por defecto es `10`.
- `porcentaje`: Un `logical` (TRUE o FALSE) que indica si se debe agregar una columna con el porcentaje de casos; su valor por defecto es `FALSE`.

## Returns

Un `data.frame` con los datos de la enfermedad o evento agrupados por edad y número de casos.

Función que agrupa los datos de una enfermedad o evento por edad y número de casos.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
agrupar_edad(
  data_event = data_limpia,
  col_edad = "edad",
  porcentaje = FALSE
)
```
