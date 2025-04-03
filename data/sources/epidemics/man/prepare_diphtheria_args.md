# Prepare arguments to diphtheria model function

```r
.check_prepare_args_diphtheria(mod_args)
```

## Arguments

- `mod_args`: A named list of the population, and epidemic modifiers.

## Returns

A list of model arguments suitable for `.model_diphtheria_cpp()`. This is a named list consisting of:

 * `initial_state`: the initial conditions modified to represent absolute rather than proportional values;
 * `transmission_rate`, `transmission_rate_vax`: two numbers representing the transmission rate of the infection for unvaccinated or single-dose vaccinated, and two-dose vaccinated individuals, respectively;
 * `infectiousness_rate`: a single number for the transition rate from the 'exposed' and 'exposed_vaccinated' to the 'infectious' and 'infectious_vaccinated' compartments;
 * `recovery_rate`: a single number for the recovery rate from the infection;
 * `reporting_rate`: a single number for the proportion of infectious cases reported;
 * `prop_hosp`: a single number for the proportion of reported cases that need hospitalisation;
 * `hosp_entry_rate`, `hosp_exit_rate`: two numbers representing the rate of entry and exit from the 'hospitalised' compartment;
 * `rate_interventions`: an Rcpp List giving the interventions on model parameters;
 * `time_dependence`: an Rcpp List giving the time-dependent effects on model parameters in the form of R functions;
 * `pop_change_times` and `pop_change_values`: the times and values of changes in the population of susceptibles;
 * `time_end`, `increment`: two numbers for the time at which to end the simulation, and the value by which the simulation time is incremented.

Prepare arguments to `model_diphtheria()` for `.model_diphtheria_cpp()`.

## Details

`.check_prepare_args_diphtheria()` prepares arguments for `.model_diphtheria_cpp()`, which is the C++ function that solves the ODE system using a Boost **odeint** solver, by converting the arguments collected in `mod_args` into simpler structures such as lists and numeric or integer vectors that can be interpreted as C++ types such as `Rcpp::List`, `Rcpp::NumericVector`, or `Eigen::MatrixXd`.
