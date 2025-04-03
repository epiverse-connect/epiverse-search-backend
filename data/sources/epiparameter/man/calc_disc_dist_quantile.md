# Calculate the quantiles of a probability distribution based on the vector of probabilities and time data (e.g. time since infection)

```r
calc_disc_dist_quantile(prob, days, quantile)
```

## Arguments

- `prob`: A `numeric` vector of probabilities.
- `days`: A `numeric` vector of days.
- `quantile`: A single `numeric` or vector of `numerics` specifying which quantiles to extract from the distribution.

## Returns

A named vector of quantiles.

This function can be used in cases where the data on a fitted distribution is not openly available and the summary statistics of the distribution are not reported so the data are scraped from the plot and the quantiles are needed in order use the `extract_param()` function.

## Examples

```r
prob <- dgamma(seq(0, 10, length.out = 21), shape = 2, scale = 2)
days <- seq(0, 10, 0.5)
quantiles <- c(0.025, 0.975)
calc_disc_dist_quantile(prob = prob, days = days, quantile = quantiles)
```
