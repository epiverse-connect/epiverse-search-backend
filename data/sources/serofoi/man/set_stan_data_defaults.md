# Set stan data defaults for sampling

```r
set_stan_data_defaults(stan_data, is_log_foi = FALSE, is_seroreversion = FALSE)
```

## Arguments

- `stan_data`: List to be passed to rstan
- `is_log_foi`: Boolean to set logarithmic scale in the FoI
- `is_seroreversion`: Boolean specifying whether to include seroreversion rate estimation in the model

## Returns

List with default values of stan data for sampling

Set stan data defaults for sampling
