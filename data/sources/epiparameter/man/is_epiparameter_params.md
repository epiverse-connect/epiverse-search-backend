# Check whether the vector of parameters for the probability distribution are in the set of possible parameters used in the epiparameter package

```r
is_epiparameter_params(prob_distribution, prob_distribution_params)
```

## Arguments

- `prob_distribution`: A `character` string specifying the probability distribution. This should match the naming convention of probability distributions (e.g. lognormal is `lnorm`, negative binomial is `nbinom`, and geometric is `geom`).
- `prob_distribution_params`: A named vector of probability distribution parameters.

## Returns

A boolean `logical`.

Check whether the vector of parameters for the probability distribution are in the set of possible parameters used in the epiparameter package

## Details

This check for valid parameters is independent of whether the distribution is truncated or discretised.

## Examples

```r
is_epiparameter_params(
  prob_distribution = "gamma",
  prob_distribution_params = c(shape = 2, scale = 1)
)
```
