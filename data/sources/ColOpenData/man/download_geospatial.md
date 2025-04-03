# Download geospatial dataset

```r
download_geospatial(
  spatial_level,
  simplified = TRUE,
  include_geom = TRUE,
  include_cnpv = TRUE
)
```

## Arguments

- `spatial_level`: character with the spatial level to be consulted:
    
     * `"DPTO"` or `"department"`: Department.
     * `"MPIO"` or `"municipality"`: Municipality.
     * `"MPIOCL"` or `"municipality_class"`: Municipality including class.
     * `"SETU"` or `"urban_sector"`: Urban Sector.
     * `"SETR"` or `"rural_sector"`: Rural Sector.
     * `"SECU"` or `"urban_section"`: Urban Section.
     * `"SECR"` or `"rural_section"`: Rural Section.
     * `"ZU"` or `"urban_zone"`: Urban Zone.
     * `"MZN"` or `"block"`: Block.
- `simplified`: logical for indicating if the downloaded spatial data should be a simplified version of the geometries. Simplified versions are lighter but less precise, and are only recommended for easier applications like plots. Default is `TRUE`.
- `include_geom`: logical for including (or not) the spatial geometry. Default is `TRUE`. If `TRUE`, the function will return an `"sf"` `data.frame`.
- `include_cnpv`: logical for including (or not) CNPV demographic and socioeconomic information. Default is `TRUE`.

## Returns

`data.frame` object with downloaded data.

This function downloads geospatial datasets from the National Geostatistical Framework at different levels of spatial aggregation. These datasets include a summarized version of the National Population and Dwelling Census (CNPV) with demographic and socioeconomic information for each spatial unit.

## Examples

```r
departments <- download_geospatial("department")
head(departments)
```
