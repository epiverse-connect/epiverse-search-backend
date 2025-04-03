# Simulate serosurvey data based on a time-varying Force-of-Infection (FoI) model.

```r
simulate_serosurvey_time(foi, survey_features, seroreversion_rate = 0)
```

## Arguments

- `foi`: A dataframe containing the FoI values. For time-varying models the columns should be:
    
    - **year**: Calendar years starting at the birth year of the oldest person and up to the time of the serosurvey
    - **foi**: Corresponding values of the FoI by year
    
    For age-varying models the columns should be:.
    
    - **age**: Ages starting at 1 and up to the age of the oldest person in the serosurvey
    - **foi**: Corresponding values of the FoI by age
    
    For age-and-time-varying models the columns should be:
    
    
    - **age**: Ages starting at 1 and up to the age of the oldest person in the serosurvey
    - **time**: Calendar years starting at the birth year of the oldest person and up to the time of the serosurvey
    - **foi**: Corresponding values of FoI by age and year
- `survey_features`: A dataframe containing information about the binned age groups and sample sizes for each. It should contain columns:
    
    - **age_min**: Left limits of the age groups to be considered in the serosurvey
    - **age_max**: Right limits of the age groups to be considered in the serosurvey
    - **n_sample**: Number of samples by age group
    
    The resulting age intervals are closed to the left `[` and open to the right `)`.
- `seroreversion_rate`: A non-negative value determining the rate of seroreversion (per year). Default is 0.

## Returns

A dataframe with simulated serosurvey data, including age group information, overall sample sizes, the number of seropositive individuals, and other survey features.

This function generates binned serosurvey data based on a time-varying FoI model, optionally including seroreversion. This function allows construction of serosurveys with binned age groups, and it generates uncertainty in the distribution of a sample size within an age bin through multinomial sampling.

## Examples

```r
# specify FOIs for each year
foi_df <- data.frame(
  year = seq(1990, 2009, 1),
  foi = rnorm(20, 0.1, 0.01)
)
survey_features <- data.frame(
  age_min = c(1, 3, 15),
  age_max = c(2, 14, 20),
  n_sample = c(1000, 2000, 1500))
serosurvey <- simulate_serosurvey_time(
foi_df, survey_features)
```
