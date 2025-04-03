# Importar datos geográficos de Colombia

```r
import_geo_cods(descargar = FALSE)
```

## Arguments

- `descargar`: Un `logical` (`TRUE` o `FALSE`) que indica si los datos deben descargarse desde la API de datos abiertos de Colombia; su valor por defecto es `FALSE`.

## Returns

Un `data.frame` con los nombres y códigos de los departamentos y municipios de Colombia.

Función que importa los nombres y códigos de los departamentos y municipios de Colombia a través de una URL.

## Examples

```r
import_geo_cods(descargar = FALSE)
```
