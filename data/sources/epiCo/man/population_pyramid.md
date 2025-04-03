# Returns the population pyramid of the consulted region

```r
population_pyramid(
  divipola_code,
  year,
  sex = TRUE,
  range = 5,
  total = TRUE,
  plot = FALSE
)
```

## Arguments

- `divipola_code`: A code from the divipola table representing a department or municipality. To obtain values at the national level, code '0' is used
- `year`: A numeric input for the year of interest
- `sex`: A boolean to consult data disaggregated by sex. The default value is TRUE
- `range`: A numeric value from 1 to 100 for the age range to use. The default value is 5
- `total`: A boolean for returning the total number rather than the proportion of the country's population. The default value is TRUE
- `plot`: A boolean for displaying a plot. The default value is TRUE

## Returns

A dataframe with the proportion or total count of individuals

Function that returns the population pyramid of the municipality or department of a specific year

## Examples

```r
population_pyramid("15001", 2015, sex = TRUE, total = TRUE, plot = TRUE)
```
