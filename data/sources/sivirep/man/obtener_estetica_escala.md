# Obtener la estética de una escala para un gráfico de `sivirep`

```r
obtener_estetica_escala(
  escala = 0,
  nombre,
  etiquetas = NULL,
  ajustar_texto = FALSE
)
```

## Arguments

- `escala`: Un `numeric` (numérico) que indica la cantidad de valores que contiene la escala.
- `nombre`: Un `character` (cadena de caracteres) que contiene el nombre de la escala.
- `etiquetas`: Un `character` (cadena de caracteres) que contiene las etiquetas de la escala.

## Returns

Un objeto `scale_fill_manual` de `ggplot2`.

Función que genera la estética de una escala para un gráfico de `sivirep`.
