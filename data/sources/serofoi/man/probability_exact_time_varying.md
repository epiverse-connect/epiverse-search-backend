# Computes the probability of being seropositive when Forces-of-Infection (FoIs) vary by time

```r
probability_exact_time_varying(years, fois, seroreversion_rate = 0)
```

## Arguments

- `years`: Integer indicating the years covering the birth ages of the sample
- `fois`: Numeric atomic vector corresponding to the age-varying FoI to simulate from
- `seroreversion_rate`: Non-negative seroreversion rate. Default is 0.

## Returns

vector of probabilities of being seropositive for age-varying FoI including seroreversion (ordered from youngest to oldest individuals)

Computes the probability of being seropositive when Forces-of-Infection (FoIs) vary by time
