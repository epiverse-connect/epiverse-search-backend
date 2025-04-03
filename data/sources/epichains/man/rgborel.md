# Generate random numbers from a Gamma-Borel mixture distribution

```r
rgborel(n, size, prob, mu, censor_at = Inf)
```

## Arguments

- `n`: Number of random variates to generate.
- `size`: The dispersion parameter (often called `k` in ecological applications); A positive number.
- `prob`: Probability of success (in the parameterisation with `prob`, see also `NegBinomial`); A number between 0 and 1.
- `mu`: Mean; A positive number.
- `censor_at`: A stopping criterion; `<numeric>`. Defaults to `Inf`. A value above which the simulation ends and the random number is set to `Inf` (as a form of censoring). `rborel()` simulates chain sizes using `simulate_chain_stats()` with a Poisson offspring distribution, so if `mu >= 1`, the simulation could proceed unendingly. This parameter is used to prevent this.

## Returns

Numeric vector of random numbers

Generate random numbers from a Gamma-Borel mixture distribution

## Examples

```r
set.seed(32)
rgborel(n = 5, size = 0.3, mu = 1, censor_at = 5)
```

## Author(s)

Sebastian Funk James M. Azam
