# Reads in parameter library from JSON

```r
.read_db()
```

## Returns

`list`.

Read epidemiological parameter database from JSON using `jsonlite::read_json()` and returns the list with a `<epiparameterDB>`

class attribute to validate it has been read using this function.
