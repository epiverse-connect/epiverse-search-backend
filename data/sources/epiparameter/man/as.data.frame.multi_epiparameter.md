# `as.data.frame()` method for `<multi_epiparameter>` class

```r
## S3 method for class 'multi_epiparameter'
as.data.frame(x, ...)
```

## Arguments

- `x`: A `<multi_epiparameter>` object.
- `...`: dots Not used, extra arguments supplied will cause a warning.

## Returns

A `<data.frame>` with as many rows as length of input list.

`as.data.frame()` method for `<multi_epiparameter>` class

## Details

The `<data.frame>` returned will contain some atomic columns (i.e. one object per row), and other columns that are lists (i.e. multiple objects per row). The list columns can contain lists or S3 objects (e.g. `<bibentry>`

object in the `citation` column).

## Examples

```r
db <- epiparameter_db()
as.data.frame(db)
```
