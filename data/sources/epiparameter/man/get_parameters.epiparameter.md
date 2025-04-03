# Get parameters from an `<epiparameter>` object

```r
## S3 method for class 'epiparameter'
get_parameters(x, ...)

## S3 method for class 'multi_epiparameter'
get_parameters(x, ...)
```

## Arguments

- `x`: An `<epiparameter>` object.
- `...`: dots Not used, extra arguments supplied will cause a warning.

## Returns

A named vector of parameters or `NA` when the `<epiparameter>`

object is unparameterised.

Extract the parameters of the distribution stored in an `<epiparameter>`

object.

## Details

The `<epiparameter>` object can be unparameterised in which it lacks a probability distribution or parameters of a probability distribution, in this case the `get_parameters.epiparameter()` method will return `NA`.

## Examples

```r
ep <- epiparameter_db(
  disease = "COVID-19",
  epi_name = "serial interval",
  single_epiparameter = TRUE
)
get_parameters(ep)
```
