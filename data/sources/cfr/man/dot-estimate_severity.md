# Estimate the corrected case fatality risk

```r
.estimate_severity(
  total_cases,
  total_deaths,
  total_outcomes,
  poisson_threshold,
  p_mid = total_deaths/round(total_outcomes)
)
```

## Arguments

- `total_cases`: The total number of cases observed over the period of an outbreak of interest. The total number of cases must be greater than or equal to the total number of deaths.
- `total_deaths`: The total number of deaths observed over the period of an outbreak of interest. The total number of deaths must be less than or equal to the total number of cases.
- `total_outcomes`: The total number of outcomes expected to be observed over the period of an outbreak of interest. See `estimate_outcomes()`.
- `poisson_threshold`: The case count above which to use Poisson approximation. Set to 100 by default. Must be > 0.
- `p_mid`: The initial severity estimate, which is used to determine the likelihood approximation used when `total_cases` > `poisson_threshold`. Defaults to `total_deaths / round(total_outcomes)`.

## Returns

A `<data.frame>` with one row and three columns for the maximum likelihood estimate and 95% confidence interval of the corrected severity estimates, named "severity_estimate", "severity_low", and "severity_high".

Estimates the maximum likelihood estimate and 95% confidence interval of a corrected severity, using the total cases and total cases with known outcomes, where the latter replaces the total number of deaths in the standard (naive) severity definition. We use a binomial likelihood, approximated by a Poisson likelihood for large samples.

## Details

### Special cases

 * When any two of `total_cases`, `total_deaths`, or `total_outcomes` are 0, the estimate and confidence intervals cannot be calculated and the output `\<data.frame\>` contains only `NA`s.
 * When `total_outcomes \<= total_deaths`, estimate and confidence intervals cannot be reliably calculated and are returned as `NA`.
