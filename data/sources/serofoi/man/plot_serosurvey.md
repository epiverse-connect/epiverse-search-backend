# Plots seroprevalence from the given serosurvey

```r
plot_serosurvey(
  serosurvey,
  size_text = 11,
  bin_serosurvey = FALSE,
  bin_step = 5
)
```

## Arguments

- `serosurvey`: - **`survey_year`**: Year in which the survey took place (only needed to plot time models)
    - **`age_min`**: Floor value of the average between age_min and age_max
    - **`age_max`**: The size of the sample
    - **`n_sample`**: Number of samples for each age group
    - **`n_seropositive`**: Number of positive samples for each age group
- `size_text`: Size of text for plotting (`base_size` in ggplot2 )
- `bin_serosurvey`: If `TRUE`, `serodata` is binned by means of `prepare_bin_serosurvey`. Otherwise, age groups are kept as originally input.
- `bin_step`: Integer specifying the age groups bin size to be used when `bin_serosurvey` is set to `TRUE`.

## Returns

ggplot object with seroprevalence plot

Plots seroprevalence from the given serosurvey

## Examples

```r
# Chikungunya example serosurvey
data(chik2015)
plot_serosurvey(chik2015)

# VEEV example serosurvey
data(veev2012)
plot_serosurvey(veev2012)
```
