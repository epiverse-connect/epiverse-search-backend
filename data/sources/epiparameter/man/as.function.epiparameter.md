# `as.function()` method for `<epiparameter>` class

```r
## S3 method for class 'epiparameter'
as.function(x, func_type = c("density", "cdf", "generate", "quantile"), ...)
```

## Arguments

- `x`: An `<epiparameter>` object.
- `func_type`: A single `character` string specifying which distribution to convert `<epiparameter>` object into. Default is `"density"`. Other options are `"cdf"`, `"generate"`, or `"quantile"`.
- `...`: dots Extra arguments to be passed to the method.

## Returns

A function object.

Converts an `<epiparameter>` object to a distribution function (see epiparameter_distribution_functions ), either probability density/mass function, (`density`), cumulative distribution function (`cdf`), random number generator (`generate`), or quantile (`quantile`).

## Details

The function returned takes a single required argument `x`.

## Examples

```r
ep <- epiparameter_db(single_epiparameter = TRUE)
# by default it will convert to a density function
f <- as.function(ep)
# use function
f(10)

f <- as.function(ep, func_type = "cdf")
f(10)
```
