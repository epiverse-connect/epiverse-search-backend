# `lines()` method for `<epiparameter>` class

```r
## S3 method for class 'epiparameter'
lines(x, cumulative = FALSE, ...)
```

## Arguments

- `x`: An `<epiparameter>` object.
- `cumulative`: A boolean `logical`, default is `FALSE`. `cumulative = TRUE` plots the cumulative distribution function (CDF).
- `...`: further arguments passed to or from other methods.

## Returns

These functions are invoked for their side effect of drawing on the active graphics device.

`lines()` method for `<epiparameter>` class

## Examples

```r
ebola_si <- epiparameter_db(disease = "Ebola", epi_name = "serial")
plot(ebola_si[[1]])
lines(ebola_si[[2]])
```
