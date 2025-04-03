# `plot()` method for `<multi_epiparameter>` class

```r
## S3 method for class 'multi_epiparameter'
plot(x, cumulative = FALSE, ...)
```

## Arguments

- `x`: A `<multi_epiparameter>` object.
- `cumulative`: A boolean `logical`, default is `FALSE`. `cumulative = TRUE` plots the cumulative distribution function (CDF).
- `...`: further arguments passed to or from other methods.

## Returns

These functions are invoked for their side effect of drawing on the active graphics device.

Plots a list of `<epiparameter>` objects by overlaying their distributions.

## Details

Unparameterised and discrete `<epiparameter>` objects are not plotted (see `is_parameterised()` and `is_continuous()`).

## Examples

```r
ebola_si <- epiparameter_db(disease = "Ebola", epi_name = "serial")
plot(ebola_si)
```

## Author(s)

Joshua W. Lambert
