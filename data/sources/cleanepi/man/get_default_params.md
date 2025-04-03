# Set and return `clean_data` default parameters

```r
get_default_params()
```

## Returns

A `<list>` of the default cleaning parameters.

When `clean_data()` function is called without any argument, these default values provided to the function's arguments will be applied on the input data. By default, operations that require the target columns to be specified by the user will not be performed. The default cleaning operations include: i) standardizing column names, ii) detecting and removing duplicates, and iii) removing constant data.

## Examples

```r
default_params <- get_default_params()
```
