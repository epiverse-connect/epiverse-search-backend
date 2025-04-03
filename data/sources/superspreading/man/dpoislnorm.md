# Density of the poisson-lognormal compound distribution

```r
dpoislnorm(x, meanlog, sdlog)
```

## Arguments

- `x`: A `number` for the quantile of the distribution.
- `meanlog`: A `number` for the mean of the distribution on the log scale.
- `sdlog`: A `number` for the standard deviation of the distribution on the log scale.

## Returns

A `numeric` vector of the density of the poisson-lognormal distribution.

Density of the poisson-lognormal compound distribution

## Details

The function is vectorised so a vector of quantiles can be input and the output will have an equal length.

## Examples

```r
dpoislnorm(x = 10, meanlog = 1, sdlog = 2)
dpoislnorm(x = 1:10, meanlog = 1, sdlog = 2)
```
