# Simulate a line list and a contacts table

```r
sim_outbreak(
  contact_distribution = function(x) stats::dpois(x = x, lambda = 2),
  infectious_period = function(x) stats::rlnorm(n = x, meanlog = 2, sdlog = 0.5),
  prob_infection = 0.5,
  onset_to_hosp = function(x) stats::rlnorm(n = x, meanlog = 1.5, sdlog = 0.5),
  onset_to_death = function(x) stats::rlnorm(n = x, meanlog = 2.5, sdlog = 0.5),
  onset_to_recovery = NULL,
  reporting_delay = NULL,
  hosp_risk = 0.2,
  hosp_death_risk = 0.5,
  non_hosp_death_risk = 0.05,
  outbreak_start_date = as.Date("2023-01-01"),
  anonymise = FALSE,
  outbreak_size = c(10, 10000),
  population_age = c(1, 90),
  case_type_probs = c(suspected = 0.2, probable = 0.3, confirmed = 0.5),
  contact_tracing_status_probs = c(under_followup = 0.7, lost_to_followup = 0.2, unknown
    = 0.1),
  config = create_config()
)
```

## Arguments

- `contact_distribution`: A `function` or an `<epiparameter>` object to generate the number of contacts per infection.
    
    The function can be defined or anonymous. The function must have a single argument in the form of an `integer` vector with elements representing the number of contacts, and return a `numeric` vector where each element corresponds to the probability of observing the number of contacts in the vector passed to the function. The index of the `numeric` vector returned is offset by one to the corresponding probability of observing the number of contacts, i.e. the first element of the output vector is the probability of observing zero contacts, the second element is the probability of observing one contact, etc.
    
    An `<epiparameter>` can be provided. This will be converted into a probability mass function internally.
    
    The default is an anonymous function with a Poisson probability mass function (`dpois()`) with a mean (`\lambda`) of 2 contacts per infection.
- `infectious_period`: A `function` or an `<epiparameter>` object for the infectious period. This defines the duration from becoming infectious to no longer infectious. In the simulation, individuals are assumed to become infectious immediately after being infected (the latency period is assumed to be zero). The time intervals between an infected individual and their contacts are assumed to be uniformly distributed within the infectious period. Infectious periods must be strictly positive.
    
    The function can be defined or anonymous. The function must return a vector of randomly generated real numbers representing sampled infectious periods. The function must have a single argument, the number of random infectious periods to generate.
    
    An `<epiparameter>` can be provided. This will be converted into random number generator internally.
    
    The default is an anonymous function with a lognormal distribution random number generator (`rlnorm()`) with `meanlog = 2` and `sdlog = 0.5`.
- `prob_infection`: A single `numeric` for the probability of a secondary contact being infected by an infected primary contact.
- `onset_to_hosp`: A `function` or an `<epiparameter>` object for the onset-to-hospitalisation delay distribution. `onset_to_hosp` can also be set to `NULL` to not simulate hospitalisation (admission) dates.
    
    The function can be defined or anonymous. The function must return a vector of `numeric`s for the length of the onset-to-hospitalisation delay. The function must have a single argument.
    
    An `<epiparameter>` can be provided. This will be converted into a random number generator internally.
    
    The default is an anonymous function with a lognormal distribution random number generator (`rlnorm()`) with `meanlog = 1.5` and `sdlog = 0.5`.
    
    If `onset_to_hosp` is set to `NULL` then `hosp_risk` and `hosp_death_risk`
    
    will be automatically set to `NULL` if not manually specified.
