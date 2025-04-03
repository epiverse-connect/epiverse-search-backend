# Match and merge geospatial and demographic datasets

```r
merge_geo_demographic(demographic_dataset, simplified = TRUE)
```

## Arguments

- `demographic_dataset`: character with the demographic dataset name. Please use `list_datasets("demographic", "EN")` or `list_datasets("demographic", "ES")` to check available datasets.
- `simplified`: logical for indicating if the downloaded spatial data should be a simplified version of the geometries. Simplified versions are lighter but less precise, and are recommended for easier applications like plots. Default is `TRUE`.

## Returns

`data.frame` object with the merged data.

This function adds the key information of a demographic dataset to a geospatial dataset based on the spatial aggregation level. Since the smallest level of spatial aggregation present in the demographic datasets is municipality, this function can only merge with geospatial datasets that present municipality or department level.

## Examples

```r
merged <- merge_geo_demographic("DANE_CNPVV_2018_9VD", TRUE)
head(merged)
```
