# Match Cohort to Reduce Observational Bias

```r
match_cohort(
  data_set,
  outcome_date_col,
  censoring_date_col,
  start_cohort,
  end_cohort,
  nearest,
  exact,
  immunization_date_col,
  vacc_status_col,
  vaccinated_status,
  unvaccinated_status
)
```

## Arguments

- `data_set`: `data.frame` with cohort information.
- `outcome_date_col`: Name of the column that contains the outcome dates.
- `censoring_date_col`: Name of the column that contains the censoring date.
- `start_cohort`: Start date of the study.
- `end_cohort`: End date of the study.
- `nearest`: Named vector with name(s) of column(s) for `nearest` matching and caliper(s) for each variable (e.g., `nearest = c("characteristic1" = n1, "characteristic2" = n2)`, where `n1` and `n2` are the calipers).
- `exact`: Name(s) of column(s) for `exact` matching
- `immunization_date_col`: Name of the column that contains the immunization date to set the beginning of the follow-up period (`t0_follow_up`).
- `vacc_status_col`: Name of the column containing the vaccination.
- `vaccinated_status`: Status assigned to the vaccinated population.
- `unvaccinated_status`: Status assigned to the unvaccinated population.

## Returns

object of the class `match`. List with results from static match: `match`: `data.frame` with adjusted cohort, `summary`: matching summary, `balance_all`: balance of the cohort before matching, `balance_matched`: balance of the cohort after matching.

Four columns are added to the structure provided in `data_set`: `subclass`: ID of, matched pair, `t0_follow_up`: beginning of follow-up period for pair, `time_to_event`: time to event, and `outcome_status`: outcome status (1:positive, 0: negative).

This function builds pairs of vaccinated and unvaccinated individuals with similar characteristics. The function relies on the matching algorithm implemented in the package `{MatchIt}`, setting, by default, `method = "nearest"`, `ratio = 1`, and `distance = "mahalanobis"`. Exact and near characteristics are accepted, passed in the parameters `exact`

and `nearest`, respectively. The parameter `nearest` must be provided together with the calipers as a named vector (e.g., `nearest = c(characteristic1 = n1, characteristic2 = n2)`, where `n1`

and `n2` are the calipers). The default matching `method` of the function is `static`. This means that pairs are matched once, without taking into account their vaccination, censoring, and outcome dates. After this, the pairs whose exposure time do not coincide are removed to avoid negative time-to-events. The function returns a matched and adjusted by exposure cohort, with information of the beginning of follow-up period of pairs (`t0_follow_up`), corresponding to the vaccination date of the vaccinated individual, the individual time-to-event (`time_to_event`) and the outcome status (`outcome_status`), both taking into account the right-censoring dates. Pairs are censored if the vaccinated or unvaccinated partner was previously censored (i.e., if `censoring_date_col` is informed) and the censor occurs before their outcomes. Rolling calendar matching method will be included in future releases.
