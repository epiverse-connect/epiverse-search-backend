# Provides the sociological description of ethnicities in Colombia

```r
describe_ethnicity(ethnic_codes)
```

## Arguments

- `ethnic_codes`: A numeric vector with the codes of ethnicities to consult

## Returns

A printed message with ethnicities descriptions

Function that returns the description of the consulted ethnicities

## Examples

```r
describe_ethnicity(round(runif(n = 150, min = 1, max = 4)))
```
