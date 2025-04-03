# Calculate the Cumulative Effect of Interventions on Rate Parameters

```r
.cumulative_rate_intervention(t, time_begin, time_end, reduction)
```

## Arguments

- `t`: The current time.
- `time_begin`: A numeric vector of the start times of all interventions being modelled.
- `time_end`: A numeric vector of the end times of all interventions being modelled. Must be the same length as `time_begin`.
- `reduction`: A numeric vector where each element gives the effect of the corresponding intervention on model rate parameters. When two interventions overlap, the proportions are **added**, for a maximum possible value of 1.0 (i.e., rate set to zero).

## Returns

`.cumulative_rate_intervention()` returns a number of the proportion reduction in a model rate parameter.

`intervention_on_cm()` returns the contact matrix `cm` scaled by the cumulative effect of any active interventions.

Calculate the Cumulative Effect of Interventions on Rate Parameters
