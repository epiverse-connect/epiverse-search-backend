# Generar tabla con la incidencia

```r
plot_tabla_incidencia_geo(data_agrupada, col_geo = NULL)
```

## Arguments

- `data_agrupada`: Un `data.frame` que contiene los datos de la enfermedad o evento agrupados por departamento o municipio.
- `col_geo`: Un `character` (cadena de caracteres) con el nombre de la columna que contiene los nombres de los departamentos o municipios en los datos agrupados de la enfermedad o evento; su valor por defecto es `NULL`.

## Returns

Una `kable` (tabla gráfica) con la incidencia según distribución geográfica.

Función que genera la tabla con la incidencia según la distribución geográfica.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
data_agrupada <- agrupar_mpio(data_limpia, dpto = "Antioquia")
incidencia_mpios <- calcular_incidencia_geo(
  data_agrupada =
    data_agrupada,
  ruta_dir = tempdir()
)
plot_tabla_incidencia_geo(
  data_agrupada = incidencia_mpios$data_incidencia,
  col_geo = "municipio_ocurrencia"
)
```
