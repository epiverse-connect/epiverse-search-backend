# Extract date from a character vector

```r
date_i_guess_and_convert(x)
```

## Arguments

- `x`: A `<vector>` of characters

## Returns

If the format cannot be resolved, the function returns `NA`; if a matching format is found, it returns the `<vector>` of the converted values.

This function tries converting a single character string into a well-formatted date, but still returning a character. If it can't convert it, it returns NA.
