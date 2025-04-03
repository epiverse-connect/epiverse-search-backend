data

# Cohort data on vaccineff

## Format

### `cohortdata`

- **id**: Anonymous ID of the individual
- **sex**: Sex F/M
- **age**: Age (50-100)
- **death_date**: Registered death by COVID-19
- **death_other_causes**: Registered death by other causes
- **vaccine_date_1**: Registered date of the first dose
- **vaccine_date_2**: Registered date of the second dose
- **vaccine_1**: Brand of the first dose
- **vaccine_2**: Brand of the second dose

```r
cohortdata
```

Subset of data from an anonymised, real-world dataset produced as part of the early stage of the immunization program against COVID-19 in Bogota, Colombia between February 2021 and December 2021. Cohort dataset contains registers of homologous schemes for two different brands for adults aged 50 years or older. This cohort received two doses of a vaccine aimed at reducing the risk of death. All the registers were anonymised and de-identified to preserve the privacy of data. The dataset includes disaggregated information on the first and second vaccine doses (vaccine_date1, vaccine_date2, vaccine1, and vaccine2) for each participant and relevant demographic details (sex and age). Additionally, the dataset includes the dates of two outcomes: death associated with COVID-19 (death_date) and death from other causes (death_other_causes).

## Examples

```r
cohortdata
```
