# Filtrar por departamentos y municipios

```r
geo_filtro(data_event, dpto = NULL, mpio = NULL)
```

## Arguments

- `data_event`: Un `data.frame` con los datos de una enfermedad o evento.
- `dpto`: Un `character` (cadena de caracteres) o `numeric` (numérico) que contiene el nombre o código del departamento; valor por defecto `NULL`.
- `mpio`: Un `character` (cadena de caracteres) o `numeric` (numérico) que contiene el nombre o código del municipio; su valor por defecto es `NULL`.

## Returns

Un `data.frame` con los datos filtrados con la enfermedad, departamentos y municipios seleccionados.

Función que filtra los datos de una enfermedad o evento por departamentos y municipios.

## Examples

```r
data(dengue2020)
data_limpia <- limpiar_data_sivigila(data_event = dengue2020)
geo_filtro(data_event = data_limpia, dpto = "ANTIOQUIA")
geo_filtro(data_event = data_limpia, dpto = "ANTIOQUIA", mpio = "MEDELLIN")
geo_filtro(data_event = data_limpia, dpto = "05")
geo_filtro(data_event = data_limpia, dpto = "05", mpio = "05001")
geo_filtro(data_event = data_limpia, dpto = 05, mpio = 05001)
geo_filtro(data_event = data_limpia, dpto = 05, mpio = 001)
geo_filtro(data_event = data_limpia, dpto = "bogota dc", mpio = "bogota dc")
```
