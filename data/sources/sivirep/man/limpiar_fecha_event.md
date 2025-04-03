# Limpiar fechas de los datos de una enfermedad o evento

```r
limpiar_fecha_event(
  data_event,
  year,
  format_fecha = "%Y-%m-%d",
  col_fecha = "ini_sin",
  col_comp = NULL
)
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de una enfermedad o evento.
- `year`: Un `numeric` (numérico) o `character` (cadena de caracteres) que contiene el año de los datos de una enfermedad o evento.
- `format_fecha`: Un `character` (cadena de caracteres) que contiene el formato deseado de fecha; su valor por defecto es "%AAAA-%MM-%DD".
- `col_fecha`: Un `character` (cadena de caracteres) que contiene el nombre de la columna con la fecha que se desea limpiar en los datos de la enfermedad o evento.
- `col_comp`: Un `character` (cadena de caracteres) que contiene el nombre de la columna con la cual se va a comparar la columna `col_fecha` para limpiarla, estandarizarla o aplicar las reglas definidas.

## Returns

Un `data.frame` con las fechas limpias.

Función que limpia y estandariza las fechas de los datos de una enfermedad o evento.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
limpiar_fecha_event(
  data_event = data_limpia,
  year = 2020,
  format_fecha = "%Y-%m-%d",
  col_fecha = "ini_sin",
  col_comp = "fec_hos"
)
```
