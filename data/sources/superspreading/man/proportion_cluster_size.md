# Estimate what proportion of new cases originated within a transmission event of a given size

```r
proportion_cluster_size(
  R,
  k,
  cluster_size,
  ...,
  offspring_dist,
  format_prop = TRUE
)
```

## Arguments

- `R`: A `number` specifying the R parameter (i.e. average secondary cases per infectious individual).
- `k`: A `number` specifying the k parameter (i.e. overdispersion in offspring distribution from fitted negative binomial).
- `cluster_size`: A `number` for the cluster size threshold.
- `...`: dots not used, extra arguments supplied will cause a warning.
- `offspring_dist`: An `<epiparameter>` object. An S3 class for working with epidemiological parameters/distributions, see `epiparameter::epiparameter()`.
- `format_prop`: A `logical` determining whether the proportion column of the `<data.frame>` returned by the function is formatted as a string with a percentage sign (`%`), (`TRUE`, default), or as a `numeric` (`FALSE`).

## Returns

A `<data.frame>` with the value for the proportion of new cases that are part of a transmission event above a threshold for a given value of R and k.

Calculates the proportion of new cases that originated with a transmission event of a given size. It can be useful to inform backwards contact tracing efforts, i.e. how many cases are associated with large clusters. Here we define a cluster to as a transmission of a primary case to at least one secondary case.

## Details

This function calculates the proportion of secondary cases that are caused by transmission events of a certain size. It does not calculate the proportion of transmission events that cause a cluster of secondary cases of a certain size. In other words it is the number of cases above a threshold divided by the total number of cases, not the number of transmission events above a certain threshold divided by the number of transmission events.

## Examples

```r
R <- 2
k <- 0.1
cluster_size <- 10
proportion_cluster_size(R = R, k = k, cluster_size = cluster_size)

# example with a vector of k
k <- c(0.1, 0.2, 0.3, 0.4, 0.5)
proportion_cluster_size(R = R, k = k, cluster_size = cluster_size)

# example with a vector of cluster sizes
cluster_size <- c(5, 10, 25)
proportion_cluster_size(R = R, k = k, cluster_size = cluster_size)
```
