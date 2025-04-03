# Plots Force-of-Infection central estimates

```r
plot_foi_estimates(
  seromodel,
  serosurvey,
  alpha = 0.05,
  foi_df = NULL,
  foi_max = NULL,
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
- `foi_df`: Dataframe with columns
    
    - **`year`/`age`**: Year/Age (depending on the model)
    - **`foi`**: Force-of-infection values by year/age
- `foi_max`: Max FoI value for plotting
- `size_text`: Size of text for plotting (`base_size` in ggplot2 )
- `plot_constant`: boolean specifying whether to plot single Force-of-Infection estimate and its corresponding rhat value instead of showing this information in the summary. Only relevant when `seromodel@model_name == "constant"`)
- `x_axis`: either `"time"` or `"age"`. Specifies time axis values label for constant model additional plots. Only relevant when and `seromodel@model_name == "constant"`

## Returns

ggplot object with estimated FoI

Plots Force-of-Infection central estimates

## Examples

```r
data(chagas2012)
seromodel <- fit_seromodel(
  serosurvey = chagas2012,
  model_type = "time",
  foi_index = data.frame(
    year = 1935:2011,
    foi_index = c(rep(1, 46), rep(2, 31))
  ),
  iter = 100,
  chains = 2
)
plot_foi_estimates(seromodel, chagas2012)
```
