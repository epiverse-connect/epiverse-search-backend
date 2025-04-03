# Convert summary statistics to parameters of the lognormal distribution

```r
.convert_summary_stats_lnorm(...)
```

## Arguments

- `...`: <`dynamic-dots`> `Numeric` named summary statistics used to convert to parameter(s). An example is the `mean`
    
    and `sd` summary statistics for the lognormal (`lnorm`) distribution.

## Returns

A list of two elements: meanlog and sdlog

Convert the summary statistics input into the meanlog and sdlog parameters of the lognormal distribution.