- `onset_to_death`: A `function` or an `<epiparameter>` object for the onset-to-death delay distribution. `onset_to_death` can also be set to `NULL` to not simulate dates for individuals that died.
    
    The function can be defined or anonymous. The function must return a vector of `numeric`s for the length of the onset-to-death delay. The function must have a single argument.
    
    An `<epiparameter>` can be provided. This will be converted into a random number generator internally.
    
    The default is an anonymous function with a lognormal distribution random number generator (`rlnorm()`) with `meanlog = 2.5` and `sdlog = 0.5`.
    
    If `onset_to_death` is set to `NULL` then `non_hosp_death_risk` and `hosp_death_risk` will be automatically set to `NULL` if not manually specified.
    
    For hospitalised cases, the function ensures the onset-to-death time is greater than the onset-to-hospitalisation time. After many (1000) attempts, if an onset-to-death time (from `onset_to_death`) cannot be sampled that is greater than a onset-to-hospitalisation time (from `onset_to_hosp`) then the function will error. Due to this conditional sampling, the onset-to-death times in the line list may not resemble the distributional form input into the function.
- `onset_to_recovery`: A `function` or an `<epiparameter>` object for the onset-to-recovery delay distribution. `onset_to_recovery` can also be `NULL`
    
    to not simulate dates for individuals that recovered.
    
    The function can be defined or anonymous. The function must return a vector of `numeric`s for the length of the onset-to-recovery delay. The function must have a single argument.
    
    An `<epiparameter>` can be provided. This will be converted into a random number generator internally.
    
    The default is `NULL` so by default cases that recover get an `NA` in the `$date_outcome` line list column.
    
    For hospitalised cases, the function ensures the onset-to-recovery time is greater than the onset-to-hospitalisation time. After many (1000) attempts, if an onset-to-recovery time (from `onset_to_recovery`) cannot be sampled that is greater than a onset-to-hospitalisation time (from `onset_to_hosp`) then the function will error. Due to this conditional sampling, the onset-to-recovery times in the line list may not resemble the distributional form input into the function.
- `reporting_delay`: A `function` for the reporting delay distribution or `NULL`. The (random) number generating function creates delays between the time of symptom onset (`$date_onset`) and the case being reported (`$date_reporting`).
    
    The function can be defined or anonymous. The function must return a vector of `numeric`s for the length of the reporting delay. The function must have a single argument.
    
    The default is `NULL` so by default there is no reporting delay, and the `$date_reporting` line list column is identical to the `$date_onset` column.
- `hosp_risk`: Either a single `numeric` for the hospitalisation risk of everyone in the population, or a `<data.frame>` with age specific hospitalisation risks. Default is 20% hospitalisation (`0.2`) for the entire population. If the `onset_to_hosp` argument is set to `NULL` this argument will automatically be set to `NULL` if not specified or can be manually set to `NULL`. See details and examples for more information.
- `hosp_death_risk`: Either a single `numeric` for the death risk for hospitalised individuals across the population, or a `<data.frame>` with age specific hospitalised death risks Default is 50% death risk in hospitals (`0.5`) for the entire population. If the `onset_to_death` argument is set to `NULL` this argument will automatically be set to `NULL` if not specified or can be manually set to `NULL`. See details and examples for more information. The `hosp_death_risk` can vary through time if specified in the `time_varying_death_risk` element of `config`, see `vignette("time-varying-cfr", package = "simulist")` for more information.
- `non_hosp_death_risk`: Either a single `numeric` for the death risk for outside of hospitals across the population, or a `<data.frame>` with age specific death risks outside of hospitals. Default is 5% death risk outside of hospitals (`0.05`) for the entire population. If the `onset_to_death`
    
    argument is set to `NULL` this argument will automatically be set to `NULL`
    
    if not specified or can be manually set to `NULL`. See details and examples for more information. The `non_hosp_death_risk` can vary through time if specified in the `time_varying_death_risk` element of `config`, see `vignette("time-varying-cfr", package = "simulist")` for more information.
