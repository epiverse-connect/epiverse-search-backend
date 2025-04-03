# Summary method for `<epichains>` class

```r
## S3 method for class 'epichains'
summary(object, ...)
```

## Arguments

- `object`: An `<epichains>` object.
- `...`: Not used.

## Returns

An `<epichains_summary>` object containing the chain summary statistics as follows:

 * "size": the total number of offspring produced by a chain before it goes extinct.
 * "length": the number of generations achieved by a chain before it goes extinct.

This calculates the chain statistic (size/length) for the simulated chains and returns an object with the same information as that returned by an equivalent `simulate_chain_stats()` call.

## Examples

```r
# Using a negative binomial offspring distribution and simulating from a
# finite population up to chain size 10.
set.seed(32)
sim_chains_nbinom <- simulate_chains(
  n_chains = 10,
  pop = 100,
  percent_immune = 0,
  statistic = "size",
  offspring_dist = rnbinom,
  stat_threshold = 10,
  mu = 2,
  size = 0.2
)
# Summarise the simulated chains
sim_chains_nbinom_summary <- summary(sim_chains_nbinom)
sim_chains_nbinom_summary

# Same results can be obtained using `simulate_chain_stats()`
set.seed(32)
sim_summary_nbinom <- simulate_chain_stats(
  n_chains = 10,
  pop = 100,
  percent_immune = 0,
  statistic = "size",
  offspring_dist = rnbinom,
  stat_threshold = 10,
  mu = 2,
  size = 0.2
)
sim_summary_nbinom

# Check that the results are the same
setequal(sim_chains_nbinom_summary, sim_summary_nbinom)
```

## Author(s)

James M. Azam
