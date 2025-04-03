# `c()` method for `<epiparameter>` class

```r
## S3 method for class 'epiparameter'
c(...)

## S3 method for class 'multi_epiparameter'
c(...)
```

## Arguments

- `...`: dots Objects to be concatenated.

## Returns

An `<epiparameter>` or list of `<epiparameter>` objects.

`c()` method for `<epiparameter>` class

## Examples

```r
db <- epiparameter_db()

# combine two <epiparameter> objects into a list
c(db[[1]], db[[2]])

# combine a list of <epiparameter> objects and a single <epiparameter> object
c(db, db[[1]])
```
