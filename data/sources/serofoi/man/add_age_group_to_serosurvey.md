# Adds age group marker to serosurvey

```r
add_age_group_to_serosurvey(serosurvey)
```

## Arguments

- `serosurvey`: - **`survey_year`**: Year in which the survey took place (only needed to plot time models)
    - **`age_min`**: Floor value of the average between age_min and age_max
    - **`age_max`**: The size of the sample
    - **`n_sample`**: Number of samples for each age group
    - **`n_seropositive`**: Number of positive samples for each age group

## Returns

serosurvey with additional column specifying age group marker defined as the mean floor between `age_min` and `age_max`

Adds age group marker to serosurvey
