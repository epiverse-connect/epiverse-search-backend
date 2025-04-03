# Limpiar los valores atípicos de los datos

```r
limpiar_val_atipic(data_event)
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de una enfermedad o evento.

## Returns

Un `data.frame` con los datos de una enfermedad o evento con los valores atípicos limpios (convertidos a `NA`).

Función que limpia los valores atípicos de los datos de una enfermedad o evento del SIVIGILA.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_encabezado(data_event = dengue2020)
limpiar_val_atipic(data_limpia)
```
