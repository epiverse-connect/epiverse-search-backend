# Computes the probability of being seropositive when Forces-of-Infection (FoIs) vary by age

```r
probability_exact_age_varying(ages, fois, seroreversion_rate = 0)
```

## Arguments

- `ages`: Integer indicating the ages of the exposed cohorts
- `fois`: Numeric atomic vector corresponding to the age-varying Force-of-Infection to simulate from
- `seroreversion_rate`: Non-negative seroreversion rate. Default is 0.

## Returns

vector of probabilities of being seropositive for age-varying FoI including seroreversion (ordered from youngest to oldest individuals)

Computes the probability of being seropositive when Forces-of-Infection (FoIs) vary by age
