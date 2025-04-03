# Importar la población a riesgo de un evento o enfermedad

```r
import_pob_riesgo(event, year, ruta_dir = NULL, cache = FALSE)
```

## Arguments

- `event`: Un `character` (cadena de caracteres) o un `numeric` (numérico) con el nombre o código de la enfermedad o evento.
- `year`: Un `numeric` (numérico) con el año deseado de la población a riesgo.
- `ruta_dir`: Un `character` (cadena de caracteres) que especifica la ruta del directorio donde se almacenarán la población a riesgo o las proyecciones poblacionales DANE. Su valor por defecto es `NULL`.
- `cache`: Un `logical` (`TRUE` o `FALSE`) que indica si la población a riesgo o las proyecciones poblacionales DANE descargadas deben ser almacenados en caché. Su valor por defecto es `FALSE`.

## Returns

Un `data.frame` con la población a riesgo de un año específico.

Función que importa la población a riesgo de un evento o enfermedad para un año específico.

## Examples

```r
import_pob_riesgo(event = "Dengue", year = 2020, ruta_dir = tempdir())
if (interactive()) {
  import_pob_riesgo(event = "Dengue", year = 2020, cache = TRUE)
  }
```
