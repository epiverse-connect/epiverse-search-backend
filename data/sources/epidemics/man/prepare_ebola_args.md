# Prepare arguments to ebola model function

```r
.check_prepare_args_ebola(mod_args)
```

## Arguments

- `mod_args`: A named list of composable elements; must include a `<population>`.

## Returns

A list of model arguments suitable for `.model_ebola_internal()`, if all elements of `mod_args` are suitable for the Ebola model. If any of the model composable elements are not suitable, has the side-effect of throwing errors to the user. If any elements of `mod_args` are `NULL`, returns dummy placeholder values for those elements.

The returned list of prepared model arguments is a named list consisting of:

 * `"initial_state"`: the initial conditions of the simulation, which is the number of individuals in each compartment. No age stratification allowed.
 * `"intervention"`: either a list of `\<rate_intervention\>` objects, or a dummy `\<rate_intervention\>` if there are no interventions specified by the user.
 * `"time_dependence"`: the time-dependence composable element passed by the user. Input checks on this element occur in the higher level model function.

Prepare arguments to `model_ebola()` for `.model_ebola_internal()`.

## Details

`.check_prepare_args_ebola()` prepares arguments for `.model_ebola_internal()`, by converting some of the arguments collected in `mod_args` into simpler structures that are appropriate for the internal model function.
