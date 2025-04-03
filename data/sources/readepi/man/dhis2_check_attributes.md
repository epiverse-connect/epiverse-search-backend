# Check the DHIS2 attributes for data import

```r
dhis2_check_attributes(base_url, user_name, password, query_parameters)
```

## Arguments

- `base_url`: the web address of the server the user wishes to log in to
- `user_name`: the user name
- `password`: the user's password
- `query_parameters`: a list with the parameters that will be used to determine which data is returned by the query

## Returns

a list of 9 elements of type `character`.

Check the DHIS2 attributes for data import

## Examples

```r
## Not run:

  attributes <- dhis2_check_attributes(
    base_url         = "https://play.dhis2.org/dev",
    user_name        = "admin",
    password         = "district",
    query_parameters = list(dataSet = "pBOMPrpg1QX",
                            orgUnit = "DiszpKrYNg8")
  )
## End(Not run)
```
