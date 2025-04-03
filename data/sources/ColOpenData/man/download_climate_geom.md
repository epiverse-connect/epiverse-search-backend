# Download climate data from geometry

```r
download_climate_geom(geometry, start_date, end_date, tag)
```

## Arguments

- `geometry`: `sf` object containing the geometry for a given ROI. The geometry can be either a `POLYGON` or `MULTIPOLYGON`.
- `start_date`: character with the first date to consult in the format `"YYYY-MM-DD"`. (First available date is `"1920-01-01"`).
- `end_date`: character with the last date to consult in the format `"YYYY-MM-DD"`. (Last available date is `"2023-05-31"`).
- `tag`: character containing climate tag to consult.

## Returns

`data.frame` object with observations from the stations in the area.

Download climate data from stations contained in a Region of Interest (ROI/geometry). This data is retrieved from local meteorological stations provided by IDEAM.

## Examples

```r
lat <- c(4.172817, 4.172817, 4.136050, 4.136050, 4.172817)
lon <- c(-74.749121, -74.686169, -74.686169, -74.749121, -74.749121)
polygon <- sf::st_polygon(x = list(cbind(lon, lat)))
geometry <- sf::st_sfc(polygon)
roi <- sf::st_as_sf(geometry)
ptpm <- download_climate_geom(roi, "2022-11-14", "2022-11-20", "PTPM_CON")
head(ptpm)
```
