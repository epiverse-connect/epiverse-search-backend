# Plot method for `<epiparameter>` class

```r
## S3 method for class 'epiparameter'
plot(x, cumulative = FALSE, ...)
```

## Arguments

- `x`: An `<epiparameter>` object.
- `cumulative`: A boolean `logical`, default is `FALSE`. `cumulative = TRUE` plots the cumulative distribution function (CDF).
- `...`: further arguments passed to or from other methods.

## Returns

These functions are invoked for their side effect of drawing on the active graphics device.

Plot an `<epiparameter>` object by displaying the either the probability mass function (PMF), (in the case of discrete distributions) or probability density function (PDF) (in the case of continuous distributions), or the cumulative distribution function (CDF).

## Details

By default if the `xlim` argument is not specified the distribution is plotted between day 0 and the 99th quantile of the distribution. Alternatively, a `numeric` vector of length 2 with the first and last day to plot on the x-axis can be supplied to `xlim`

(through ... ).

## Examples

```r
# plot continuous epiparameter
ep <- epiparameter(
  disease = "ebola",
  epi_name = "incubation_period",
  prob_distribution = create_prob_distribution(
    prob_distribution = "gamma",
    prob_distribution_params = c(shape = 2, scale = 1)
  )
)
plot(ep)

# plot different day range (x-axis)
plot(ep, xlim = c(0, 10))

# plot CDF
plot(ep, cumulative = TRUE)

# plot discrete epiparameter
ep <- discretise(ep)
plot(ep)
```

## Author(s)

Joshua W. Lambert
