# Bayesian diffusion-driven multi-type epidemic models via Stan

```r
stan_igbm(
  y_data,
  contact_matrix,
  age_distribution_population,
  age_specific_ifr,
  itd_distr,
  incubation_period = 3,
  infectious_period = 4,
  likelihood_variance_type = c("quadratic", "linear"),
  ecr_changes = 1,
  prior_scale_x0 = 1,
  prior_scale_x1 = 1,
  prior_scale_contactmatrix = 0.05,
  pi_perc = 0.1,
  prior_volatility = normal(location = 0, scale = 2.5),
  prior_nb_dispersion = gamma(shape = 2, rate = 1),
  algorithm_inference = c("sampling", "optimizing", "meanfield", "fullrank"),
  nBurn = 500,
  nPost = 500,
  nThin = 1,
  adapt_delta = 0.8,
  max_treedepth = 14,
  seed = 1,
  ...
)

stan_igbm.fit(
  standata_preprocessed,
  prior_volatility,
  prior_nb_dispersion,
  algorithm,
  nBurn,
  nPost,
  nThin,
  adapt_delta = NULL,
  max_treedepth = NULL,
  seed,
  ...
)
```

## Arguments

- `y_data`: data.frame; age-specific mortality counts in time. See `data(age_specific_mortality_counts)`.
- `contact_matrix`: matrix; a squared matrix representing the the number of contacts between age groups.
- `age_distribution_population`: data.frame; the age distribution of a given population. See `aggregate_age_distribution`.
- `age_specific_ifr`: data.frame; time-varying age-specific infection-fatality ratio. See `aggregate_ifr_react`.
- `itd_distr`: vector; Infection-to-death distribution. A vector of length **ts_length**.
- `incubation_period`: integer; length of incubation period in days. Must be >=1.
- `infectious_period`: integer; length of infectious period in days. Must be >=1.
- `likelihood_variance_type`: integer; If `0`, the variance of the over-dispersed count model is a quadratic function of the mean; if `1`, the variance of the over-dispersed count model is a linear function of the mean.
- `ecr_changes`: integer; between 1 and 7, defaults to 1. Expresses the number of changes of the effective contact rate during the course of 7 days.
- `prior_scale_x0`: double; scale parameter of a Normal prior distribution assigned to the age-specific log(transmissibility) at time `t = 0`.
- `prior_scale_x1`: double; scale parameter of a Normal prior distribution assigned to the age-specific log(transmissibility) at time `t = 1`.
- `prior_scale_contactmatrix`: double; defaults to 0.05. A positive number that scales the informative Normal prior distribution assigned to the random contact matrix.
- `pi_perc`: numeric; between 0 and 1. It represents the proportion of Exposed individuals in each age group of a given population at time `t = 0`. while the rest `100*(1-pi_perc)` remain Susceptible.
- `prior_volatility`: Prior distribution for the volatility parameters of the age-specific diffusion processes. `prior_volatility` can be a call to `exponential` to use an exponential distribution, `gamma` to use a Gamma distribution or one of `normal`, `student_t` or `cauchy` to use a half-normal, half-t, or half-Cauchy prior. See `priors` for details on these functions.
- `prior_nb_dispersion`: Prior distribution for the dispersion parameter `phi` of the over-dispersed count model. Same options as for `prior_volatility`.
- `algorithm_inference`: One of the sampling algorithms that are implemented in Stan. See `stan`.
- `nBurn`: integer; number of burn-in iterations at the beginning of an MCMC run. See `sampling`.
- `nPost`: integer; number of MCMC iterations after burn-in. See `sampling`.
- `nThin`: integer; a positive integer specifying the period for saving samples. The default is 1, which is usually the recommended value. See `sampling`.
- `adapt_delta`: double; between 0 and 1, defaults to 0.8. See `stan`.
- `max_treedepth`: integer; defaults to 14. See `stan`.
- `seed`: integer; seed for the random number generator. See `set.seed`.
- `...`: Additional arguments, to be passed to lower-level functions.
- `standata_preprocessed`: A named list providing the data for the model. See `sampling`.
- `algorithm`: See `algorithm` in stan_igbm .

