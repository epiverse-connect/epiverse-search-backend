# Specify methodological aspects of distribution fitting

```r
create_method_assess(
  censored = NA,
  right_truncated = NA,
  phase_bias_adjusted = NA
)
```

## Arguments

- `censored`: A boolean `logical` whether the study used single or double interval censoring in the methods to infer the delay distribution
- `right_truncated`: A boolean `logical` whether the study used right- truncation in the methods to infer the delay distribution
- `phase_bias_adjusted`: A boolean `logical` whether the study adjusted for phase bias in the methods to infer the delay distribution

## Returns

A named list with three elements

A helper function when creating an `<epiparameter>` object to create a method assessment list with sensible defaults, type checking and arguments to help remember which method assessments can be accepted in the list.

## Details

Currently, the method assessment focuses on common methodological aspects of delay distributions (e.g. incubation period, serial interval, etc.), and does not currently take into account methodological aspects which may be important when fitting offspring distributions to data on disease (super)spreading.

## Examples

```r
create_method_assess(
  censored = FALSE,
  right_truncated = FALSE,
  phase_bias_adjusted = FALSE
)
```
