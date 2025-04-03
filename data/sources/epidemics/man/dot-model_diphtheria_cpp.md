# Run an SEIHR ODE model for diphtheria using a Boost solver

```r
.model_diphtheria_cpp(
  initial_state,
  transmission_rate,
  infectiousness_rate,
  recovery_rate,
  reporting_rate,
  prop_hosp,
  hosp_entry_rate,
  hosp_exit_rate,
  rate_interventions,
  time_dependence,
  pop_change_times,
  pop_change_values,
  time_end = 100,
  increment = 1
)
```

## Arguments

- `initial_state`: A matrix for the initial state of the compartments.
- `transmission_rate`: The transmission rate `\beta`.
- `infectiousness_rate`: The rate of transition from exposed to infectious `\alpha`.
- `recovery_rate`: The recovery rate `\gamma`.
- `reporting_rate`: The recovery rate `\r`.
- `prop_hosp`: The proportion of individuals hospitalised `\eta`.
- `hosp_entry_rate`: The rate at which individuals are hospitalised, represented as 1 / time to hospitalisation `\tau_1`.
- `hosp_exit_rate`: The rate at which individuals are discharged from hospital, represented as 1 / time to discharge `\tau_2`.
- `rate_interventions`: A named list of `<rate_intervention>` objects.
- `time_dependence`: A named list of functions for parameter time dependence.
- `pop_change_times`: A numeric vector of times and which the population of susceptibles changes.
- `pop_change_values`: An Rcpp List of numeric vectors giving the value of changes to each demographic group at each change in population.
- `time_end`: The end time of the simulation.
- `increment`: The time increment of the simulation.

## Returns

A two element list, where the first element is a list of matrices whose elements correspond to the numbers of individuals in each compartment as specified in the initial conditions matrix. The second list element is a vector of timesteps.

A compartmental model for diphtheria with parameters to help account for case reporting rate, delays in seeking hospitalisation, and the time spent in the hospitalised compartment.

This function is intended to only be called internally from `model_diphtheria_cpp()`.
