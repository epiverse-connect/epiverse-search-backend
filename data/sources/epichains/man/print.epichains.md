# Print an `<epichains>` object

```r
## S3 method for class 'epichains'
print(x, ...)
```

## Arguments

- `x`: An `<epichains>` object.
- `...`: Other parameters passed to `print()`.

## Returns

Invisibly returns an `<epichains>`. Called for side-effects.

Print an `<epichains>` object

## Examples

```r
# Using a Poisson offspring distribution and simulating from an infinite
# population up to chain size 10.
set.seed(32)
chains_pois_offspring <- simulate_chains(
  n_chains = 10,
  statistic = "size",
  offspring_dist = rpois,
  stat_threshold = 10,
  generation_time = function(n) rep(3, n),
  lambda = 2
)
chains_pois_offspring # Print the object
```

## Author(s)

James M. Azam
