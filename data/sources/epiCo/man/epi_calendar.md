# Get the epidemiological calendar of a consulted year.

```r
epi_calendar(year, jan_days = 4)
```

## Arguments

- `year`: A numeric value for the year of interest.
- `jan_days`: Number of January days that the first epidemiological week must contains.

## Returns

A character array with the starting dates of the epidemiological weeks of the given year.

Function that returns the starting date of the epidemiological weeks in a year of interest.

## Examples

```r
epi_calendar(2016)
```
