# Check object is an `<epiparameter>`

```r
is_epiparameter(x)
```

## Arguments

- `x`: An object.

## Returns

A boolean logical, `TRUE` if the object is an `<epiparameter>`

and `FALSE` if not.

Check object is an `<epiparameter>`

## Examples

```r
ep <- epiparameter(
  disease = "ebola",
  epi_name = "serial_interval",
  prob_distribution = create_prob_distribution(
    prob_distribution = "gamma",
    prob_distribution_params = c(shape = 1, scale = 1)
  )
)

is_epiparameter(ep)

false_ep <- list(
  disease = "ebola",
  epi_name = "serial_interval",
  prob_distribution = "gamma",
  prob_distribution_params = c(shape = 1, scale = 1)
)

is_epiparameter(false_ep)
```
