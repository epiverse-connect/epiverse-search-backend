# Import data form DHIS2

```r
read_from_dhis2(
  base_url,
  user_name,
  password,
  query_parameters,
  records = NULL,
  fields = NULL,
  id_col_name = "dataElement"
)
```

## Arguments

- `base_url`: the web address of the server the user wishes to log in to
- `user_name`: the user name
- `password`: the user password
- `query_parameters`: a list with the parameters that will be used to determine which data is returned by the query. The possible values are:
    
    1. dataSet: a vector or a list of comma-separated data set identifiers (required)
    2. dataElementGroup: a vector or a list of comma-separated data element group identifiers. This is not needed when the 'dataSet' is provided
    3. orgUnit: a vector or a list of comma-separated organisation unit identifiers (required)
    4. orgUnitGroup: a vector or a list of comma-separated organisation unit group identifiers. This is not needed when the 'orgUnit' is provided
    5. startDate: the start date for the time span of the values to export (required)
    6. startDate: the end date for the time span of the values to export (required)
- `records`: a vector or a comma-separated string of subset of subject IDs. When specified, only the records that correspond to these subjects will be imported.
- `fields`: a vector or a comma-separated string of column names. If provided, only those columns will be imported.
- `id_col_name`: the column name with the records of interest.

## Returns

a `list` of 1 element of type `data frame`.

Import data form DHIS2

## Examples

```r
## Not run:

data <- read_from_dhis2(
  base_url         = "https://play.dhis2.org/demo",
  user_name        = "admin",
  password         = "district",
  query_parameters = list(dataSet   = "BfMAe6Itzgt",
                          orgUnit   = "Umh4HKqqFp6",
                          startDate = "2014",
                          endDate   = "2023"),
  records          = NULL,
  fields           = NULL,
  id_col_name      = "dataElement"
)
## End(Not run)
```
