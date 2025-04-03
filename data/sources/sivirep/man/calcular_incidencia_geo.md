# Calcular incidencia según distribución geográfica

```r
calcular_incidencia_geo(
  data_incidencia = NULL,
  cache = FALSE,
  ruta_dir = NULL,
  data_agrupada,
  poblacion = NULL,
  year = NULL
)
```

## Arguments

- `data_incidencia`: Un `data.frame` que contiene las proyecciones poblacionales del DANE; su valor por defecto es `NULL`.
- `cache`: Un `logical` (`TRUE` o `FALSE`) que indica si la población a riesgo o las proyecciones poblacionales DANE descargadas deben ser almacenados en caché. Su valor por defecto es `FALSE`.
- `ruta_dir`: Un `character` (cadena de caracteres) que especifica la ruta del directorio donde se almacenarán la población a riesgo o las proyecciones poblacionales DANE. Su valor por defecto es `NULL`.
- `data_agrupada`: Un `data.frame` que contiene los datos de la enfermedad agrupados por departamento o municipio y número de casos.
- `poblacion`: Un `character` (cadena de caracteres) con el tipo de población para calcular la incidencia. Puede ser `"riesgo"` para la población a riesgo o `"proyecciones"` para las proyecciones poblacionales DANE; su valor por defecto es `NULL`.
- `year`: Un `numeric` (numérico) con el año que se debe tomar en la población a riesgo o en las proyecciones poblacionales DANE; su valor por defecto es `NULL`.

## Returns

Un `data.frame` con el cálculo de la incidencia para todos los departamentos de Colombia o los municipios de un departamento.

Función que calcula la incidencia de una enfermedad o evento para todos los departamentos de Colombia o los municipios de un departamento.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
data_agrupada_mpios <- agrupar_mpio(data_limpia, dpto = "Antioquia")
# Cálculo de la incidencia con población a riesgo por departamento
if (interactive()) {
  calcular_incidencia_geo(
    poblacion = "riesgo",
    data_agrupada = data_agrupada_mpios,
    year = 2020,
    cache = TRUE
  )
}
data_agrupada_dptos <- agrupar_dpto(data_limpia)
# Cálculo de la incidencia con proyecciones poblacionales para Colombia
calcular_incidencia_geo(
  poblacion = "proyecciones",
  data_agrupada = data_agrupada_dptos,
  year = 2020,
  ruta_dir = tempdir()
)
```
