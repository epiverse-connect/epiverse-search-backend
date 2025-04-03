# Convert a list to a vaccination object

```r
as.vaccination(x)
```

## Arguments

- `x`: A list, or an object that inherits from a list.

## Returns

A vaccination class object.

Convert a list to a vaccination object

## Examples

```r
# prepare a list
vax <- list(
  name = "vax_regime",
  time_begin = matrix(1),
  time_end = matrix(100),
  nu = matrix(0.001)
)

as.vaccination(vax)
```
