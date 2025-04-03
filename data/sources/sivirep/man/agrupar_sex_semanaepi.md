# Agrupar por sexo, semana epidemiológica y casos

```r
agrupar_sex_semanaepi(
  data_event,
  cols_sex = c("sexo", "semana"),
  porcentaje = TRUE
)
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de la enfermedad o evento.
- `cols_sex`: Un `character` (cadena de caracteres) o `array` (arreglo) de `character` con el nombre de la(s) columna(s) que contienen el sexo y las semanas epidemiológicas; su valor por defecto es `c("sexo", "semana")`.
- `porcentaje`: Un `logical` (TRUE o FALSE) que indica si se debe agregar una columna con el porcentaje de casos; su valor por defecto es `TRUE`.

## Returns

Un `data.frame` con los datos de la enfermedad o evento agrupados por sexo, semana epidemiológica y número de casos.

Función que agrupa los datos de enfermedades por sexo, semana epidemiológica y número de casos.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
agrupar_sex_semanaepi(
  data_event = data_limpia,
  cols_sex = c("sexo", "semana"),
  porcentaje = TRUE
)
```
