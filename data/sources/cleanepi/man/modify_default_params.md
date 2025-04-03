# Update `clean_data` default argument's values with the user-provided values.

```r
modify_default_params(defaults, params, strict = TRUE)
```

## Arguments

- `defaults`: A `<list>` with the default arguments
- `params`: A `<list>` with the user-specified arguments
- `strict`: A `<logical>` that specified whether to trigger an error or not when there is a difference between the list of default arguments and list of the arguments provided by the user. Default is `TRUE`.

## Returns

The updated `<list>` of parameters that will be used to perform the data cleaning.

Update `clean_data` default argument's values with the user-provided values.
