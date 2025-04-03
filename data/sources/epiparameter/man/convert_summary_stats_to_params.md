# Convert the summary statistics of a distribution to parameters

```r
convert_summary_stats_to_params(x, ...)

## S3 method for class 'character'
convert_summary_stats_to_params(
  x = c("lnorm", "gamma", "weibull", "nbinom", "geom"),
  ...
)

## S3 method for class 'epiparameter'
convert_summary_stats_to_params(x, ...)
```

## Arguments

- `x`: An object.
- `...`: <`dynamic-dots`> `Numeric` named summary statistics used to convert to parameter(s). An example is the `mean`
    
    and `sd` summary statistics for the lognormal (`lnorm`) distribution.

## Returns

A list of either one or two elements (depending on how many parameters the distribution has).

Convert the summary statistics for a range of distributions to the distribution's parameters. Most summary statistics are calculated analytically given the parameters. An exception is the Weibull distribution which uses a root finding numerical method.

## Details

Summary statistics should be named accordingly (case-sensitive):

 * mean: `mean`
 * median: `median`
 * mode: `mode`
 * variance: `var`
 * standard deviation: `sd`
 * coefficient of variation: `cv`
 * skewness: `skewness`
 * excess kurtosis: `ex_kurtosis`

Note : Not all combinations of summary statistics can be converted into distribution parameters. In this case the function will error stating that the parameters cannot be calculated from the given input.

The distribution names and parameter names follow the style of distributions in , for example the lognormal distribution is `lnorm`, and its parameters are `meanlog` and `sdlog`.

## Examples

```r
# examples using characters
convert_summary_stats_to_params("lnorm", mean = 1, sd = 1)
convert_summary_stats_to_params("weibull", mean = 2, var = 2)
convert_summary_stats_to_params("geom", mean = 2)

# examples using <epiparameter>
epiparameter <- epiparameter_db(single_epiparameter = TRUE)
convert_summary_stats_to_params(epiparameter)

# example using <epiparameter> and specifying summary stats
epiparameter$summary_stats <- list()
convert_summary_stats_to_params(epiparameter, mean = 10, sd = 2)
```

## See Also

`convert_params_to_summary_stats()`
