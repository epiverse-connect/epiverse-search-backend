# Check whether the optimisation of distribution parameters has converged to stable value for the parameters and function output for multiple iterations

```r
.check_optim_conv(optim_params_list, optim_params, tolerance)
```

## Arguments

- `optim_params_list`: A list, where each element is the output of `stats::optim()`. See `?optim` for more details.
- `optim_params`: A list given by the output of `stats::optim()`.
- `tolerance`: A `numeric` specifying within which disparity convergence of parameter estimates and function minimisation is accepted.

## Returns

Boolean

This function is to try and prevent optimisation to a local optimum and thus checks whether multiple optimisation routines are consistently finding parameter values to within a set tolerance.
