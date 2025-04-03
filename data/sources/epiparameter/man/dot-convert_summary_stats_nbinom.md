# Convert summary statistics to parameters of the negative binomial distribution

```r
.convert_summary_stats_nbinom(...)
```

## Arguments

- `...`: <`dynamic-dots`> `Numeric` named summary statistics used to convert to parameter(s). An example is the `mean`
    
    and `sd` summary statistics for the lognormal (`lnorm`) distribution.

## Returns

A list of two elements, the probability and dispersion parameters.

Convert summary statistics of the negative binomial distribution the parameters (`prob`) and (`dispersion`) of the negative binomial distribution.
