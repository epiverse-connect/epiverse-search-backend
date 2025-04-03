# Checks the uniqueness in values of the sample IDs column

```r
check_subject_ids_oness(data, id_col_name)
```

## Arguments

- `data`: The input `<data.frame>` or `<linelist>`
- `id_col_name`: A `<character>` with the name of the column that contains the sample IDs

## Returns

the input `<data.frame>` with and extra element in its attributes when there are missing or duplicated IDs.

Checks the uniqueness in values of the sample IDs column
