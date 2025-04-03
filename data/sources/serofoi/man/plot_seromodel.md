# Visualise results of the provided model

```r
plot_seromodel(
  seromodel,
  serosurvey,
  alpha = 0.05,
  bin_serosurvey = FALSE,
  bin_step = 5,
  foi_df = NULL,
  foi_max = NULL,
  loo_estimate_digits = 1,
  central_estimate_digits = 2,
  seroreversion_digits = 2,
  rhat_digits = 2,
  size_text = 11,
  plot_constant = FALSE,
  x_axis = NA
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
- `bin_serosurvey`: If `TRUE`, `serodata` is binned by means of `prepare_bin_serosurvey`. Otherwise, age groups are kept as originally input.
- `bin_step`: Integer specifying the age groups bin size to be used when `bin_serosurvey` is set to `TRUE`.
- `foi_df`: Dataframe with columns
    
    - **`year`/`age`**: Year/Age (depending on the model)
    - **`foi`**: Force-of-infection values by year/age
- `foi_max`: Max FoI value for plotting
- `loo_estimate_digits`: Number of loo estimate digits
- `central_estimate_digits`: Number of central estimate digits
- `seroreversion_digits`: Number of seroreversion rate digits
- `rhat_digits`: Number of rhat estimate digits
- `size_text`: Size of text for plotting (`base_size` in ggplot2 )
- `plot_constant`: boolean specifying whether to plot single Force-of-Infection estimate and its corresponding rhat value instead of showing this information in the summary. Only relevant when `seromodel@model_name == "constant"`)
- `x_axis`: either `"time"` or `"age"`. Specifies time axis values label for constant model additional plots. Only relevant when and `seromodel@model_name == "constant"`

## Returns

seromodel summary plot

Visualise results of the provided model

## Examples

```r
data(veev2012)
seromodel <- fit_seromodel(veev2012, iter = 100)
plot_seromodel(seromodel, veev2012)
```
