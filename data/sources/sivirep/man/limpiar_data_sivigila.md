# Limpiar datos de SIVIGILA

```r
limpiar_data_sivigila(data_event, uni_med_edad = 1)
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de una enfermedad o evento.
- `uni_med_edad`: Un `numeric` (numérico) o `character`(cadena de caracteres) que contiene la unidad de medida a la que se debe estandarizar la edad; su valor por defecto es `1`.

## Returns

Un `data.frame` con los datos limpios de la enfermedad o evento.

Función que limpia los datos seleccionados de una enfermedad o evento provenientes de la fuente SIVIGILA.

## Examples

```r
data(dengue2020)
limpiar_data_sivigila(data_event = dengue2020)
```
