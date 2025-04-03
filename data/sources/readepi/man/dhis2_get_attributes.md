# Get the target DHIS2 attribute identifiers and names

```r
dhis2_get_attributes(base_url, user_name, password, which = "dataSets")
```

## Arguments

- `base_url`: the base URL of the DHIS2 server
- `user_name`: the user name
- `password`: the user's password
- `which`: the target DHIS2 attribute name.

## Returns

an object of type `data.frame` with details about the DHIS2 attributes of interest.

Get the target DHIS2 attribute identifiers and names

## Examples

```r
## Not run:

datasets <- dhis2_get_attributes(
  base_url  = "https://play.dhis2.org/demo/",
  user_name = "admin",
  password  = "district",
  which     = "dataSets"
)
## End(Not run)
```
