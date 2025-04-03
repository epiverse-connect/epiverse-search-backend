# Subset fields when reading from DHIS2

```r
dhis2_subset_fields(data, fields = c("dataElement", "period", "value"))
```

## Arguments

- `data`: the input data frame
- `fields`: vector of fields to select from the data frame

## Returns

an object of type `data.frame` with the data that contains only the fields of interest.

Subset fields when reading from DHIS2

## Examples

```r
## Not run:

results <- dhis2_subset_fields(
  data = readepi(
    credentials_file = system.file("extdata", "test.ini",
                                     package = "readepi"),
    data_source      = "https://play.dhis2.org/demo",
    query_parameters = list(
        dataSet   = "pBOMPrpg1QX,BfMAe6Itzgt",
        orgUnit   = "DiszpKrYNg8",
        startDate = "2014",
        endDate   = "2023")
  )$data,
  fields             = c("dataElement", "period", "value")
)
## End(Not run)
```
