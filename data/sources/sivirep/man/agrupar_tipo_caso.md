# Agrupar por la clasificación inicial del caso

```r
agrupar_tipo_caso(data_event, cols_tipo = "tip_cas")
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de la enfermedad o evento.
- `cols_tipo`: Un `character` (cadena de caracteres) o `array` (arreglo) de `character` con el nombre de las columna(s) que contiene la clasificación inicial del caso en los datos de la enfermedad o evento; su valor por defecto es `"tip_cas"`.

## Returns

Un `data.frame` con los datos de la enfermedad o evento agrupados por la clasificación inicial del caso y/u otras variables como los años.

Función que agrupa los casos por la clasificación inicial del caso.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
agrupar_tipo_caso(
  data_event = data_limpia,
  cols_tipo = "tip_cas"
)
```
