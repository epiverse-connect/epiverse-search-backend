# Format method for `<epiparameter>` class

```r
## S3 method for class 'epiparameter'
format(x, ...)
```

## Arguments

- `x`: An `<epiparameter>` object.
- `...`: dots Extra arguments to be passed to the method.

## Returns

Invisibly returns an `<epiparameter>`. Called for printing side-effects.

Format method for `<epiparameter>` class

## Examples

```r
epiparameter <- epiparameter(
  disease = "ebola",
  epi_name = "incubation_period",
  prob_distribution = create_prob_distribution(
    prob_distribution = "gamma",
    prob_distribution_params = c(shape = 1, scale = 1)
  )
)
format(epiparameter)
```
