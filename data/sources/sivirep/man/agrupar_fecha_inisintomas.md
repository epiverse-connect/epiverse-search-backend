# Agrupar por fecha de inicio de síntomas y casos

```r
agrupar_fecha_inisintomas(data_event, col_fecha = "ini_sin")
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de la enfermedad o evento.
- `col_fecha`: Un `character` (cadena de caracteres) con el nombre de la columna de los datos de la enfermedad o evento que contiene las fechas de inicio de síntomas; su valor por defecto es `"ini_sin"`.

## Returns

Un `data.frame` con los datos de la enfermedad o evento agrupados por fecha de inicio de síntomas y número de casos.

Función que agrupa los datos de una enfermedad o evento por fecha de inicio de síntomas y número de casos.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
agrupar_fecha_inisintomas(
  data_event = data_limpia,
  col_fecha = "ini_sin"
)
```
