# Cumulative distribution function of the poisson-Weibull compound distribution

```r
ppoisweibull(q, shape, scale)
```

## Arguments

- `q`: A `number` for the quantile of the distribution.
- `shape`: A `number` for the shape parameter of the distribution.
- `scale`: A `number` for the scale parameter of the distribution.

## Returns

A `numeric` vector of the distribution function.

Cumulative distribution function of the poisson-Weibull compound distribution

## Details

The function is vectorised so a vector of quantiles can be input and the output will have an equal length.

## Examples

```r
ppoisweibull(q = 10, shape = 1, scale = 2)
ppoisweibull(q = 1:10, shape = 1, scale = 2)
```
