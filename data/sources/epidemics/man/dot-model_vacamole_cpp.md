# Run the RIVM Vacamole model

```r
.model_vacamole_cpp(
  initial_state,
  transmission_rate,
  transmission_rate_vax,
  infectiousness_rate,
  mortality_rate,
  mortality_rate_vax,
  hospitalisation_rate,
  hospitalisation_rate_vax,
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
- `transmission_rate_vax`: The transmission rate `\beta_V` at which individuals who have received two vaccine doses are infected by the disease.
- `infectiousness_rate`: The rate of transition from exposed to infectious `\alpha`. This is common to fully susceptible, partially vaccinated, and fully vaccinated individuals (where fully vaccinated represents two doses).
- `mortality_rate`: The mortality rate of fully susceptible and partially vaccinated and unprotected individuals.
- `mortality_rate_vax`: The mortality rate of individuals who are protected by vaccination.
- `hospitalisation_rate`: The hospitalisation rate of fully susceptible and partially vaccinated and unprotected individuals.
- `hospitalisation_rate_vax`: The hospitalisation rate of individuals who are protected by vaccination.
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

Vacamole is a deterministic, compartmental epidemic model built by Kylie Ainslie and others at RIVM, the Dutch Public Health Institute for the Covid-19 pandemic, with a focus on scenario modelling for hospitalisation and vaccination. Model code: https://github.com/kylieainslie/vacamole Manuscript describing the model and its application: https://doi.org/10.2807/1560-7917.ES.2022.27.44.2101090 This function is intended to only be called internally from `model_vacamole_cpp()`.
