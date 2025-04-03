# Limpiar las etiquetas del encabezado

```r
limpiar_encabezado(data_event)
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de una enfermedad o evento.

## Returns

Un `data.frame` con las etiquetas del encabezado formateadas con guiones bajos (_).

Función que limpia las etiquetas del encabezado de los datos de una enfermedad o evento.

## Examples

```r
data(dengue2020)
limpiar_encabezado(data_event = dengue2020)
```
