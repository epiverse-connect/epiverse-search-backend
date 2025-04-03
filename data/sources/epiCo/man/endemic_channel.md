# Create and return the endemic channel of a disease from an incidence object

```r
endemic_channel(
  incidence_historic,
  observations = NULL,
  method = c("geometric", "median", "mean", "unusual_behavior"),
  geometric_method = "shifted",
  outlier_years = NULL,
  outliers_handling = c("ignored", "included", "replaced_by_median", "replaced_by_mean",
    "replaced_by_geometric_mean"),
  ci = 0.95,
  plot = FALSE
)
```

## Arguments

- `incidence_historic`: An incidence object with the historic weekly observations
- `observations`: A numeric vector with the current observations
- `method`: A string with the mean calculation method of preference (median, mean, or geometric) or to use the unusual behavior method (Poisson Distribution Test for Hypoendemic settings)
- `geometric_method`: A string with the selected method for geometric mean calculation; see: geometric_mean
- `outlier_years`: A numeric vector with the outlier years
- `outliers_handling`: A string with the handling decision regarding outlier years, see: outliers_handling function
- `ci`: = 0.95 A numeric value to specify the confidence interval to use with the geometric method
- `plot`: A boolean for displaying a plot

## Returns

A dataframe with the observation, historical mean, and confidence intervals (or risk areas)

Function that builds the endemic channel of a disease time series based on the selected method and windows of observation

## Examples

```r
data_event <- epiCo::epi_data
data_ibague <- data_event[data_event$cod_mun_o == 73001, ]
incidence_historic <- incidence::incidence(data_ibague$fec_not,
  interval = "1 epiweek"
)
endemic_channel(incidence_historic,
  method = "geometric", plot = TRUE
)
```
