# Table of epidemiological distributions

```r
parameter_tbl(
  multi_epiparameter,
  disease = "all",
  pathogen = "all",
  epi_name = "all"
)
```

## Arguments

- `multi_epiparameter`: Either an `<epiparameter>` object or a list of `<epiparameter>` objects.
- `disease`: A `character` string with name of the infectious disease.
- `pathogen`: A `character` string with the name of the causative agent of disease, or `NA` if not known.
- `epi_name`: A `character` string with the name of the epidemiological parameter type.

## Returns

A `<parameter_tbl>` object which is a subclass of `<data.frame>`.

This function subsets the epidemiological parameter library to return only the chosen epidemiological distribution. The results are returned as a data frame containing the disease, epidemiological distribution, probability distribution, author of the study, and the year of publication.

## Examples

```r
epiparameter_list <- epiparameter_db(disease = "COVID-19")
parameter_tbl(multi_epiparameter = epiparameter_list)

# example filtering an existing list to incubation periods
epiparameter_list <- epiparameter_db(disease = "COVID-19")
parameter_tbl(
  multi_epiparameter = epiparameter_list,
  epi_name = "incubation period"
)
```

## Author(s)

Joshua W. Lambert, Adam Kucharski
