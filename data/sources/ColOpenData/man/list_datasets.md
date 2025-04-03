# Download list of available datasets

```r
list_datasets(module = "all", language = "ES")
```

## Arguments

- `module`: character with module to be consulted (`"demographic"`, `"geospatial"` or `"climate"`). Default is `"all"`.
- `language`: character with the language of dataset details (`"EN"`
    
    or `"ES"`. Default is `"ES"`.

## Returns

`data.frame` object with the available datasets.

List all available datasets by name, including group, source, year, level, category and description.

## Examples

```r
list <- list_datasets("geospatial", "EN")
head(list)
```
