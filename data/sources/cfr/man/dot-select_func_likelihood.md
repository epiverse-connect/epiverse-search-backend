# Select a likelihood function for severity estimation

```r
.select_func_likelihood(total_cases, poisson_threshold, p_mid)
```

## Arguments

- `total_cases`: A single count for the total number of cases in the outbreak.
- `poisson_threshold`: A single count for the threshold of cases above which a Poisson or Normal approximation is returned.
- `p_mid`: A single positive number bounded 0 -- 1, representing an initial estimate of the severity, which is used to determine whether a Poisson or Normal approximation is returned. determine whether

## Returns

A function with three arguments, `total_outcomes`, `total_deaths`, and `pp`, which is used to generate the profile likelihood. Also prints messages to the screen when a Poisson or Normal approximation function is returned.

Switches between Binomial, Poisson, and Normal approximation based on the total number of cases and an initial estimate of the severity.

## Details

Returns a likelihood function as follows:

 * Binomial approximation: when `total_cases \< poisson_threshold`, used when there are few cases, such as in a small outbreak;
 * Poisson approximation: when `total_cases \>= poisson_threshold` but when `p_mid` \< 0.05;
