# Sets initialization function for sampling

```r
set_foi_init(foi_init, is_log_foi, foi_index)
```

## Arguments

- `foi_init`: Initialization function for sampling. If null, default is chosen depending on the foi-scale of the model
- `is_log_foi`: Boolean to set logarithmic scale in the FoI
- `foi_index`: Integer vector specifying the age-groups for which Force-of-Infection values will be estimated. It can be specified by means of get_foi_index

## Returns

Function specifying initialization vector for the Force-of-Infection

Sets initialization function for sampling

## Examples

```r
data(chagas2012)
foi_index <- get_foi_index(chagas2012, group_size = 5, model_type = "age")
foi_init <- set_foi_init(
  foi_init = NULL,
  is_log_foi = FALSE,
  foi_index = foi_index
)
```
