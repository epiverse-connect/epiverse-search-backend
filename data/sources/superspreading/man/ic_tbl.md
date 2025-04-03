# Helper function to create a model comparison table

```r
ic_tbl(..., sort_by = c("AIC", "BIC", "none"))
```

## Arguments

- `...`: dots One or more model fit results from `fitdistrplus::fitdist()`.
- `sort_by`: A `character` string specifying which information criterion to order the table by, either `"AIC"` (default), `"BIC"`, or `"none"`
    
    (i.e. no ordering).

## Returns

A `<data.frame>`.

This is a helper function for creating a model comparison `<data.frame>` primarily for use in the `superspreading` vignettes. It is designed specifically for handling `fitdistrplus::fitdist()` output and not a generalised function. See `bbmle::ICtab()` for a more general use function to create information criteria tables.

## Examples

```r
if (requireNamespace("fitdistrplus", quietly = TRUE)) {
  cases <- rnbinom(n = 100, mu = 5, size = 0.7)
  pois_fit <- fitdistrplus::fitdist(data = cases, distr = "pois")
  geom_fit <- fitdistrplus::fitdist(data = cases, distr = "geom")
  nbinom_fit <- fitdistrplus::fitdist(data = cases, distr = "nbinom")
  ic_tbl(pois_fit, geom_fit, nbinom_fit)
}
```
