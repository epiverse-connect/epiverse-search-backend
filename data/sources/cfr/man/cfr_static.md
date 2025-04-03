# Estimate a static disease severity measure

```r
cfr_static(data, delay_density = NULL, poisson_threshold = 100)
```

## Arguments

- `data`: A `<data.frame>` containing the outbreak data. A daily time series with dates or some other absolute indicator of time (e.g. epiday or epiweek) and the numbers of new cases and new deaths at each time point. Note that the required columns are "date" (for the date), "cases" (for the number of reported cases), and "deaths" (for the number of reported deaths) on each day of the outbreak.
    
    Note that the `<data.frame>` is required to have an unbroken sequence of dates with no missing dates in between. The "date" column must be of class `Date` (see `as.Date()`).
    
    Note also that the total number of cases must be greater than the total number of reported deaths.
- `delay_density`: An optional argument that controls whether delay correction is applied in the severity estimation. May be `NULL`, for no delay correction, or a function that returns the density function of a distribution to evaluate density at user-specified values, e.g. `function(x) stats::dgamma(x = x, shape = 5, scale = 1)`.
- `poisson_threshold`: The case count above which to use Poisson approximation. Set to 100 by default. Must be > 0.

## Returns

A `<data.frame>` with the maximum likelihood estimate and 95% confidence interval of the severity estimates, named "severity_estimate", "severity_low", and "severity_high".

Calculates the severity of a disease, while optionally correcting for reporting delays using an epidemiological delay distribution of the time between symptom onset and death (onset-to-death).

Other delay distributions may be passed to calculate different disease severity measures such as the hospitalisation fatality risk.

## Details: Adjusting for delays between two time series

The method used in `cfr_static()` follows Nishiura et al. (2009). The function calculates a quantity `u_t` for each day within the input data, which represents the proportion of cases estimated to have a known outcome on day `t`. Following Nishiura et al., `u_t` is calculated as: c("`u_t = \\dfrac{\\sum_{i = 0}^t\n`", "`        \\sum_{j = 0}^\\infty c_i f_{j - i}}{\\sum_{i = 0} c_i}`")

where `f_t` is the value of the probability mass function at time `t`

and `c_t`, `d_t` are the number of new cases and new deaths at time `t`, (respectively). We then use `u_t` at the end of the outbreak in the following likelihood function to estimate the severity of the disease in question. c("`{\\sf L}({\\theta \\mid y}) = \\log{\\dbinom{u_tC}{D}} + D \\log{\\theta} +\n`", "`  (u_tC - D)\\log{(1.0 - \\theta)}`")

`C` and `D` are the cumulative number of cases and deaths (respectively) up until time `t`. `\theta` is the parameter we wish to estimate, the severity of the disease. We estimate `\theta` using simple maximum-likelihood methods, allowing the functions within this package to be quick and easy tools to use.

The precise severity measure — CFR, IFR, HFR, etc — that `\theta`

represents depends upon the input data given by the user.

The epidemiological delay-distribution density function passed to `delay_density` is used to evaluate the probability mass function parameterised by time; i.e. `f(t)` which gives the probability that a case has a known outcome (usually death) at time `t`, parameterised with disease-specific parameters before it is supplied here.

### Profile likelihood methods

The naive CFR estimate (without delay correction) is the outcome of a Binomial test on deaths and cases using `stats::binom.test()`. The confidence intervals around the estimate are also taken from the test.

The delay-corrected CFR estimates are however obtained by generating a profile likelihood over the sequence `seq(1e-4, 1.0, 1e-4)`. The method used depends on the outbreak size and the initial expectation of disease severity. This is implemented in the internal function `.estimate_severity()`.

 * Delay correction, small outbreaks : For outbreaks where the total cases are below the user-specified 'Poisson threshold' (`poisson_threshold`, default = 100), the CFR and uncertainty around it is taken from a profile likelihood generated from a Binomial model of deaths (successes) and estimated known outcomes (trials).
   
    * Delay correction, large outbreaks with low severity : For outbreaks with total cases greater than the Poisson threshold (default = 100) and with initial severity estimates \\< 0.05, the CFR and uncertainty are taken from a Poisson approximation of the Binomial profile likelihood (taking `\lambda = np` for `n` estimated outcomes and `p` as the severity estimate).
 * Delay correction, large outbreaks with higher severity : For outbreaks with total cases greater than the Poisson threshold (default = 100) and with initial severity estimates `\geq` 0.05, the CFR and uncertainty are taken from a Normal approximation of the Binomial profile likelihood.

## Examples

```r
# load package data
data("ebola1976")

# estimate severity without correcting for delays
cfr_static(ebola1976)

# estimate severity for each day while correcting for delays
# obtain onset-to-death delay distribution parameters from Barry et al. 2018
# The Lancet. <https://doi.org/10.1016/S0140-6736(18)31387-4>
cfr_static(
  ebola1976,
  delay_density = function(x) dgamma(x, shape = 2.40, scale = 3.33)
)
```

## References

Nishiura, H., Klinkenberg, D., Roberts, M., & Heesterbeek, J. A. P. (2009). Early Epidemiological Assessment of the Virulence of Emerging Infectious Diseases: A Case Study of an Influenza Pandemic. PLOS ONE, 4(8), e6852. tools:::Rd_expr_doi("10.1371/journal.pone.0006852")
