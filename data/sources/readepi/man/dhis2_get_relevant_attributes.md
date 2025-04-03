# Get the relevant dataset

```r
dhis2_get_relevant_attributes(
  base_url,
  user_name,
  password,
  attribute_id = NULL,
  which = "dataSets"
)
```

## Arguments

- `base_url`: the web address of the server the user wishes to log in to
- `user_name`: the user name
- `password`: the user's password
- `attribute_id`: a vector of DHIS2 attribute ids. The ids could be those of a dataSet or an orgUnit.
- `which`: the target DHIS2 end point

## Returns

a `list` of 2 elements: a `character` string with the target attributes ID(s) and a `data.frame` that contains the data of interest from the specified DHIS2 attribute ids.

Get the relevant dataset

## Examples

```r
## Not run:

result <- dhis2_get_relevant_attributes(
  base_url     = "https://play.dhis2.org/demo",
  user_name    = "admin",
  password     = "district",
  attribute_id = c("pBOMPrpg1QX", "BfMAe6Itzgt"),
  which        = "dataSets"
)
## End(Not run)
```
