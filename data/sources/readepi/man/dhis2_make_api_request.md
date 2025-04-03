# Make an API request to the target DHIS2 system

```r
dhis2_make_api_request(base_url, user_name, password, which = "dataElements")
```

## Arguments

- `base_url`: the base URL of the DHIS2 server
- `user_name`: the user name
- `password`: the user's password
- `which`: the target DHIS2 attribute name. Possible values are:
    
    1. dataSets: to get the dataset identifiers and names
    2. organisationUnits: to get the organisation unit identifiers and names
    3. dataElementGroups: to get the data element groups identifiers and names
    4. dataElements: to get the data elements identifiers and names

## Returns

an object of class `data.frame` that contains the information of interest.

Make an API request to the target DHIS2 system

## Examples

```r
## Not run:

  response <- dhis2_make_api_request(
    base_url  = file.path("https:/", "play.dhis2.org", "demo"),
    user_name = "admin",
    password  = "district",
    which     = "dataElements"
  )
## End(Not run)
```
