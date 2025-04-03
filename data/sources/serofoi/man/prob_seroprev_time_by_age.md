# Generate probabilities of seropositivity by age based on a time-varying Force-of-Infection (FoI) model.

```r
prob_seroprev_time_by_age(foi, seroreversion_rate)
```

## Arguments

- `foi`: A dataframe containing the FoI values for different years. It should have two columns: 'year' and 'foi'.
- `seroreversion_rate`: A non-negative numeric value representing the rate of seroreversion.

## Returns

A dataframe with columns 'age' and 'seropositivity'.

This function calculates the probabilities of seropositivity by age based on a time-varying FoI model. It takes into account the FoI and the rate of seroreversion.
