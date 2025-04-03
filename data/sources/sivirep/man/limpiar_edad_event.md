# Limpiar las edades de los datos de una enfermedad o evento

```r
limpiar_edad_event(data_event, col_edad = "edad")
```

## Arguments

- `data_event`: Un `data.frame` que contiene los datos de una enfermedad o evento.
- `col_edad`: Un `character` (cadena de caracteres) con el nombre de la columna que contiene las edades en los datos de la enfermedad o evento; su valor por defecto es `"edad"`.

## Returns

Un `data.frame` con los datos de una enfermedad o evento con las edades limpias.

Función que limpia y estandariza las edades de los datos de una enfermedad o evento, convirtiéndolas en años, según la clasificación del Instituto Nacional de Salud:

 * No aplica = 0
 * Años = 1
 * Meses = 2
 * Días = 3
 * Horas = 4
 * Minutos = 5

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
limpiar_edad_event(data_event = data_limpia, col_edad = "edad")
```