## Returns

An object of class **stanigbm** representing the fitted results. Slot mode for this object indicates if the sampling is done or not.

An object of S4 class **stanfit** representing the fitted results. Slot mode for this object indicates if the sampling is done or not.

## Description

A Bayesian evidence synthesis approach to model the age-specific transmission dynamics of COVID-19 based on daily age-stratified mortality counts. The temporal evolution of transmission rates in populations containing multiple types of individual is reconstructed via independent diffusion processes assigned to the key epidemiological parameters. A suitably tailored Susceptible-Exposed-Infected-Removed (SEIR) compartmental model is used to capture the latent counts of infections and to account for fluctuations in transmission influenced by phenomena like public health interventions and changes in human behaviour.

## Details

The `stan_igbm` function performs full Bayesian estimation (if `algorithm_inference` is `"sampling"`) via MCMC. The Bayesian model adds priors (i) on the diffusion processes used to express the time-varying transmissibility of the virus, the probability that a contact between an infectious person in age group alpha and a susceptible person in age group alpha leads to transmission at time `t` and (ii) on a random contact matrix which represents the average number of contacts between individuals of age group alpha and age group alpha' The `stan_igbm` function calls the workhorse `stan_igbm.fit` function.

## Examples

```r
# Age-specific mortality/incidence count time series:
data(age_specific_mortality_counts)
data(age_specific_cusum_infection_counts)

# Import the age distribution for Greece in 2020:
age_distr <- age_distribution(country = "Greece", year = 2020)

# Lookup table:
lookup_table <- data.frame(Initial = age_distr$AgeGrp,
                          Mapping = c(rep("0-39",  8),
                                      rep("40-64", 5),
                                      rep("65+"  , 3)))

# Aggregate the age distribution table:
aggr_age <- aggregate_age_distribution(age_distr, lookup_table)

# Import the projected contact matrix for Greece:
conmat <- contact_matrix(country = "GRC")

# Aggregate the contact matrix:
aggr_cm <- aggregate_contact_matrix(conmat, lookup_table, aggr_age)

# Aggregate the IFR:
ifr_mapping <- c(rep("0-39", 8), rep("40-64", 5), rep("65+", 3))

aggr_age_ifr <- aggregate_ifr_react(age_distr, ifr_mapping, age_specific_cusum_infection_counts)

# Infection-to-death distribution:
ditd <- itd_distribution(ts_length  = nrow(age_specific_mortality_counts),
                         gamma_mean = 24.19231,
                         gamma_cv   = 0.3987261)

# Posterior sampling:

rstan::rstan_options(auto_write = TRUE)
chains <- 1
options(mc.cores = chains)

igbm_fit <- stan_igbm(y_data                      = age_specific_mortality_counts,
                      contact_matrix              = aggr_cm,
                      age_distribution_population = aggr_age,
                      age_specific_ifr            = aggr_age_ifr[[3]],
                      itd_distr                   = ditd,
                      incubation_period           = 3,
                      infectious_period           = 4,
                      likelihood_variance_type    = "linear",
                      ecr_changes                 = 7,
                      prior_scale_x0              = 1,
                      prior_scale_x1              = 1,
                      prior_scale_contactmatrix   = 0.05,
                      pi_perc                     = 0.1,
                      prior_volatility            = normal(location = 0, scale = 1),
                      prior_nb_dispersion         = exponential(rate = 1/5),
                      algorithm_inference         = "sampling",
                      nBurn                       = 10,
                      nPost                       = 30,
                      nThin                       = 1,
                      chains                      = chains,
                      adapt_delta                 = 0.6,
                      max_treedepth               = 14,
                      seed                        = 1)

# print_summary <- summary(object = igbm_fit, y_data = age_specific_mortality_counts)$summary
```

## References

Bouranis, L., Demiris, N. Kalogeropoulos, K. and Ntzoufras, I. (2022). Bayesian analysis of diffusion-driven multi-type epidemic models with application to COVID-19. arXiv: [https://arxiv.org/abs/2211.15229](https://arxiv.org/abs/2211.15229)



