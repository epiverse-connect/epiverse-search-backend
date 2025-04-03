# Plots model summary

```r
plot_summary(
  seromodel,
  serosurvey,
  loo_estimate_digits = 1,
  central_estimate_digits = 2,
  rhat_digits = 2,
  size_text = 11,
  plot_constant = FALSE
)
```

## Arguments

- `seromodel`: stan_fit object obtained from sampling a model with fit_seromodel
- `serosurvey`: - **`survey_year`**: Year in which the survey took place (only needed to plot time models)
    - **`age_min`**: Floor value of the average between age_min and age_max
    - **`age_max`**: The size of the sample
    - **`n_sample`**: Number of samples for each age group
    - **`n_seropositive`**: Number of positive samples for each age group
- `loo_estimate_digits`: Number of loo estimate digits
- `central_estimate_digits`: Number of central estimate digits
- `rhat_digits`: Number of rhat estimate digits
- `size_text`: Size of text for plotting (`base_size` in ggplot2 )
- `plot_constant`: boolean specifying whether to plot single Force-of-Infection estimate and its corresponding rhat value instead of showing this information in the summary. Only relevant when `seromodel@model_name == "constant"`)

## Returns

ggplot object with a summary of the specified model

Plots model summary

## Examples

```r
data(veev2012)
seromodel <- fit_seromodel(veev2012, iter = 100)
plot_summary(seromodel, veev2012)
```
