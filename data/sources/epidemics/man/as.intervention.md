# Convert a list to a intervention object

```r
as.intervention(x, type = c("contacts", "rate"))
```

## Arguments

- `x`: A list, or an object that inherits from a list.
- `type`: A string for the type of intervention: `"contacts"` for a `<contact_intervention>` or `"rate"` for a `<rate_intervention>`.

## Returns

A intervention class object.

Convert a list to a intervention object

## Examples

```r
# prepare a list
npi <- list(
  name = "npi",
  type = "contacts",
  time_begin = 30,
  time_end = 60,
  reduction = rep(0.1, 3)
)

as.intervention(npi)
```
