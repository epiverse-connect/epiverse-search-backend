# Aggregate climate data for different frequencies

```r
aggregate_climate(climate_data, frequency)
```

## Arguments

- `climate_data`: `data.frame` obtained from download functions. Only observations under the same tag can be aggregated.
- `frequency`: character with the aggregation frequency: (`"day"`, `"month"` or `"year"`).

## Returns

`data.frame` object with the aggregated data.

Aggregate time series downloaded climate data to day, month or year. Only observations under the tags `TSSM_CON`, `TMN_CON`, `TMX_CON`, `PTPM_CON`, and `BSHG_CON` can be aggregated, since are the ones where methodology for aggregation is explicitly provided by the source.

## Examples

```r
lat <- c(4.172817, 4.172817, 4.136050, 4.136050, 4.172817)
lon <- c(-74.749121, -74.686169, -74.686169, -74.749121, -74.749121)
polygon <- sf::st_polygon(x = list(cbind(lon, lat)))
geometry <- sf::st_sfc(polygon)
roi <- sf::st_as_sf(geometry)
ptpm <- download_climate_geom(roi, "2022-11-01", "2022-12-31", "PTPM_CON")
monthly_ptpm <- aggregate_climate(ptpm, "month")
head(monthly_ptpm)
```
