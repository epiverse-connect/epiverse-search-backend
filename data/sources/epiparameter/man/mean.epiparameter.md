# Mean method for `<epiparameter>` class

```r
## S3 method for class 'epiparameter'
mean(x, ...)
```

## Arguments

- `x`: An `<epiparameter>` object.
- `...`: dots Not used, extra arguments supplied will cause a warning.

## Returns

A `numeric` mean of a distribution or `NA`.

Mean method for `<epiparameter>` class

## Examples

```r
ep <- epiparameter_db(
  disease = "COVID-19",
  epi_name = "incubation period",
  single_epiparameter = TRUE
)
mean(ep)
```
