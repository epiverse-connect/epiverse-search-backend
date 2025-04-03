# Density of the Borel distribution

```r
dborel(x, mu, log = FALSE)
```

## Arguments

- `x`: A numeric vector of quantiles.
- `mu`: A non-negative number for the poisson mean.
- `log`: Logical; if TRUE, probabilities p are given as log(p).

## Returns

A numeric vector of the borel probability density.

Density of the Borel distribution

## Examples

```r
set.seed(32)
dborel(1:5, 1)
```

## Author(s)

Sebastian Funk James M. Azam
