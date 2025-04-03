# Check DHIS2 authentication details

```r
dhis2_login(base_url, user_name, password)
```

## Arguments

- `base_url`: the base URL of the DHIS2 server
- `user_name`: the user name
- `password`: the user's password

## Returns

a message if the dhis2_login was successful, throws an error otherwise.

a message if the login was successful, throws an error otherwise.

If the user were granted with access to the API, this will return a message specifying that the user was successfully connected. Otherwise, it will throw an error message.

## Examples

```r
## Not run:

  dhis2_login(
    base_url  = file.path("https:/", "play.dhis2.org", "demo"),
    user_name = "admin",
    password  = "district"
  )
## End(Not run)
```
