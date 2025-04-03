# Discretises a continuous distribution in an `<epiparameter>` object

```r
discretise(x, ...)

discretize(x, ...)

## S3 method for class 'epiparameter'
discretise(x, ...)

## Default S3 method:
discretise(x, ...)
```

## Arguments

- `x`: An `<epiparameter>` object.
- `...`: dots Extra arguments to be passed to the method.

## Returns

An `<epiparameter>` object.

Discretises a continuous distribution in an `<epiparameter>` object

## Details

Converts the S3 distribution object in an `<epiparameter>` from continuous (using an object from the `{distributional}` package) to a discretised distribution (using an object from the `{distcrete}` package).

## Examples

```r
ebola_incubation <- epiparameter(
  disease = "ebola",
  epi_name = "incubation_period",
  prob_distribution = create_prob_distribution(
    prob_distribution = "gamma",
    prob_distribution_params = c(shape = 1, scale = 1)
  )
)
discretise(ebola_incubation)
```
