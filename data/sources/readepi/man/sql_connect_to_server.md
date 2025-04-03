# Establish connection to the server

```r
sql_connect_to_server(
  base_url,
  user_name,
  password,
  dbms,
  driver_name,
  database_name,
  port
)
```

## Arguments

- `base_url`: the host server name
- `user_name`: the user name
- `password`: the user's password
- `dbms`: the database management system type
- `driver_name`: the driver name
- `database_name`: the database name
- `port`: the server port ID

## Returns

the `connection` object

Establish connection to the server

## Examples

```r
## Not run:

con <- sql_connect_to_server(
  base_url      = "mysql-rfam-public.ebi.ac.uk",
  user_name     = "rfamro",
  password      = "",
  dbms          = "MySQL",
  driver_name   = "",
  database_name = "Rfam",
  port          = 4497
)
## End(Not run)
```
