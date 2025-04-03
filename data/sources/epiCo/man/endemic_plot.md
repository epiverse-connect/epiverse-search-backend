# Creates the endemic channel plot

```r
endemic_plot(channel_data, method, outlier_years, outliers_handling)
```

## Arguments

- `channel_data`: Data frame with the central tendency, upper limit, lower limit, and observations to plot
- `method`: A string with the method used in the endemic channel calculation
- `outlier_years`: A numeric vector with the outlier years
- `outliers_handling`: A string with the handling decision regarding outlier years

## Returns

The ggplot object with the endemic channel plot

Function that creates the endemic channel plot
