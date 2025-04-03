# Convert parameter of the geometric distribution to summary statistics

```r
.convert_params_geom(...)
```

## Arguments

- `...`: <`dynamic-dots`> `Numeric` named parameter(s) used to convert to summary statistics. An example is the `meanlog` and `sdlog` parameters of the lognormal (`lnorm`) distribution.

## Returns

A list of eight elements including: mean, median, mode, variance (`var`), standard deviation (`sd`), coefficient of variation (`cv`), skewness, and excess kurtosis (`ex_kurtosis`).

Convert the probability (`prob`) of the geometric distribution to a number of summary statistics which can be calculated analytically given the geometric parameter. One exception is the median which is calculated using `stats::qgeom()` as the analytical form is not always unique.

## Details

This conversion function assumes that distribution represents the number of failures before the first success (supported for zero). This is the same form as used by base R and `distributional::dist_geometric()`.
