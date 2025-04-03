# Rename columns of a linelist

```r
## S3 replacement method for class 'linelist'
names(x) <- value
```

## Arguments

- `x`: a `linelist` object
- `value`: a `character` vector to set the new names of the columns of `x`

## Returns

a `linelist` with new column names

This function can be used to rename the columns a `linelist`, adjusting tags as needed.

## Examples

```r
if (require(outbreaks)) {

  ## dataset to create a linelist from
  measles_hagelloch_1861

  ## create linelist
  x <- make_linelist(measles_hagelloch_1861,
    id = "case_ID",
    date_onset = "date_of_prodrome",
    age = "age",
    gender = "gender"
  )
  head(x)

  ## change names
  names(x)[1] <- "case_label"

  ## see results: tags have been updated
  head(x)
  tags(x)

 # This also works with using `dplyr::rename()` because it uses names<-()
 # under hood
 if (require(dplyr)) {
   x <- x |>
     rename(case_id= case_label)
   head(x)
   tags(x)
 }
}
```
