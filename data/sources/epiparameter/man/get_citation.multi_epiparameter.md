# Get citation from a list of `<epiparameter>` objects

```r
## S3 method for class 'multi_epiparameter'
get_citation(x, ...)
```

## Arguments

- `x`: An `<epiparameter>` object.
- `...`: dots Not used, extra arguments supplied will cause a warning.

## Returns

A `<bibentry>` object containing multiple references. The length of output `<bibentry>` is equal to the length of the list of `<epiparameter>`

objects supplied.

Extract the citation stored in a list of `<epiparameter>` objects.

## Examples

```r
# example with list of <epiparameter>
db <- epiparameter_db()
get_citation(db)
```
