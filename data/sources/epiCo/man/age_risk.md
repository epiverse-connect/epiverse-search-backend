# Returns the specific rates associated with being infected given age and sex

```r
age_risk(age, population_pyramid, sex = NULL, plot = FALSE)
```

## Arguments

- `age`: A vector with the ages of cases in years from 0 to 100 years
- `population_pyramid`: A dataframe with the count of individuals with the columns age, population and sex
- `sex`: A vector with the sex of cases 'F' and 'M'. The default value is NULL
- `plot`: A boolean for displaying a plot. The default value is FALSE

## Returns

A dataframe with the proportion or total count of individuals

Function that returns the specific rates of being infected given age and sex

## Examples

```r
pop_pyramid <- population_pyramid("15001", 2015,
  sex = TRUE, total = TRUE,
  plot = FALSE
)
ages <- round(runif(150, 0, 100))
sex <- c(rep("M", 70), rep("F", 80))
age_risk(
  age = ages, sex = sex, population_pyramid = pop_pyramid,
  plot = TRUE
)
```
