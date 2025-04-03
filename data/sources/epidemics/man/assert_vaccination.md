# Assert properties of a `vaccination` object

```r
assert_vaccination(x, doses, population = NULL)
```

## Arguments

- `x`: A vaccination object.
- `doses`: The number of doses expected in the vaccination object.
- `population`: An optional argument which is a `<population>` object. When present, this is used to check whether the vaccination object `x` has corresponding values for each demographic group in `population`.

## Returns

Silently returns the `<vaccination>` object `x`. Primarily called for its side effects of throwing errors when `x` does not meet certain requirements.

Assert that objects of the `vaccination` class have the parameters expected by an epidemic model. See `vaccination()` and specific epidemic functions to check the vaccination properties required by each model. This function is for internal use in argument checking functions.
