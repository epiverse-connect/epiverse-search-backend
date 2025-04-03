# Obtener las condiciones para calcular la incidencia de una enfermedad o evento

```r
obtener_cond_inciden_event(cod_eve)
```

## Arguments

- `cod_eve`: Un `numeric` (numérico) o `character` (cadena de caracteres) que contiene el código de una enfermedad o evento.

## Returns

Un `data.frame` con las condiciones para calcular la incidencia de una enfermedad o evento.

Función que obtiene las condiciones del numerador, denominador y coeficiente de múltiplicación para calcular la incidencia de un evento.

## Examples

```r
obtener_cond_inciden_event(cod_eve = 210)
```
