# Aggregate multiple `<epiparameter>` objects into a single `<epiparameter>`

object.

```r
## S3 method for class 'multi_epiparameter'
aggregate(x, weighting = c("equal", "sample_size", "custom"), ..., weights)
```

## Arguments

- `x`: A `<multi_epiparameter>` object.
- `weighting`: A `character` string with the type of weighting to use to create the mixture distribution. Options are: `"equal"` for equal weighting across distributions, `"sample_size"` for using the sample size in each `<epiparameter>` object to weight the distribution (the sample sizes are normalised), or `"custom"` allows a vector of weights to be passed to the `weights` argument for a custom weighting.
- `...`: dots Not used, will warn if extra arguments are passed to function.
- `weights`: A `numeric` vector of equal length the number of `<epiparameter>` objects passed to `x`. `weights` is only required if `weighting = "custom"`.

## Returns

An `<epiparameter>` object

Combine a list of `<epiparameter>` objects into a single `<epiparameter>`

with a mixture distribution [see `distributional::dist_mixture()`].

The aggregated `<epiparameter>` returned from `aggregate()` can then be used with the `density()`, `cdf()`, `quantile()` and `generate()` methods for the combined distributions.

## Details

The `aggregate()` method requires that all `<epiparameter>` objects are parameterised with `<distribution>` objects (from the `distributional`

package). This means that unparameterised (see `is_parameterised()`) or discretised (see `discretise()`) distributions cannot be aggregated and the function will error.

## Examples

```r
ebola_si <- epiparameter_db(epi_name = "serial interval", disease = "ebola")
aggregate(ebola_si)
```
