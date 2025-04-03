# Check whether a package is installed

```r
.is_pkg_installed(package)
```

## Arguments

- `package`: string naming the package/name space to load.

## Returns

Invisibly returns a boolean `logical`.

Check whether a package is installed

## Details

This functions allows testing for when a suggested package dependency is not installed to check if conditional code can be run.
