# Extract specified loo estimate

```r
summarise_loo_estimate(
  seromodel,
  par_loo_estimate = "elpd_loo",
  loo_estimate_digits = 2
)
```

## Arguments

- `seromodel`: stan_fit object obtained from sampling a model with fit_seromodel
- `par_loo_estimate`: Name of the loo estimate to be extracted. Available options are:
    
    - **`"elpd_loo"`**: Expected log pointwise predictive density
    - **`"p_loo"`**: Effective number of parameters
    - **`"looic"`**: Leave-one-out cross-validation information criteria
    
    For additional information refer to loo .
- `loo_estimate_digits`: Number of loo estimate digits

## Returns

Text summarising specified loo estimate

Extract specified loo estimate

## Examples

```r
data(veev2012)
seromodel <- fit_seromodel(veev2012, iter = 100)
summarise_loo_estimate(seromodel)
```
