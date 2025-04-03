# Assert an object is a valid `<epiparameter>` object

```r
assert_epiparameter(x)
```

## Arguments

- `x`: An object.

## Returns

Invisibly returns an `<epiparameter>`. Called for side-effects (errors when invalid `<epiparameter>` object is provided).

Assert an object is a valid `<epiparameter>` object

## Examples

```r
ep <- epiparameter_db(single_epiparameter = TRUE)
assert_epiparameter(ep)

# example with invalid <epiparameter>
ep$disease <- NULL
try(assert_epiparameter(ep))
```
