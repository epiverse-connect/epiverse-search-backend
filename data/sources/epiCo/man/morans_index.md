# Calculate spatial correlation of given municipalities in an incidence_rate object.

```r
morans_index(incidence_object, scale = 1e+05, threshold = 2, plot = TRUE)
```

## Arguments

- `incidence_object`: An incidence object with one observation for the different locations (groups).
- `scale`: Scale to consider when calculating the incidence_rate.
- `threshold`: Maximum traveling time around each municipality.
- `plot`: if TRUE, returns a plot of influential observations in the Moran's plot.

## Returns

List of Moran's I clustering analysis, giving the quadrant of each observation, influential values.

Function to calculate spatial autocorrelation via Moran's Index from a given incidence_rate object grouped by municipality.

## Examples

```r
data_event <- epiCo::epi_data
incidence_historic <- incidence::incidence(data_event$fec_not,
  groups = data_event$cod_mun_o,
  interval = "4 year"
)
incidence_object <- subset(incidence_historic,
  from = "2015-01-04",
  to = "2018-12-27"
)
morans_index(incidence_object, scale = 100000, threshold = 2, plot = TRUE)
```
