# Convert the parameter(s) of a distribution to summary statistics

```r
convert_params_to_summary_stats(x, ...)

## S3 method for class 'character'
convert_params_to_summary_stats(
  x = c("lnorm", "gamma", "weibull", "nbinom", "geom"),
  ...
)

## S3 method for class 'epiparameter'
convert_params_to_summary_stats(x, ...)
```

## Arguments

- `x`: An object.
- `...`: <`dynamic-dots`> `Numeric` named parameter(s) used to convert to summary statistics. An example is the `meanlog` and `sdlog` parameters of the lognormal (`lnorm`) distribution.

## Returns

A list of eight elements including: mean, median, mode, variance (`var`), standard deviation (`sd`), coefficient of variation (`cv`), skewness, and excess kurtosis (`ex_kurtosis`).

Convert the parameters for a range of distributions to a number of summary statistics. All summary statistics are calculated analytically given the parameters.

## Details

The distribution names and parameter names follow the style of distributions in , for example the lognormal distribution is `lnorm`, and its parameters are `meanlog` and `sdlog`.

## Examples

```r
# example using characters
convert_params_to_summary_stats("lnorm", meanlog = 1, sdlog = 2)
convert_params_to_summary_stats("gamma", shape = 1, scale = 1)
convert_params_to_summary_stats("nbinom", prob = 0.5, dispersion = 2)

# example using <epiparameter>
epiparameter <- epiparameter_db(single_epiparameter = TRUE)
convert_params_to_summary_stats(epiparameter)

# example using <epiparameter> and specifying parameters
epiparameter <- epiparameter_db(
  disease = "Influenza",
  author = "Virlogeux",
  subset = prob_dist == "weibull"
)
convert_params_to_summary_stats(epiparameter[[2]], shape = 1, scale = 1)
```

## See Also

`convert_summary_stats_to_params()`
