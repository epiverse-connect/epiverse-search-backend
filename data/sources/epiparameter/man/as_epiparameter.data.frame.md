# Convert `<data.frame>` to an `<epiparameter>` object

```r
## S3 method for class 'data.frame'
as_epiparameter(x, ...)
```

## Arguments

- `x`: A `<data.frame>`.
- `...`: dots Not used, extra arguments supplied will cause a warning.

## Returns

An `<epiparameter>` object or list of `<epiparameter>` objects.

Convert the tabular information in `<data.frame>` to an `<epiparameter>`. If the information in the `<data.frame>` cannot be converted into an `<epiparameter>` the function will error.

## Examples

```r
ep <- epiparameter_db(single_epiparameter = TRUE)
df <- as.data.frame(ep)
ep <- as_epiparameter(df)
```
