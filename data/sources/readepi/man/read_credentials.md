# Read credentials from a configuration file

```r
read_credentials(file_path, base_url)
```

## Arguments

- `file_path`: the path to the file with the user-specific credential details for the projects of interest.
- `base_url`: the URL of the HIS of interest

## Returns

a `list` of 5 elements of type `character` and `numeric`. These correspond to the user's credential details.

Read credentials from a configuration file

## Examples

```r
## Not run:

credentials <- read_credentials(
  file_path = system.file("extdata", "test.ini", package = "readepi"),
  base_url  = "mysql-rfam-public.ebi.ac.uk"
)
## End(Not run)
```
