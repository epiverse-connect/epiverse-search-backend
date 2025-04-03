# Subset a specified set of records from a dataset imported from DHIS2

```r
dhis2_subset_records(data, records, id_col_name = "dataElement")
```

## Arguments

- `data`: the input data frame
- `records`: a vector of records to select from the data
- `id_col_name`: the column name where the records belong to

## Returns

an object of type `data.frame` with the data that contains only the records of interest.

Subset a specified set of records from a dataset imported from DHIS2

## Examples

```r
## Not run:

result <- dhis2_subset_records(
  data = readepi(
    credentials_file = system.file("extdata", "test.ini",
                                   package = "readepi"),
    data_source      = "https://play.dhis2.org/demo",
    query_parameters = list(
        dataSet   = "pBOMPrpg1QX",
        orgUnit   = "DiszpKrYNg8",
        startDate = "2014",
        endDate   = "2023")
  )$data,
  records            = c("FTRrcoaog83", "eY5ehpbEsB7", "Ix2HsbDMLea"),
  id_col_name        = "dataElement"
)
## End(Not run)
```
