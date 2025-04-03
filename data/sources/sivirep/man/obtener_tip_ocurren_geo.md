# Obtener columnas de ocurrencia geográfica de los datos de la enfermedad o evento

```r
obtener_tip_ocurren_geo(cod_event = NULL, nombre_event = NULL)
```

## Arguments

- `cod_event`: Un `numeric` (numérico) o `character` (cadena de caracteres) que contiene el código de la enfermedad o evento.
- `nombre_event`: Un `character` (cadena de caracteres) con el nombre de la enfermedad o evento.

## Returns

Un `data.frame` con las columnas de ocurrencia geográfica de los datos de la enfermedad o evento.

Función que obtiene las columnas de ocurrencia geográfica de los datos de la enfermedad o evento.

## Examples

```r
obtener_tip_ocurren_geo(cod_event = 210)
```