- `outbreak_start_date`: A `date` for the start of the outbreak.
- `anonymise`: A `logical` boolean for whether case names should be anonymised. Default is `FALSE`.
- `outbreak_size`: A `numeric` vector of length 2 defining the minimum and the maximum number of infected individuals for the simulated outbreak. Default is `c(10, 1e4)`, so the minimum outbreak size is 10 infected individuals, and the maximum outbreak size is 10,000 infected individuals. Either number can be changed to increase or decrease the maximum or minimum outbreak size to allow simulating larger or smaller outbreaks. If the minimum outbreak size cannot be reached after running the simulation for many iterations (internally) then the function errors, whereas if the maximum outbreak size is exceeded the function returns the data early and a warning stating how many cases and contacts are returned.
- `population_age`: Either a `numeric` vector with two elements or a `<data.frame>` with age structure in the population. Use a `numeric` vector to specific the age range of the population, the first element is the lower bound for the age range, and and the second is the upper bound for the age range (both inclusive, i.e. [lower, upper]). The `<data.frame>` with age groups and the proportion of the population in that group. See details and examples for more information.
- `case_type_probs`: A named `numeric` vector with the probability of each case type. The names of the vector must be `"suspected"`, `"probable"`, `"confirmed"`. Values of each case type must sum to one.
- `contact_tracing_status_probs`: A named `numeric` vector with the probability of each contact tracing status. The names of the vector must be `"under_followup"`, `"lost_to_followup"`, `"unknown"`. Values of each contact tracing status must sum to one.
- `config`: A list of settings to adjust the randomly sampled delays and Ct values. See `create_config()` for more information.

## Returns

A list with two elements:

1. A line list `\<data.frame\>`
2. A contacts `\<data.frame\>`

The line list and contacts are simulated using a branching process and parameterised with epidemiological parameters.

## Details

For age-stratified hospitalised and death risks a `<data.frame>`

will need to be passed to the `hosp_risk` and/or `hosp_death_risk`

arguments. This `<data.frame>` should have two columns:

 * `age_limit`: a column with one `numeric` per cell for the lower bound (minimum) age of the age group (inclusive).
 * `risk`: a column with one `numeric` per cell for the proportion (or probability) of hospitalisation for that age group. Should be between 0 and 1.

For an age-structured population, a `<data.frame>` with two columns:

 * `age_limit`: a column with one `numeric` per cell for the lower bound (minimum) age of the age group (inclusive), except the last element which is the upper bound (maximum) of the population.
 * `proportion`: a column with the proportion of the population that are in that age group. Proportions must sum to one.

## Examples

```r
# quickly simulate an outbreak using the function defaults
outbreak <- sim_outbreak()
head(outbreak$linelist)
head(outbreak$contacts)

# to simulate a more realistic outbreak load epiparameters from
# {epiparameter}
library(epiparameter)
contact_distribution <- epiparameter(
  disease = "COVID-19",
  epi_name = "contact distribution",
  prob_distribution = create_prob_distribution(
    prob_distribution = "pois",
    prob_distribution_params = c(mean = 2)
  )
)

infectious_period <- epiparameter(
  disease = "COVID-19",
  epi_name = "infectious period",
  prob_distribution = create_prob_distribution(
    prob_distribution = "gamma",
    prob_distribution_params = c(shape = 1, scale = 1)
  )
)

onset_to_hosp <- epiparameter(
  disease = "COVID-19",
  epi_name = "onset to hospitalisation",
  prob_distribution = create_prob_distribution(
    prob_distribution = "lnorm",
    prob_distribution_params = c(meanlog = 1, sdlog = 0.5)
  )
)

# get onset to death from {epiparameter} database
onset_to_death <- epiparameter_db(
  disease = "COVID-19",
  epi_name = "onset to death",
  single_epiparameter = TRUE
)

outbreak <- sim_outbreak(
  contact_distribution = contact_distribution,
  infectious_period = infectious_period,
  prob_infection = 0.5,
  onset_to_hosp = onset_to_hosp,
  onset_to_death = onset_to_death
)
```

## Author(s)

Joshua W. Lambert
