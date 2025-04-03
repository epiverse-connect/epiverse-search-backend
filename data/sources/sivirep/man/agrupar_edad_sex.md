# Agrupar por edades, sexo y casos

```r
agrupar_edad_sex(
  data_event,
  col_edad = "edad",
  col_sex = "sexo",
  porcentaje = TRUE,
  interval_edad = 10
)
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de la enfermedad o evento.
- `col_edad`: Un `character` (cadena de caracteres) con el nombre de la columna que contiene las edades en los datos de la enfermedad o evento; su valor por defecto es `"edad"`.
- `col_sex`: Un `character` (cadena de caracteres) con el nombre de la columna que contiene el sexo en los datos de la enfermedad o evento; su valor por defecto es `"sexo`.
- `porcentaje`: Un `logical` (TRUE o FALSE) que indica si se debe agregar una columna con el porcentaje de casos; su valor por defecto es `TRUE`.
- `interval_edad`: Un `numeric` (numérico) que contiene el intervalo del rango de edades; su valor por defecto es `10`.

## Returns

Un `data.frame` con los datos de enfermedades agrupados por edades, sexo y número de casos.

Función que agrupa los datos de una enfermedad o evento por edades, sexo y número de casos.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
agrupar_edad_sex(
  data_event = data_limpia,
  col_edad = "edad",
  col_sex = "sexo",
  porcentaje = TRUE
)
```
