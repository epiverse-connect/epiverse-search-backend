# Check if distribution in `<epiparameter>` is truncated

```r
is_truncated(x)
```

## Arguments

- `x`: An `<epiparameter>` object.

## Returns

A boolean `logical`.

Check if distribution in `<epiparameter>` is truncated

## Details

The `<epiparameter>` class can hold probability distribution objects from the `{distributional}` package or the `{distcrete}` package, however, only distribution objects from `{distributional}` can be truncated. If a `<epiparameter>` object has a `<distcrete>` object `is_truncated` will return `FALSE` by default.

## Examples

```r
ep <- epiparameter(
  disease = "ebola",
  epi_name = "incubation_period",
  prob_distribution = create_prob_distribution(
    prob_distribution = "lnorm",
    prob_distribution_params = c(meanlog = 1, sdlog = 1)
  )
)
is_truncated(ep)

ep <- epiparameter(
  disease = "ebola",
  epi_name = "incubation_period",
  prob_distribution = create_prob_distribution(
    prob_distribution = "lnorm",
    prob_distribution_params = c(meanlog = 1, sdlog = 1),
    truncation = 10
  )
)
is_truncated(ep)
```
