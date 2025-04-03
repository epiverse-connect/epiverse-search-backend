# Agrupar por tipo de enfermedad o evento

```r
agrupar_eventos(data_event, col_event = "cod_eve")
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de la enfermedad o evento.
- `col_event`: Un `character` (cadena de caracteres) con el nombre de la columna que contiene los códigos de los eventos o de las enfermedades en los datos; su valor por defecto es `"cod_eve"`.

## Returns

Un `data.frame` con los datos de la enfermedad o evento agrupados por tipo.

Función que agrupa los casos por tipo de enfermedad o evento.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
agrupar_eventos(
  data_event = data_limpia,
  col_event = "cod_eve"
)
```
