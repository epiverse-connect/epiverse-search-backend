# Calculate outcomes averted by interventions

```r
outcomes_averted(baseline, scenarios, by_group = TRUE, summarise = TRUE)
```

## Arguments

- `baseline`: A nested `<data.table>` of a single model outcome with parameter uncertainty. This is expected to be the output of a single call to model functions such as `model_default()` or `model_ebola()`.
- `scenarios`: A nested `<data.table>` of any number of model outcomes with infection parameter sets identical to those in `baseline` for comparability, i.e., the `scenarios` must differ from the `baseline` only in any interventions applied.
- `by_group`: A single logical value that controls whether outcomes averted are calculated separately for each demographic group in the model outputs. This is passed to the `by_group` argument in `epidemic_size()`. Defaults to `TRUE`.
- `summarise`: A single logical value that controls whether outcomes averted are summarised (returning the median and 95% uncertainty intervals), aggregating over parameter sets for each scenario, or whether the raw differences between the baseline and comparator scenarios are returned while matching by parameter set.

## Returns

A `<data.table>`. When `summarise = TRUE`, a `<data.table>` of the same number of rows as `scenarios`, with the columns `"scenario"`, `"averted_median"`, `"averted_lower"`, and `"averted_upper"`.

When `summarise = FALSE`, a `<data.table>` with one row per `"scenario"`, parameter set (`"param_set"`), and demography group (`"demography_group`), with the additional column `"outcomes_averted"` giving the difference between the baseline and the comparator scenario for each parameter set for each demography group.

Calculate outcomes averted by interventions

## Details

Both deterministic and stochastic models (currently only the Ebola model) are supported.

When comparing deterministic model scenarios, users are expected to ensure that outputs comparable in terms of demographic groups and parameters. The output is expected to have parameter uncertainty, and differences between each scenario and the baseline are calculated after matching on parameter sets.

When comparing stochastic model scenarios, each scenario is matched against the baseline on the replicate number as well as the parameter set to reduce the effect of initial conditions on differences in outcomes.

## Examples

```r
polymod <- socialmixr::polymod
contact_data <- socialmixr::contact_matrix(
  polymod,
  countries = "United Kingdom",
  age.limits = c(0, 20, 40),
  symmetric = TRUE
)

# prepare contact matrix
contact_matrix <- t(contact_data$matrix)

# prepare the demography vector
demography_vector <- contact_data$demography$population
names(demography_vector) <- rownames(contact_matrix)

# initial conditions
initial_i <- 1e-6
initial_conditions <- c(
  S = 1 - initial_i, E = 0, I = initial_i, R = 0, V = 0
)

# build for all age groups
initial_conditions <- rbind(
  initial_conditions,
  initial_conditions,
  initial_conditions
)

# create population object
uk_population <- population(
  name = "UK",
  contact_matrix = contact_matrix,
  demography_vector = demography_vector,
  initial_conditions = initial_conditions
)

# create vector of parameters
beta <- withr::with_seed(
  1,
  rnorm(100, mean = 1.3 / 7, sd = 0.005)
)

baseline <- model_default(
  population = uk_population,
  transmission_rate = beta
)

max_time <- 100
# prepare durations as starting at 25% of the way through an epidemic
# and ending halfway through
time_begin <- max_time / 4
time_end <- max_time / 2

# create three distinct contact interventions
# prepare an intervention that models school closures for 180 days
close_schools <- intervention(
  name = "School closure",
  type = "contacts",
  time_begin = time_begin,
  time_end = time_end,
  reduction = matrix(c(0.3, 0.01, 0.01))
)

# prepare an intervention which mostly affects adults 20 -- 65
close_workplaces <- intervention(
  name = "Workplace closure",
  type = "contacts",
  time_begin = time_begin,
  time_end = time_end,
  reduction = matrix(c(0.01, 0.3, 0.01))
)

intervention_sets <- list(
  list(
    contacts = close_schools
  ),
  list(
    contacts = close_workplaces
  )
)

scenarios <- model_default(
  population = uk_population,
  transmission_rate = beta,
  intervention = intervention_sets
)

# Defaults to summarise = TRUE
outcomes_averted(
  baseline = baseline,
  scenarios = scenarios
)

# Set summarise = FALSE to get raw difference data
outcomes_averted(
  baseline = baseline,
  scenarios = scenarios,
  summarise = FALSE
)
```
