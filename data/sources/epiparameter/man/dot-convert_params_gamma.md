# Convert parameters of the gamma distribution to summary statistics

```r
.convert_params_gamma(...)
```

## Arguments

- `...`: <`dynamic-dots`> `Numeric` named parameter(s) used to convert to summary statistics. An example is the `meanlog` and `sdlog` parameters of the lognormal (`lnorm`) distribution.

## Returns

A list of eight elements including: mean, median, mode, variance (`var`), standard deviation (`sd`), coefficient of variation (`cv`), skewness, and excess kurtosis (`ex_kurtosis`).

Convert the shape and scale parameters of the gamma distribution to a number of summary statistics which can be calculated analytically given the gamma parameters. One exception is the median which is calculated using `qgamma()` as no analytical form is available.
