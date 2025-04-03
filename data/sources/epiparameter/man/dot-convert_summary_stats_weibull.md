# Convert summary statistics to parameters of the Weibull distribution

```r
.convert_summary_stats_weibull(...)
```

## Arguments

- `...`: <`dynamic-dots`> `Numeric` named summary statistics used to convert to parameter(s). An example is the `mean`
    
    and `sd` summary statistics for the lognormal (`lnorm`) distribution.

## Returns

A list of two elements, the shape and scale.

Convert summary statistics input into the shape and scale parameters of the Weibull distribution.
