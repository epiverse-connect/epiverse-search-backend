# Obtener el nombre de un municipio de Colombia

```r
obtener_nombre_mpio(data_geo, cod_dpto, cod_mpio)
```

## Arguments

- `data_geo`: Un `data.frame` que contiene los códigos geográficos (departamentos y municipios de Colombia).
- `cod_dpto`: Un `numeric` (numérico) o `character` (cadena de caracteres) que contiene el código del departamento.
- `cod_mpio`: Un `numeric` (numérico) o `character` (cadena de caracteres) que contiene el código del municipio.

## Returns

Un `character` (cadena de caracteres) con el nombre del municipio.

Función que obtiene el nombre de un municipio de Colombia a partir de su código geográfico.

## Examples

```r
data_geo <- import_geo_cods()
obtener_nombre_mpio(data_geo,
  cod_dpto = "05",
  cod_mpio = "001"
)
obtener_nombre_mpio(data_geo,
  cod_dpto = 05,
  cod_mpio = 001
)
obtener_nombre_mpio(data_geo,
  cod_dpto = 5,
  cod_mpio = 1
)
```
