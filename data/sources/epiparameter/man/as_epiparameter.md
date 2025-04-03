# Convert to an `<epiparameter>` object

```r
as_epiparameter(x, ...)
```

## Arguments

- `x`: an object used to select a method.
- `...`: dots Extra arguments to be passed to the method.

## Returns

An `<epiparameter>` object or list of `<epiparameter>` objects.

Convert from an object to an `<epiparameter>` object. If conversion is not possible the function will error.

## Details

To create the full citation the information from the article table from the `epireview` package of the corresponding entry will need to be passed to function via the `...` argument. The argument should be called `article`, as it will be matched by name by `$`.

To specify a probability distribution pass a `character` string to the function via the `...` argument. The argument should be called `prob_distribution`. For example, to specify a gamma distribution: `as_epiparameter(x, prob_distribution = "gamma")`.

**Warning**: distributions specified via the `prob_dist` argument will overwrite the probability distribution specified in the `x` argument. For example, if the probability distribution is given in an `epireview`

entry and the `prob_dist` argument is specified then the function may error or return an unparameterised `<epiparameter>` if the parameterisation becomes incompatible.

Valid probability distributions are: `"gamma"`, `"lnorm"`, `"weibull"`, `"nbinom"`, `"geom"`, `"pois"`, `"norm"`, `"exp"`.
