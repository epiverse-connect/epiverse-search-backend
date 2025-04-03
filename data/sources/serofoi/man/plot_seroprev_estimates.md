# Plot seroprevalence estimates on top of the serosurvey

```r
plot_seroprev_estimates(
  seromodel,
  serosurvey,
  alpha = 0.05,
  size_text = 11,
  bin_serosurvey = FALSE,
  bin_step = 5
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
- `size_text`: Size of text for plotting (`base_size` in ggplot2 )
- `bin_serosurvey`: If `TRUE`, `serodata` is binned by means of `prepare_bin_serosurvey`. Otherwise, age groups are kept as originally input.
- `bin_step`: Integer specifying the age groups bin size to be used when `bin_serosurvey` is set to `TRUE`.

## Returns

ggplot object with seroprevalence estimates and serosurveys plots

Plot seroprevalence estimates on top of the serosurvey

## Examples

```r
data(veev2012)
seromodel <- fit_seromodel(veev2012, iter = 100)
plot_seroprev_estimates(seromodel, veev2012)
```
