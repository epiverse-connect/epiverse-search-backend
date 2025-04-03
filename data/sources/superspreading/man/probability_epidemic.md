# Calculate the probability a disease will cause an outbreak based on R, k and initial cases

```r
probability_epidemic(
  R,
  k,
  num_init_infect,
  ind_control = 0,
  pop_control = 0,
  ...,
  offspring_dist
)
```

## Arguments

- `R`: A `number` specifying the R parameter (i.e. average secondary cases per infectious individual).
- `k`: A `number` specifying the k parameter (i.e. overdispersion in offspring distribution from fitted negative binomial).
- `num_init_infect`: An `integer` (or at least ["integerish"](https://rlang.r-lib.org/reference/is_integerish.html) if stored as double) specifying the number of initial infections.
- `ind_control`: A `numeric` specifying the strength of individual-level control measures. These control measures assume that infected individuals do not produce any secondary infections with probability `ind_control`, thus increasing the proportion of cases that do not create any subsequent infections. The control measure is between `0` (default) and `1` (maximum).
- `pop_control`: A `numeric` specifying the strength of population-level control measures that reduce the transmissibility of all cases by a constant factor. Between `0` (default) and `1` (maximum).
- `...`: <`dynamic-dots`> Named elements to replace default optimisation settings. Currently only `"fit_method"` is accepted and can be either `"optim"` (default) or `"grid"` for numerical optimisation routine or grid search, respectively.
- `offspring_dist`: An `<epiparameter>` object. An S3 class for working with epidemiological parameters/distributions, see `epiparameter::epiparameter()`.

## Returns

A value with the probability of a large epidemic.

Calculates the probability a branching process will cause an epidemic (i.e. probability will fail to go extinct) based on R, k and initial cases.

## Examples

```r
probability_epidemic(R = 1.5, k = 0.1, num_init_infect = 10)
```

## References

Lloyd-Smith, J. O., Schreiber, S. J., Kopp, P. E., & Getz, W. M. (2005) Superspreading and the effect of individual variation on disease emergence. Nature, 438(7066), 355-359. tools:::Rd_expr_doi("10.1038/nature04153")

Kucharski, A. J., Russell, T. W., Diamond, C., Liu, Y., Edmunds, J., Funk, S. & Eggo, R. M. (2020). Early dynamics of transmission and control of COVID-19: a mathematical modelling study. The Lancet Infectious Diseases, 20(5), 553-558. tools:::Rd_expr_doi("10.1016/S1473-3099(20)30144-4")

## See Also

`probability_extinct()`
