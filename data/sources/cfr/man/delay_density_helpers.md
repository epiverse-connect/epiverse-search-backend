# Check delay density functions passed to exported functions

```r
test_fn_req_args(fn, n_req_args = 1)

test_fn_num_out(fn, n = 10)
```

## Arguments

- `fn`: A function. This is expected to be a function evaluating the density of a distribution at numeric values, and suitable to be passed to `delay_density` in `cfr_*()`.
- `n_req_args`: The number of required arguments, i.e., arguments without default values.
- `n`: The number of elements over which to evaluate the function `fn`. Defaults to 10, and `fn` is evaluated over `seq(n)`.

## Returns

A logical for whether the function `fn` fulfils conditions specified in the respective checks.

Internal helper function that check whether a function passed to the `delay_density` argument in `cfr_*()` or `estimate_outcomes()` meet the requirements of package methods.

`test_fn_req_args()` checks whether the function has only the expected number of required arguments, i.e., arguments without default values. Defaults to checking for a single required argument.

`test_fn_num_out()` checks whether the function returns a numeric output consistent with evaluating the probability density or probability mass function of a distribution over a sequence of values. Expects that the function returns a numeric vector of finite values `\geq` 0.0, that no values are missing, and that the output vector is the same length as the input vector.
