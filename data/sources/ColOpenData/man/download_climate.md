# Download climate from named geometry (municipality or department)

```r
download_climate(code, start_date, end_date, tag)
```

## Arguments

- `code`: character with the DIVIPOLA code for the area (2 digits for departments and 5 digits for municipalities).
- `start_date`: character with the first date to consult in the format `"YYYY-MM-DD"`. (First available date is `"1920-01-01"`).
- `end_date`: character with the last date to consult in the format `"YYYY-MM-DD"`. (Last available date is `"2023-05-31"`).
- `tag`: character containing climate tag to consult. Please use `cliamte_tags()` to check IDEAM tags.

## Returns

`data.frame` object with observations from the stations in the area.

Download climate data from stations contained in a municipality or department. This data is retrieved from local meteorological stations provided by IDEAM.

## Examples

```r
ptpm <- download_climate("73148", "2021-11-14", "2021-11-20", "PTPM_CON")
head(ptpm)
```
