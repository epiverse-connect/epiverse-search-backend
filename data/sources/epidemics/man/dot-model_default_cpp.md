# Run an age-structured SEIR-V epidemic ODE model using a Boost solver

```r
.model_default_cpp(
  initial_state,
  transmission_rate,
  infectiousness_rate,
  recovery_rate,
  contact_matrix,
  npi_time_begin,
  npi_time_end,
  npi_cr,
  vax_time_begin,
  vax_time_end,
  vax_nu,
  rate_interventions,
  time_dependence,
  time_end = 100,
  increment = 1
)
```

## Arguments

- `initial_state`: A matrix for the initial state of the compartments.
- `transmission_rate`: The transmission rate `\beta` at which unvaccinated and partially vaccinated individuals are infected by the disease.
- `infectiousness_rate`: The rate of transition from exposed to infectious `\alpha`.
- `recovery_rate`: The recovery rate `\gamma`.
- `contact_matrix`: The population contact matrix.
- `npi_time_begin`: The start time of any non-pharmaceutical interventions .
- `npi_time_end`: The end time of any non-pharmaceutical interventions.
- `npi_cr`: The reduction in contacts from any non-pharmaceutical interventions.
- `vax_time_begin`: The start time of any vaccination campaigns.
- `vax_time_end`: The end time of any vaccination campaigns.
- `vax_nu`: The vaccination rate of any vaccination campaigns.
- `rate_interventions`: A named list of `<rate_intervention>` objects.
- `time_dependence`: A named list of functions for parameter time dependence.
- `time_end`: The end time of the simulation.
- `increment`: The time increment of the simulation.

## Returns

A two element list, where the first element is a list of matrices whose elements correspond to the numbers of individuals in each compartment as specified in the initial conditions matrix (see `population()`). The second list element is a vector of timesteps.

A compartmental model with an optional non-pharmaceutical intervention and an optional vaccination regime.

This function is intended to only be called internally from `model_default_cpp()`.
