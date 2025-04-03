# Standardise the variables input by users

```r
.clean_string(x)
```

## Arguments

- `x`: A `character` string.

## Returns

A `character` vector of equal length to the input.

Checks a user has supplied a `character` string and converts to `epiparameter` standards: lower-case and whitespace instead of dashes or underscores.

Examples of strings needing to be cleaned are: disease and pathogen names, and epidemiological distributions.
