# Get the lower and upper percentiles with a preference for symmetrical percentiles

```r
.get_sym_percentiles(percentiles)
```

## Arguments

- `percentiles`: A named vector of percentiles. The names are in the correct format to be converted to their numeric value using `as.numeric()`.

## Returns

A named `numeric` vector of two elements with the lower (first element) and upper (second element) percentiles.

Get the lower and upper percentiles with a preference for symmetrical percentiles
