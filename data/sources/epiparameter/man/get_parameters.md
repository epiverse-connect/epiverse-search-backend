# Get parameters from an object

```r
get_parameters(x, ...)
```

## Arguments

- `x`: an object used to select a method.
- `...`: dots Extra arguments to be passed to the method.

## Returns

A named vector of parameters or `NA` when the `<epiparameter>`

object is unparameterised, or a list where each element is a named vectors or `NA`.

Extract the parameters stored in an object.
