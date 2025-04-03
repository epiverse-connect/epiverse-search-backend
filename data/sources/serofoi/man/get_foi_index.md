# Generates Force-of-Infection indexes for heterogeneous age groups

```r
get_foi_index(serosurvey, group_size, model_type)
```

## Arguments

- `serosurvey`: - **`survey_year`**: Year in which the survey took place (only needed to plot time models)
    - **`age_min`**: Floor value of the average between age_min and age_max
    - **`age_max`**: The size of the sample
    - **`n_sample`**: Number of samples for each age group
    - **`n_seropositive`**: Number of positive samples for each age group
- `group_size`: Age groups size
- `model_type`: Type of the model. Either "age" or "time"

## Returns

A Data Frame which describes the grouping of years or ages (dependent on model) into pieces within which the FoI is assumed constant when performing model fitting. A single FoI value will be estimated for ages/years assigned with the same index

Generates a list of integers indexing together the time/age intervals for which FoI values will be estimated in fit_seromodel . The max value in `foi_index` corresponds to the number of FoI values to be estimated when sampling. The serofoi approach to fitting serological data currently supposes that FoI is piecewise-constant across either groups of years or ages, and this function creates a Data Frame that communicates this grouping to the Stan model

## Examples

```r
data(chagas2012)
foi_index <- get_foi_index(chagas2012, group_size = 25, model_type = "time")
```
