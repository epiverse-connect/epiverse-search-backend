# Estimate static severity for an expanding time series

```r
cfr_rolling(data, delay_density = NULL, poisson_threshold = 100)
```

## Arguments

- `data`: A `<data.frame>` containing the outbreak data. A daily time series with dates or some other absolute indicator of time (e.g. epiday or epiweek) and the numbers of new cases and new deaths at each time point. Note that the required columns are "date" (for the date), "cases" (for the number of reported cases), and "deaths" (for the number of reported deaths) on each day of the outbreak.
    
    Note that the `<data.frame>` is required to have an unbroken sequence of dates with no missing dates in between. The "date" column must be of class `Date` (see `as.Date()`).
    
    Note also that the total number of cases must be greater than the total number of reported deaths.
- `delay_density`: An optional argument that controls whether delay correction is applied in the severity estimation. May be `NULL`, for no delay correction, or a function that returns the density function of a distribution to evaluate density at user-specified values, e.g. `function(x) stats::dgamma(x = x, shape = 5, scale = 1)`.
- `poisson_threshold`: The case count above which to use Poisson approximation. Set to 100 by default. Must be > 0.

## Returns

A `<data.frame>` with the date, maximum likelihood estimate and 95% confidence interval of the daily severity estimates, named "severity_estimate", "severity_low", and "severity_high", with one row for each day in the original data.frame.

Calculates the CFR at each time point in the case and death time series supplied, using an expanding window of time. The static CFR is calculated for each time point, using the time series from the start to each time point, and increasing the number of time points included by one in each iteration.

## Details

When delay correction is applied by passing a delay distribution density function to `delay_density`, the internal function `.estimate_severity()` is used to calculate the rolling severity.

Note that in the naive method the severity estimate and confidence intervals cannot be calculated for days on which the cumulative number of cases since the start of the time-series, and for days on which the cumulative number of deaths reported exceeds the cumulative reported cases, and is returned as `NA`.

`cfr_rolling()` applies the internal function `.estimate_severity()` to an expanding time-series of total cases, total estimated outcomes, and total deaths. The method used to generate a profile likelihood for each day depends on the outbreak size and initial severity estimate for that day. This is essentially the same as running `cfr_static()` on each new day. The method used for each day is not communicated to the user, in order to prevent cluttering the terminal with messages.

## Examples

```r
# load package data
data("ebola1976")

# estimate severity without correcting for delays
cfr_static(ebola1976)

# estimate severity for each day while correcting for delays
# obtain onset-to-death delay distribution parameters from Barry et al. 2018
# The Lancet. <https://doi.org/10.1016/S0140-6736(18)31387-4>
# view only the first values
estimate <- cfr_rolling(
  ebola1976,
  delay_density = function(x) dgamma(x, shape = 2.40, scale = 3.33)
)

head(estimate)
```
