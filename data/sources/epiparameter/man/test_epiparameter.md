# Test whether an object is a valid `<epiparameter>` object

```r
test_epiparameter(x)
```

## Arguments

- `x`: An object.

## Returns

A boolean `logical` whether the object is a valid `<epiparameter>`

object (prints message when invalid `<epiparameter>` object is provided).

Test whether an object is a valid `<epiparameter>` object

## Examples

```r
ep <- epiparameter_db(single_epiparameter = TRUE)
test_epiparameter(ep)

# example with invalid <epiparameter>
ep$disease <- NULL
test_epiparameter(ep)
```
