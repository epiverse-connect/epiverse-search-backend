# Extracts central estimates from stan_fit object for specified parameter

```r
extract_central_estimates(
  seromodel,
  serosurvey,
  alpha = 0.05,
  par_name = "foi_vector"
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

## Returns

A dataframe with the following columns

- **`median`**: Median of the samples computed as the 0.5 quantile
- **`lower`**: Lower quantile `alpha`
- **`upper`**: Upper quantile `1 - alpha`

Extracts central estimates from stan_fit object for specified parameter

## Examples

```r
data(veev2012)
seromodel <- fit_seromodel(veev2012, iter = 100)
central_estimates <- extract_central_estimates(
  seromodel,
  veev2012,
  par_name = "foi"
)
```
