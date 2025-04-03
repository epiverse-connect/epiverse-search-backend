# Modifies the historic incidence to handle with the observations of epidemic years

```r
endemic_outliers(
  historic,
  outlier_years,
  outliers_handling,
  geometric_method = "shifted"
)
```

## Arguments

- `historic`: Historic incidence counts
- `outlier_years`: A numeric vector with the outlier years
- `outliers_handling`: A string with the handling decision regarding outlier years
    
     * ignored = data from outlier years will not take into account
     * included = data from outlier years will take into account
     * replaced_by_median = data from outlier years will be replaced with the median and take into account
     * replaced_by_mean = data from outlier years will be replaced with the mean and take into account
     * replaced_by_geometric_mean = data from outlier years will be replaced with the geometric mean and take into account
- `geometric_method`: A string with the selected method for geometric mean calculation; see: geometric_mean

## Returns

A modified historic incidence

Function that modifies an historic incidence by including, ignoring or replacing the observations of epidemic years
