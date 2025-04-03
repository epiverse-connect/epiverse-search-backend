# Summarise specified model

```r
summarise_seromodel(
  seromodel,
  serosurvey,
  alpha = 0.05,
  par_loo_estimate = "elpd_loo",
  loo_estimate_digits = 1,
  central_estimate_digits = 2,
  rhat_digits = 2
)
```

## Arguments

- `seromodel`: stan_fit object obtained from sampling a model with fit_seromodel
- `serosurvey`: - **`survey_year`**: Year in which the survey took place (only needed to plot time models)
    - **`age_min`**: Floor value of the average between age_min and age_max
    - **`age_max`**: The size of the sample
    - **`n_sample`**: Number of samples for each age group
    - **`n_seropositive`**: Number of positive samples for each age group
- `alpha`: 1 - alpha indicates the credibility level to be used
- `par_loo_estimate`: Name of the loo estimate to be extracted. Available options are:
    
    - **`"elpd_loo"`**: Expected log pointwise predictive density
    - **`"p_loo"`**: Effective number of parameters
    - **`"looic"`**: Leave-one-out cross-validation information criteria
    
    For additional information refer to loo .
- `loo_estimate_digits`: Number of loo estimate digits
- `central_estimate_digits`: Number of central estimate digits
- `rhat_digits`: Number of rhat estimate digits

## Returns

A list summarising the specified model

- **`model_name`**: Name of the model
- **`elpd`**: elpd and its standard deviation
- **`foi`**: Estimated foi with credible interval (for 'constant' model)
- **`foi_rhat`**: foi rhat value (for 'constant' model)
- **`seroreversion_rate`**: Estimated seroreversion rate
- **`seroreversion_rate_rhat`**: Seroreversion rate rhat value

Summarise specified model

## Examples

```r
data(veev2012)
seromodel <- fit_seromodel(veev2012, iter = 100)
summarise_seromodel(seromodel, veev2012)
```
