# Prepare arguments to default model function

```r
.check_prepare_args_default(mod_args)
```

## Arguments

- `mod_args`: A named list of the population, and epidemic modifiers.

## Returns

A list of model arguments suitable for `.model_default_cpp()`. This is a named list consisting of:

 * `initial_state`: the initial conditions modified to represent absolute rather than proportional values;
 * `transmission_rate`, `infectiousness_rate`, `recovery_rate`: three numbers representing the transmission rate of the infection, the rate of transition from exposed to infectious, and the recovery rate, respectively;
 * `contact_matrix`, a numeric matrix for the population contact matrix scaled by the largest real eigenvalue and by the size of each groups;
 * `npi_time_begin`, `npi_time_end`: two vectors for the start and end times of any interventions applied;
 * `npi_cr`: a matrix for the age- and intervention-specific effect on social contacts;
 * `vax_time_begin`,`vax_time_end`, `vax_nu`: three numeric matrices for the age- and dose-specific start times, end times, and rates of any vaccination doses implemented;
 * `time_end`, `increment`: two numbers for the time at which to end the simulation, and the value by which the simulation time is incremented.

Prepare arguments to `model_default()` for `.model_default_cpp()`.

## Details

`.check_prepare_args_default()` prepares arguments for `.model_default_cpp()`, which is the C++ function that solves the default ODE system using a Boost **odeint** solver, by converting some of the arguments collected in `mod_args` into simpler structures such as lists and numeric or integer vectors that can be interpreted as C++ types such as `Rcpp::List`, `Rcpp::NumericVector`, or `Eigen::MatrixXd`.
