# Summarise central estimate

```r
summarise_central_estimate(
  seromodel,
  serosurvey,
  alpha,
  par_name = "seroreversion_rate",
  central_estimate_digits = 2
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
- `par_name`: String specifying the parameter to be extracted from `seromodel`
- `central_estimate_digits`: Number of central estimate digits

## Returns

Text summarising specified central estimate

Summarise central estimate

## Examples

```r
data(veev2012)
seromodel <- fit_seromodel(veev2012, iter = 100)
summarise_central_estimate(
  seromodel,
  veev2012,
  alpha = 0.05,
  par_name = "foi"
  )
```
