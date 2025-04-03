# Get new infections over model time

```r
new_infections(data, compartments_from_susceptible = NULL, by_group = TRUE)
```

## Arguments

- `data`: A table of model output, typically the output of `model_default()` or similar functions.
- `compartments_from_susceptible`: An optional argument, for a character vector of the names of model compartments into which individuals transition from the "susceptible" compartment, and which are not related to infection. A common example is a compartment for "vaccinated" individuals who are no longer susceptible, but who should also not be counted as infected.
- `by_group`: A logical representing whether the epidemic size should be returned by demographic group, or whether a single population-wide value is returned.

## Returns

A table with the same columns as `data`, but with the additional variable under `compartment`, "new_infections", resulting in additional rows.

Get new infections over model time

## Examples

```r
# create a population
uk_population <- population(
  contact_matrix = matrix(1),
  demography_vector = 67e6,
  initial_conditions = matrix(
    c(0.9999, 0.0001, 0, 0, 0),
    nrow = 1, ncol = 5L
  )
)


# run epidemic simulation with no vaccination or intervention
data <- model_default(
  population = uk_population,
  time_end = 200,
  increment = 1
)

new_infections(data)
```
