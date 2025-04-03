# Importar las proyecciones DANE del año 2005 hasta el 2035

```r
import_pob_proyecciones(year, ruta_dir = NULL, cache = FALSE)
```

## Arguments

- `year`: Un `numeric` (numérico) con el año de las proyecciones poblacionales DANE que desea importar.
- `ruta_dir`: Un `character` (cadena de caracteres) que especifica la ruta del directorio donde se almacenarán la población a riesgo o las proyecciones poblacionales DANE. Su valor por defecto es `NULL`.
- `cache`: Un `logical` (`TRUE` o `FALSE`) que indica si la población a riesgo o las proyecciones poblacionales DANE descargadas deben ser almacenados en caché. Su valor por defecto es `FALSE`.

## Returns

Un `data.frame` con las proyecciones poblacionales DANE.

Función que importa las proyecciones poblacionales DANE desde el año 2005 hasta el 2035.

## Examples

```r
import_pob_proyecciones(year = 2020, ruta_dir = tempdir())
if (interactive()) {
  import_pob_proyecciones(year = 2020, cache = TRUE)
  }
```
