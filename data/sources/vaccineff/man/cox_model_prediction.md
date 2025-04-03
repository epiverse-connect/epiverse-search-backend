# Internal function to calculate prediction from Cox model

```r
cox_model_prediction(cox_model, vaccinated_status, unvaccinated_status)
```

## Arguments

- `cox_model`: Result from `cox_model` function

## Returns

`data.frame` containing `time`: time-to-event until `at`

`logtime`: log of time-to-event `hazard`: estimated hazard from model `surv`: estimated survival probability from model `loglog`: -log(-log(survival probability)) `strata`: vaccinated/unvaccinated status

Internal function to calculate prediction from Cox model
