# Sample names using `randomNames::randomNames()`

```r
.sample_names(.data, buffer_factor = 1.5)
```

## Arguments

- `.data`: A `<data.frame>` containing the infectious history from a branching process simulation (`.sim_network_bp()`).
- `buffer_factor`: A single `numeric` determining the level of oversampling (or buffer) when creating a vector of unique names from `randomNames::randomNames()`.

## Returns

A `character` vector.

Sample names for specified sexes by sampling with replacement to avoid exhausting number of name when `sample.with.replacement = FALSE`. The duplicated names during sampling need to be removed to ensure each individual has a unique name. In order to have enough unique names, more names than required are sampled from `randomNames::randomNames()`, and the level of oversampling is determined by the `buffer_factor` argument. A `buffer_factor` too high and the more names are sampled which takes longer, a `buffer_factor` too low and not enough unique names are sampled and the `.sample_names()` function will need to loop until it has enough unique names.
