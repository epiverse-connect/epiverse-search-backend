# `as.data.frame()` method for `<epiparameter>` class

```r
## S3 method for class 'epiparameter'
as.data.frame(x, ...)
```

## Arguments

- `x`: An `<epiparameter>` object.
- `...`: dots Not used, extra arguments supplied will cause a warning.

## Returns

A `<data.frame>` with a single row.

`as.data.frame()` method for `<epiparameter>` class

## Details

The `<data.frame>` returned will contain some atomic columns (i.e. one object per row), and other columns that are lists (i.e. multiple objects per row). The list columns can contain lists or S3 objects (e.g. `<bibentry>`

object in the `citation` column).

## Examples

```r
ep <- epiparameter_db(single_epiparameter = TRUE)
as.data.frame(ep)
```
