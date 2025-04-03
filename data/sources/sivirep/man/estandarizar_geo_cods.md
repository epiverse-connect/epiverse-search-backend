# Estandarizar códigos geográficos de los datos de una enfermedad o evento

```r
estandarizar_geo_cods(data_event)
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de una enfermedad o evento con códigos geográficos.

## Returns

Un `data.frame` con los códigos geográficos estandarizados de los datos de una enfermedad o evento según la codificación del DIVIPOLA.

Función que estandariza los códigos geográficos de los datos de una enfermedad o evento según la codificación del DIVIPOLA.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
estandarizar_geo_cods(data_event = data_limpia)
```
