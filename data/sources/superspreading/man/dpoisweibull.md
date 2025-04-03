# Density of the poisson-Weibull compound distribution

```r
dpoisweibull(x, shape, scale)
```

## Arguments

- `x`: A `number` for the quantile of the distribution.
- `shape`: A `number` for the shape parameter of the distribution.
- `scale`: A `number` for the scale parameter of the distribution.

## Returns

A `numeric` vector of the density of the poisson-Weibull distribution.

Density of the poisson-Weibull compound distribution

## Details

The function is vectorised so a vector of quantiles can be input and the output will have an equal length.

## Examples

```r
dpoisweibull(x = 10, shape = 1, scale = 2)
dpoisweibull(x = 1:10, shape = 1, scale = 2)
```
