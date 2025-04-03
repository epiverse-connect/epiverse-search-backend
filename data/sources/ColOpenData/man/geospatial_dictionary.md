# Download data dictionaries

```r
geospatial_dictionary(spatial_level, language = "ES")
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
- `language`: character with the language of the dictionary variables (`"EN"` or `"ES"`. Default is `"ES"`.

## Returns

`data.frame` object with geospatial data dictionary.

Retrieve geospatial data dictionaries to understand internal tags and named columns. Dictionaries are available in English and Spanish.

## Examples

```r
dict <- geospatial_dictionary("setu", "EN")
head(dict)
```
