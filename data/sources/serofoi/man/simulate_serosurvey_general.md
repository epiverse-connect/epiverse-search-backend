# Simulate serosurvey data based on general serocatalytic model.

```r
simulate_serosurvey_general(
  construct_A_fun,
  calculate_seroprev_fun,
  initial_conditions,
  survey_features,
  ...
)
```

## Arguments

- `construct_A_fun`: A function that constructs a matrix that defines the multiplier term in the linear ODE system.
- `calculate_seroprev_fun`: A function which takes the state vector and returns the seropositive fraction.
- `initial_conditions`: The initial state vector proportions for each birth cohort.
- `survey_features`: A dataframe containing information about the binned age groups and sample sizes for each. It should contain columns:
    
    - **age_min**: Left limits of the age groups to be considered in the serosurvey
    - **age_max**: Right limits of the age groups to be considered in the serosurvey
    - **n_sample**: Number of samples by age group
    
    The resulting age intervals are closed to the left `[` and open to the right `)`.
- `...`: Additional parameters for `construct_A_fun`

## Returns

A dataframe with simulated serosurvey data, including age group information, overall sample sizes, the number of seropositive individuals, and other survey features.

This simulation method assumes only that the model system can be written as a piecewise-linear ordinary differential equation system.

## Examples

```r
foi_df_time <- data.frame(
  year = seq(1946, 2025, 1),
  foi = c(rep(0, 40), rep(1, 40))
)

foi_df_age <- data.frame(
  age = 1:80,
  foi = 2 * dlnorm(1:80, meanlog = 3.5, sdlog = 0.5)
)

# generate age and time dependent FoI from multipliers
foi_age_time <- expand.grid(
  year = foi_df_time$year,
  age = foi_df_age$age
) |>
  dplyr::left_join(foi_df_age, by = "age") |>
  dplyr::rename(foi_age = foi) |>
  dplyr::left_join(foi_df_time, by = "year") |>
  dplyr::rename(foi_time = foi) |>
  dplyr::mutate(foi = foi_age * foi_time) |>
  dplyr::select(-c("foi_age", "foi_time"))

# create survey features for simulating
max_age <- 80
n_sample <- 50
survey_features <- data.frame(
  age_min = seq(1, max_age, 5),
  age_max = seq(5, max_age, 5)) |>
  dplyr::mutate(n_sample = rep(n_sample, length(age_min))
  )

# simulate survey from age and time FoI
serosurvey <- simulate_serosurvey(
  model = "age-time",
  foi = foi_age_time,
  survey_features = survey_features
)
```
