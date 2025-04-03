# Obtener información geográfica de los datos de la enfermedad o evento

```r
obtener_info_depts(dpto = NULL, mpio = NULL)
```

## Arguments

- `dpto`: Un `character` (cadena de caracteres) o `numeric` (numérico) que contiene el nombre o código del departamento; su valor por defecto es `NULL`.
- `mpio`: Un `character` (cadena de caracteres) o `numeric` (numérico) que contiene el nombre o código del municipio; su valor por defecto es `NULL`.

## Returns

Un `data.frame` con la información geográfica de los datos de la enfermedad o evento.

Función que obtiene la información geográfica de los datos de la enfermedad o evento.

## Examples

```r
obtener_info_depts(dpto = "ANTIOQUIA")
obtener_info_depts(dpto = "ANTIOQUIA", mpio = "MEDELLIN")
obtener_info_depts(dpto = "05")
obtener_info_depts(dpto = "05", mpio = "05001")
obtener_info_depts(dpto = 05, mpio = 05001)
obtener_info_depts(dpto = 05, mpio = 001)
obtener_info_depts(dpto = "bogota dc", mpio = "bogota dc")
```
