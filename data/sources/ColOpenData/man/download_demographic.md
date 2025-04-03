# Download demographic dataset

```r
download_demographic(dataset)
```

## Arguments

- `dataset`: character with the demographic dataset name. Please use `list_datasets("demographic", "EN")` or `list_datasets("demographic", "ES")` to check available datasets.

## Returns

`data.frame` object with downloaded data.

This function downloads demographic datasets from the National Population and Dwelling Census (CNPV) of 2018.

## Examples

```r
house_under_15 <- download_demographic("DANE_CNPVH_2018_1HD")
head(house_under_15)
```
