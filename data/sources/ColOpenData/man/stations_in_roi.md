# Stations in region of interest

```r
stations_in_roi(geometry)
```

## Arguments

- `geometry`: `sf` object containing the geometry for a given ROI. The geometry can be either a `POLYGON` or `MULTIPOLYGON`.

## Returns

`data.frame` object with the stations contained inside the consulted geometry.

Download and filter climate stations contained inside a region of interest (ROI).

## Examples

```r
lat <- c(5.166278, 5.166278, 4.982247, 4.982247, 5.166278)
lon <- c(-75.678072, -75.327859, -75.327859, -75.678072, -75.678072)
polygon <- sf::st_polygon(x = list(cbind(lon, lat)))
geometry <- sf::st_sfc(polygon)
roi <- sf::st_as_sf(geometry)
stations <- stations_in_roi(roi)
head(stations)
```
