# Convert summary statistics to parameters of the geometric distribution

```r
.convert_summary_stats_geom(...)
```

## Arguments

- `...`: <`dynamic-dots`> `Numeric` named summary statistics used to convert to parameter(s). An example is the `mean`
    
    and `sd` summary statistics for the lognormal (`lnorm`) distribution.

## Returns

A list of one element, the probability parameter.

Convert summary statistics of the geometric distribution the parameter (`prob`) of the geometric distribution.

## Details

This conversion function assumes that distribution represents the number of failures before the first success (supported for zero). This is the same form as used by base R and `distributional::dist_geometric()`.
