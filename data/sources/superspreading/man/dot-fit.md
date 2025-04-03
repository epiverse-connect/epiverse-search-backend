# Optimise a function using either numerical optimisation or grid search

```r
.fit(func, fit_method = c("optim", "grid"), ...)
```

## Arguments

- `func`: A `function`.
- `fit_method`: A `character` string, either `"optim"` or `"grid"`.
- `...`: <`dynamic-dots`> Named elements to replace default optimisation settings for either `optim()` or grid search. See details.

## Returns

A single `numeric`.

Optimise a function using either numerical optimisation or grid search

## Details

Arguments passed through dots depend on whether `fit_method` is set to `"optim"` or `"grid"`. For `"optim"`, arguments are passed to `optim()`, for `"grid"`, the variable arguments are `lower`, `upper` (lower and upper bounds on the grid search for the parameter being optimised, defaults are `lower = 0.001` and `upper = 0.999`), and `"res"` (the resolution of grid, default is `res = 0.001`).
