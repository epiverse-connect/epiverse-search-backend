# Runs specified stan model for the Force-of-Infection (FoI)

```r
fit_seromodel(
  serosurvey,
  model_type = "constant",
  is_log_foi = FALSE,
  foi_prior = sf_normal(),
  foi_sigma_rw = sf_none(),
  foi_index = NULL,
  foi_init = NULL,
  is_seroreversion = FALSE,
  seroreversion_prior = sf_normal(),
  ...
)
```

## Arguments

- `serosurvey`: - **`survey_year`**: Year in which the survey took place (only needed to plot time models)
    - **`age_min`**: Floor value of the average between age_min and age_max
    - **`age_max`**: The size of the sample
    - **`n_sample`**: Number of samples for each age group
    - **`n_seropositive`**: Number of positive samples for each age group
- `model_type`: Type of the model. Either "constant", "age" or "time"
- `is_log_foi`: Boolean to set logarithmic scale in the FoI
- `foi_prior`: Force-of-infection distribution specified by means of the helper functions. Currently available options are:
    
    - **sf_normal**: Function to set normal distribution priors
    - **sf_uniform**: Function to set uniform distribution priors
- `foi_sigma_rw`: Prior distribution for the standard deviation of the Force-of-Infection. Currently available options are:
    
    - **sf_normal**: Function to set normal distribution prior. Available for time models in the log-scale
    - **sf_cauchy**: Function to set Cauchy distribution prior. Available for time models in regular scale.
- `foi_index`: Integer vector specifying the age-groups for which Force-of-Infection values will be estimated. It can be specified by means of get_foi_index
- `foi_init`: Initialization function for sampling. If null, default is chosen depending on the foi-scale of the model
- `is_seroreversion`: Boolean specifying whether to include seroreversion rate estimation in the model
- `seroreversion_prior`: seroreversion distribution specified by means of the helper functions. Currently available options are:
    
    - **sf_normal**: Function to set normal distribution priors
    - **sf_uniform**: Function to set uniform distribution priors
    - **sf_none**: Function to set no prior distribution
- `...`: Additional parameters for rstan

## Returns

stan_fit object with Force-of-Infection and seroreversion (when applicable) samples

Runs specified stan model for the Force-of-Infection (FoI)

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
  iter = 100
)
```
