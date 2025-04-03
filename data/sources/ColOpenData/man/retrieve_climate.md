# Retrieve climate table file from one station

```r
retrieve_climate(dataset_path, start_date, end_date)
```

## Arguments

- `dataset_path`: character path to the climate dataset on server.
- `start_date`: character with the first date to consult in the format `"YYYY-MM-DD"`. (First available date is `"1920-01-01"`).
- `end_date`: character with the last date to consult in the format `"YYYY-MM-DD"` (Last available date is `"2023-05-31"`).

## Returns

`data.frame` object with downloaded data filtered for requested dates.

Retrieve climate table file from one station
