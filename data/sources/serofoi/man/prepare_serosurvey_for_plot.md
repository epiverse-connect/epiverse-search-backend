# Prepares serosurvey for plotting

```r
prepare_serosurvey_for_plot(serosurvey, alpha = 0.05)
```

## Arguments

- `serosurvey`: - **`survey_year`**: Year in which the survey took place (only needed to plot time models)
    - **`age_min`**: Floor value of the average between age_min and age_max
    - **`age_max`**: The size of the sample
    - **`n_sample`**: Number of samples for each age group
    - **`n_seropositive`**: Number of positive samples for each age group
- `alpha`: 1 - alpha indicates the confidence level to be used

## Returns

serosurvey with additional columns:

- **seroprev**: Seroprevalence computed as the proportion of positive cases `n_seropositive` in the number of samples `n_sample` for each age group
- **seroprev_lower**: Lower limit of the binomial confidence interval of `seroprev`
- **seroprev_upper**: Upper limit of the binomial confidence interval of `seroprev`

Adds seroprevalence values with corresponding binomial confidence interval
