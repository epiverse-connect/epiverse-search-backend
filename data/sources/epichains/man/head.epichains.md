# `head` and `tail` method for `<epichains>` class

```r
## S3 method for class 'epichains'
head(x, ...)

## S3 method for class 'epichains'
tail(x, ...)
```

## Arguments

- `x`: An `<epichains>` object.
- `...`: Further arguments passed to or from other methods.

## Returns

An object of class `<data.frame>`.

`head` and `tail` method for `<epichains>` class

## Details

This returns the top rows of an `<epichains>` object, starting from the first known infectors.

To view the full output, use `as.data.frame(<object_name>)`.

## Examples

```r
set.seed(32)
chains_pois_offspring <- simulate_chains(
  n_chains = 10,
  statistic = "size",
  offspring_dist = rpois,
  stat_threshold = 10,
  generation_time = function(n) rep(3, n),
  lambda = 2
)
head(chains_pois_offspring)
set.seed(32)
chains_pois_offspring <- simulate_chains(
  n_chains = 10,
  statistic = "size",
  offspring_dist = rpois,
  stat_threshold = 10,
  generation_time = function(n) rep(3, n),
  lambda = 2
)
tail(chains_pois_offspring)
```

## Author(s)

James M. Azam
