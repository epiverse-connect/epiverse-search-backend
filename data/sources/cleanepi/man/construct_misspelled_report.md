# Build the report for the detected misspelled values during dictionary-based data cleaning operation

```r
construct_misspelled_report(misspelled_options, data)
```

## Arguments

- `misspelled_options`: A `<list>` with the detected misspelled values in the columns of interest.
- `data`: The input `<data.frame>` or `<linelist>`

## Returns

A `<data.frame>` the details about where in the input data the misspelled values were found.

Build the report for the detected misspelled values during dictionary-based data cleaning operation
