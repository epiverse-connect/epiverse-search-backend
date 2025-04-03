# Get the underlying distributions names from a `<distribution>` object from the `distributional` package in distribution naming convention.

```r
.distributional_family(x, base_dist = TRUE)
```

## Arguments

- `x`: An `<distribution>` object.
- `base_dist`: A boolean `logical` for whether to return the name of a transformed distribution (e.g. `"mixture"` or `"truncated"`) or the underlying distribution type (e.g. `"gamma"` or `"lnorm"`). Default is `TRUE`.

## Returns

A `character` vector.

Get the underlying distributions names from a `<distribution>` object from the `distributional` package in distribution naming convention.

## Details

Get and standardise distribution name. For untransformed distributions (e.g. `distributional::dist_gamma()`) it will return the distribution name. For transformed distributions (e.g. `distributional::dist_mixture()`) it will get the name of the underlying distribution(s) by default (`base_dist = TRUE`). Distribution names are returned in the naming style (e.g. lognormal is `"lnorm"`). When `base_dist = FALSE` transformed distributions return the name of the transformation (e.g. `"mixture"`).
