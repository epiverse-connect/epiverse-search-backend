# Download population projections

```r
download_pop_projections(
  spatial_level,
  start_year,
  end_year,
  include_sex = FALSE,
  include_ethnic = FALSE
)
```

## Arguments

- `spatial_level`: character with the spatial level to be consulted. Can be either `"national"`, `"department"` or `"municipality"`.
- `start_year`: numeric with the start year to be consulted.
- `end_year`: numeric with the end year to be consulted.
- `include_sex`: logical for including (or not) division by sex. Default is `FALSE`.
- `include_ethnic`: logical for including (or not) division by ethnic group (only available for `"municipality"`). Default is `FALSE`.

## Returns

`data.frame` object with downloaded data.

This function downloads population projections and back projections taken from the National Population and Dwelling Census of 2018 (CNPV), adjusted after COVID-19. Available years are different for each spatial level:

 * `"national"`: 1950 - 2070.
 * `"national"` with sex: 1985 - 2050.
 * `"department"`: 1985 - 2050.
 * `"department"` with sex: 1985 - 2050.
 * `"municipality"`: 1985 - 2035.
 * `"municipality"` with sex: 1985 - 2035.
 * `"municipality"` with sex and ethnic groups: 2018 - 2035.

## Examples

```r
pop_proj <- download_pop_projections("national", 2020, 2030)
head(pop_proj)
```
