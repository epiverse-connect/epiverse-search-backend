# Builds stan data for sampling depending on the selected model

```r
build_stan_data(
  serosurvey,
  model_type = "constant",
  foi_prior = sf_uniform(),
  foi_index = NULL,
  is_log_foi = FALSE,
  foi_sigma_rw = sf_none(),
  is_seroreversion = FALSE,
  seroreversion_prior = sf_none()
)
```

## Arguments

- `serosurvey`: - **`survey_year`**: Year in which the survey took place (only needed to plot time models)
    - **`age_min`**: Floor value of the average between age_min and age_max
    - **`age_max`**: The size of the sample
    - **`n_sample`**: Number of samples for each age group
    - **`n_seropositive`**: Number of positive samples for each age group
- `model_type`: Type of the model. Either "constant", "age" or "time"
- `foi_prior`: Force-of-infection distribution specified by means of the helper functions. Currently available options are:
    
    - **sf_normal**: Function to set normal distribution priors
    - **sf_uniform**: Function to set uniform distribution priors
- `foi_index`: Integer vector specifying the age-groups for which Force-of-Infection values will be estimated. It can be specified by means of get_foi_index
- `is_log_foi`: Boolean to set logarithmic scale in the FoI
- `foi_sigma_rw`: Prior distribution for the standard deviation of the Force-of-Infection. Currently available options are:
    
    - **sf_normal**: Function to set normal distribution prior. Available for time models in the log-scale
    - **sf_cauchy**: Function to set Cauchy distribution prior. Available for time models in regular scale.
- `is_seroreversion`: Boolean specifying whether to include seroreversion rate estimation in the model
- `seroreversion_prior`: seroreversion distribution specified by means of the helper functions. Currently available options are:
    
    - **sf_normal**: Function to set normal distribution priors
    - **sf_uniform**: Function to set uniform distribution priors
    - **sf_none**: Function to set no prior distribution

## Returns

List with necessary data for sampling the specified model

Builds stan data for sampling depending on the selected model
