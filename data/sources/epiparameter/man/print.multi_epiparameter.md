# Print method for `<multi_epiparameter>` class

```r
## S3 method for class 'multi_epiparameter'
print(x, ..., n = NULL)
```

## Arguments

- `x`: A `<multi_epiparameter>` object.
- `...`: dots Extra arguments to be passed to the method.
- `n`: A `numeric` specifying how many `<epiparameter>` objects to print. This argument is passed to `head()` for `list` printing. Default is `NULL`
    
    and the number of elements to print is controlled by package `options()`.

## Returns

Invisibly returns a `<multi_epiparameter>`. Called for side-effects.

Print method for `<multi_epiparameter>` class

## Examples

```r
# entire database
db <- epiparameter_db()
db

# a single disease
db <- epiparameter_db(disease = "Ebola")
db

# a single epi parameter
db <- epiparameter_db(epi_name = "offspring distribution")
db
```
