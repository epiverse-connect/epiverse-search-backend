# Check if object is line list from `sim_linelist()`

```r
.check_linelist(linelist)
```

## Arguments

- `linelist`: Line list `<data.frame>` output from `sim_linelist()`.

## Returns

Invisibly return the `linelist` `<data.frame>`. The function is called for its side-effects, which will error if the input is invalid.

Check if object is line list from `sim_linelist()`

## Details

This is a check that the object supplied to `linelist` is from the `sim_linelist()` or `sim_outbreak()` functions, it is not related to the class of the object, in other words, it does not check the object is of class `<linelist>`.
