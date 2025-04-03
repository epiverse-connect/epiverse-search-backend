# Check if `<epiparameter>` or list of `<epiparameter>` objects contains a distribution and distribution parameters

```r
is_parameterised(x, ...)

is_parameterized(x, ...)

## S3 method for class 'epiparameter'
is_parameterised(x, ...)

## S3 method for class 'multi_epiparameter'
is_parameterised(x, ...)
```

## Arguments

- `x`: An `<epiparameter>` or list of `<epiparameter>` objects.
- `...`: dots Extra arguments to be passed to the method.

## Returns

A single boolean `logical` for `<epiparameter>` or vector of `logical`s equal in length to the list of `<epiparameter>` objects input. If the `<epiparameter>` object is missing either a probability distribution or parameters for the probability distribution returns `FALSE`, otherwise it returns `TRUE`.

Check if `<epiparameter>` or list of `<epiparameter>` objects contains a distribution and distribution parameters

## Examples

```r
# parameterised <epiparameter>
ep <- epiparameter(
  disease = "ebola",
  epi_name = "incubation",
  prob_distribution = create_prob_distribution(
    prob_distribution = "gamma",
    prob_distribution_params = c(shape = 1, scale = 1)
  )
)
is_parameterised(ep)

# unparameterised <epiparameter>
ep <- epiparameter(
  disease = "ebola",
  epi_name = "incubation"
)
is_parameterised(ep)

# list of <epiparameter>
db <- epiparameter_db()
is_parameterised(db)
```
