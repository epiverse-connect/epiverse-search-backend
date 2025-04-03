# Calculates the complementary log-probability

```r
.complementary_logprob(x)
```

## Arguments

- `x`: A numeric vector of log-probabilities. Must be negative.

## Returns

A numeric value of the complementary log-probability.

Given x and norm, this calculates log(1-sum(exp(x)))

## Author(s)

Sebastian Funk
