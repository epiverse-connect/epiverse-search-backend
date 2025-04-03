# Auxiliary function to calculate the proportion by age according to the total population and sex

```r
get_age_risk_sex(age, sex_vector, pyramid, sex)
```

## Arguments

- `age`: A vector with the ages of cases in years from 0 to 100 years
- `sex_vector`: A vector with the sex of cases 'F' and 'M'
- `pyramid`: A dataframe with the count of individuals
- `sex`: A string specifying the sex being calculated

## Returns

A dataframe with the proportion by age according to the total population and sex

Auxiliary function to calculate the proportion by age according to the total population and sex
