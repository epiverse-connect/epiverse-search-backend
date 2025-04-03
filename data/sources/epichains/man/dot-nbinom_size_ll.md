# Log-likelihood of the size of chains with Negative-Binomial offspring distribution

```r
.nbinom_size_ll(x, size, prob, mu)
```

## Arguments

- `x`: A numeric vector of chain sizes.
- `size`: The dispersion parameter (often called `k` in ecological applications); A positive number.
- `prob`: Probability of success (in the parameterisation with `prob`, see also `NegBinomial`); A number between 0 and 1.
- `mu`: Mean; A positive number.

## Returns

A numeric vector of log-likelihood values.

Log-likelihood of the size of chains with Negative-Binomial offspring distribution

## Author(s)

Sebastian Funk James M. Azam
