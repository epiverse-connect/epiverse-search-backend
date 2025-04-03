# Aggregate cases in `<epichains>` objects by "generation" or "time", if present

```r
## S3 method for class 'epichains'
aggregate(x, by = c("time", "generation"), ...)
```

## Arguments

- `x`: An `<epichains>` object.
- `by`: The variable to aggregate by; A character string with options "time" and "generation".
- `...`: Not used.

## Returns

A `<data.frame>` object of cases by `by`.

This function provides a quick way to create a time series of cases over generation or time (if `generation_time` was specified) from simulated `<epichains>` objects.

## Examples

```r
set.seed(32)
chains <- simulate_chains(
  n_chains = 10,
  statistic = "size",
  offspring_dist = rpois,
  stat_threshold = 10,
  generation_time = function(n) rep(3, n),
  lambda = 2
)
chains

# Aggregate cases per time
cases_per_time <- aggregate(chains, by = "time")
head(cases_per_time)

# Aggregate cases per generation
cases_per_gen <- aggregate(chains, by = "generation")
head(cases_per_gen)
```

## Author(s)

James M. Azam
