# Extends an incidence class object with incidence rates estimations.

```r
incidence_rate(incidence_object, level, scale = 1e+05)
```

## Arguments

- `incidence_object`: An incidence object.
- `level`: Administration level at which incidence counts are grouped (0 = national, 1 = state/department, 2 = city/municipality).
- `scale`: Scale to consider when calculating the incidence_rate.

## Returns

A modified incidence object where counts are normalized with the population.

Function that estimates incidence rates from a incidence class object and population projections.

## Examples

```r
data_event <- epiCo::epi_data
incidence_historic <- incidence::incidence(data_event$fec_not,
  groups = data_event$cod_mun_o,
  interval = "1 year"
)
incidence_object <- subset(incidence_historic,
  from = "2015-01-04",
  to = "2018-12-27"
)
inc_rate <- incidence_rate(incidence_object, level = 2, scale = 100000)
inc_rate$rates
```
