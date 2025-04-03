# Samples size (the number of trials) of a binomial distribution

```r
.rbinom_size(n, x, prob)
```

## Arguments

- `n`: The number of samples to generate. Must be a positive integer.
- `x`: The number of successes. Must be a positive integer.
- `prob`: The probability of success. A numeric between 0 and 1.

## Returns

A numeric vector of the sampled sizes.

Samples the size parameter from the binomial distribution with fixed x (number of successes) and p (success probability)

## Author(s)

Sebastian Funk
