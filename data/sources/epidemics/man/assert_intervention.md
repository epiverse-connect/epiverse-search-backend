# Assert properties of a `intervention` object

```r
assert_intervention(x, type = c("contacts", "rate"), population = NULL)
```

## Arguments

- `x`: A intervention object.
- `type`: A string for the type of intervention to check for. May be one of `"contacts"` or `"rate"`.
- `population`: An optional argument which is a population object. When present, this is used to check whether the intervention object `x` has corresponding values of `reduction` for each demographic group in `population`.

## Returns

Silently returns the `<intervention>`-superclass object `x` of the same class as `x`, i.e., `<rate_intervention>` or `<contacts_intervention>`. Primarily called for its side effects of throwing errors when `x` does not meet certain requirements.

Assert that objects of the `intervention` class have the properties expected by an epidemic model. See `intervention()` and specific model functions to check the intervention properties required by each model. This function is for internal use in argument checking functions.
