# Agrupar por la pertenencia étnica

```r
agrupar_per_etn(data_event, cols_etn = "per_etn", porcentaje = TRUE)
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de la enfermedad o evento.
- `cols_etn`: Un `character` (cadena de caracteres) o un `array` de `character` con el nombre de la(s) columna(s) que contiene(n) la pertenencia étnica en los datos de la enfermedad o evento; su valor por defecto es `"per_etn"`
- `porcentaje`: Un `logical` (TRUE o FALSE) que indica si se debe agregar una columna con el porcentaje de casos; su valor por defecto es `TRUE`.

## Returns

Un `data.frame` con los datos de la enfermedad o evento agrupados por la pertenencia étnica.

Función que agrupa los casos por la pertenencia étnica.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
agrupar_per_etn(
  data_event = data_limpia,
  cols_etn = "per_etn"
)
```
