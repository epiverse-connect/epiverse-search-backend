# Construct age-group variable from age column

```r
get_age_group(data_set, col_age, max_val, min_val = 0, step)
```

## Arguments

- `data_set`: `data.frame` with at least a column containing the age information
- `col_age`: Name of the column containing the age information
- `max_val`: Maximum value of age interval to split
- `min_val`: Minimum value of age interval to split
- `step`: Step used to split the age interval

## Returns

Column of type `factor` with the same length as the number of rows in `data_set`, with levels corresponding to age bins between `min_val` and `max_val`. Ages above `max_val` are represented as `>max_val`.

This method splits an age interval from `min_val` to `max_val`

into intervals of size `step`. If the method finds ages greater or equal than `max_val`

it assigns the string `">max_val"`. By default `min_val` is set to 0, however it can be assigned by convenience. If the method finds ages lower or equal than `min_val` it assigns the string `"<min_val-1"`. The function warns when (max_val - min_val) is not an integer multiple of step. In that case the last interval is truncated to the upper value closest to max_val for which (closest_upper - min_val) is multiple of step.

## Examples

```r
# load data provided with the package
data(cohortdata)

# assign age groups as a column of the `data.frame`
cohortdata$age_group <- get_age_group(
  data_set = cohortdata,
  col_age = "age",
  max_val = 80,
  step = 10
)

# view the `data.frame` with new column
head(cohortdata)
```
