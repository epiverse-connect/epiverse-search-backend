# Samples chain lengths with given observation probabilities

```r
.rgen_length(n, x, prob)
```

## Arguments

- `n`: The number of samples to generate. Must be a positive integer.
- `x`: A numeric vector of the observed chain lengths.
- `prob`: The probability of observation. A numeric between 0 and 1.

## Returns

A numeric vector of the sampled chain lengths.

Samples the length of a transmission chain where each individual element is observed with binomial probability with parameters n (number of successes) and p (success probability)

## Author(s)

Sebastian Funk
