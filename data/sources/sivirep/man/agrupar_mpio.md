# Agrupar por municipios y casos

```r
agrupar_mpio(
  data_event,
  dpto = NULL,
  col_mpio = "cod_mun_o",
  porcentaje = FALSE
)
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de la enfermedad o evento.
- `dpto`: Un `character` (cadena de caracteres) o `numeric` (numérico) que contiene el nombre del departamento; su valor por defecto es `NULL`.
- `col_mpio`: Un `character` (cadena de caracteres) con el nombre de la columna que contiene los códigos de los municipios en los datos de la enfermedad o evento; su valor por defecto es `"cod_mun_o"`.
- `porcentaje`: Un `logical` (TRUE o FALSE) que indica si se debe agregar una columna con el porcentaje de casos; su valor por defecto es `FALSE`.

## Returns

Un `data.frame` con los datos de la enfermedad o evento agrupados por códigos de municipios y número de casos.

Función que agrupa los datos de una enfermedad o evento por código de municipios y número de casos.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
agrupar_mpio(
  data_event = data_limpia,
  dpto = "ANTIOQUIA",
  col_mpio = "cod_mun_o",
  porcentaje = FALSE
)
agrupar_mpio(
  data_event = data_limpia,
  dpto = "05",
  col_mpio = "cod_mun_o",
  porcentaje = FALSE
)
agrupar_mpio(
  data_event = data_limpia,
  dpto = 05,
  col_mpio = "cod_mun_o",
  porcentaje = TRUE
)
```
