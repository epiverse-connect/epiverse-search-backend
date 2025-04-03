# Prepare common epidemiological data formats for CFR estimation

```r
prepare_data(data, ...)

## S3 method for class 'incidence2'
prepare_data(
  data,
  cases_variable = "cases",
  deaths_variable = "deaths",
  fill_NA = TRUE,
  ...
)
```

## Arguments

- `data`: A `<data.frame>`-like object. Currently, only `<incidence2>`
    
    objects are supported. These may be grouped.
- `...`: Currently unused. Passing extra arguments will throw a warning.
- `cases_variable`: A string for the name of the cases variable in the "count_variable" column of `data`.
- `deaths_variable`: A string for the name of the deaths variable in the "count_variable" column of `data`.
- `fill_NA`: A logical indicating whether `NA`s in the cases and deaths data should be replaced by 0s. The default value is `TRUE`, with a message to make users aware of the replacement.

## Returns

A `<data.frame>` suitable for disease severity estimation functions provided in `cfr`, with the columns "date", "cases", and "deaths".

Additionally, for grouped `<incidence2>` data, columns representing the grouping variables will also be present.

The result has a continuous sequence of dates between the start and end date of `data`; this is required if the data is to be passed to functions such as `cfr_static()`.

This S3 generic has methods for classes commonly used for epidemiological data.

Currently, the only supported data format is `<incidence2>` from the `incidence2` package. See `incidence2::incidence()`. Grouped `<incidence2>` data are supported, see Details .

## Details

The method for `<incidence2>` data can replace `NA`s in the case and death data with 0s using the `fill_NA` argument, which is `TRUE` by default, meaning that `NA`s are replaced.

Keeping `NA`s will cause downstream issues when calling functions such as `cfr_static()` on the data, as they cannot handle `NA`s. Setting `fill_NA = TRUE` resolves this issue.

Passing a grouped `<incidence2>` object to `data` will result in the function respecting the grouping and returning grouping variables in separate columns.

## Examples

```r
#### For <incidence2> data ####
# load Covid-19 data from incidence2
covid_uk <- incidence2::covidregionaldataUK

# convert to incidence2 object
covid_uk_incidence <- incidence2::incidence(
  covid_uk,
  date_index = "date",
  counts = c("cases_new", "deaths_new"),
  count_names_to = "count_variable"
)

# View tail of prepared data
data <- prepare_data(
  covid_uk_incidence,
  cases_variable = "cases_new",
  deaths_variable = "deaths_new"
)

tail(data)

#### For grouped <incidence2> data ####
# convert data to incidence2 object grouped by region
covid_uk_incidence <- incidence2::incidence(
  covid_uk,
  date_index = "date",
  counts = c("cases_new", "deaths_new"),
  count_names_to = "count_variable",
  groups = "region"
)

# View tail of prepared data
data <- prepare_data(
  covid_uk_incidence,
  cases_variable = "cases_new",
  deaths_variable = "deaths_new"
)

tail(data)
```
