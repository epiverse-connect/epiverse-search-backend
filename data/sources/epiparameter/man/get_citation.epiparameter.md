# Get citation from an `<epiparameter>` object

```r
## S3 method for class 'epiparameter'
get_citation(x, ...)
```

## Arguments

- `x`: An `<epiparameter>` object.
- `...`: dots Not used, extra arguments supplied will cause a warning.

## Returns

A `<bibentry>` object.

Extract the citation stored in an `<epiparameter>` object.

## Examples

```r
# example with <epiparameter>
ep <- epiparameter_db(single_epiparameter = TRUE)
get_citation(ep)

# example returning bibtex format
ep <- epiparameter_db(disease = "COVID-19", single_epiparameter = TRUE)
cit <- get_citation(ep)
format(cit, style = "bibtex")
```
