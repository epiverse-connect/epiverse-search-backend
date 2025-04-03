# Importar el Shapefile del mapa de Colombia

```r
import_shape_map(ruta_dir = NULL, cache = FALSE)
```

## Arguments

- `ruta_dir`: Un `character` (cadena de caracteres) que contiene la ruta del directorio donde se almacenará el Shapefile del mapa de Colombia. Su valor por defecto es `NULL`.
- `cache`: Un `logical` (`TRUE` o `FALSE`) que indica si el Shapefile del mapa de Colombia debe ser almacenado en caché. Su valor por defecto es `FALSE`.

## Returns

Un objeto `sf` que contiene los elementos del Shapefile del mapa.

Función que importa el Shapefile del mapa de Colombia.
