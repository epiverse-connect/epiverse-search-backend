# Obtener valor del archivo de configuración

```r
obtener_val_config(llave)
```

## Arguments

- `llave`: Un `character` (cadena de caracteres) con el nombre de la llave que se encuentra en el archivo de configuración del paquete.

## Returns

Un `character` (cadena de caracteres) con el valor de la llave del archivo de configuración del paquete.

Función que obtiene el valor de una llave del archivo de configuración.

## Examples

```r
obtener_val_config("request_timeout")
```
