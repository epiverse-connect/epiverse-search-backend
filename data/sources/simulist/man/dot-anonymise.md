# Anonymise names

```r
.anonymise(x, string_len = 10)
```

## Arguments

- `x`: A vector of `character` strings.
- `string_len`: A single `numeric` specifying the number of alphanumeric characters to use for each anonymising `character` string. Default is `10`.

## Returns

A vector of `character` strings of equal length to the input.

A simple algorithm to replace names with an alphanumeric string with an fixed number of characters (i.e. `nchar()`) specified by `string_len`.
