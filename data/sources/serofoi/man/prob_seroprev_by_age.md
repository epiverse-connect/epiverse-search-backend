# Generate probabilities of seropositivity by age based on model choice.

```r
prob_seroprev_by_age(model, foi, seroreversion_rate = 0)
```

## Arguments

- `model`: A string specifying the model type which can be either '"age"', '"time"', '"age-time"'.
- `foi`: A dataframe containing the FoI values. For time-varying models the columns should be:
    
    - **year**: Calendar years starting at the birth year of the oldest person and up to the time of the serosurvey
    - **foi**: Corresponding values of the FoI by year
    
    For age-varying models the columns should be:.
    
    - **age**: Ages starting at 1 and up to the age of the oldest person in the serosurvey
    - **foi**: Corresponding values of the FoI by age
    
    For age-and-time-varying models the columns should be:
    
    
    - **age**: Ages starting at 1 and up to the age of the oldest person in the serosurvey
    - **time**: Calendar years starting at the birth year of the oldest person and up to the time of the serosurvey
    - **foi**: Corresponding values of FoI by age and year
- `seroreversion_rate`: A non-negative value determining the rate of seroreversion (per year). Default is 0.

## Returns

A dataframe with columns 'age' and 'seropositivity'.

This function generates seropositivity probabilities based on either a time-varying Force-of-Infection (FoI) model, an age-varying FoI model, or an age-and-time-varying FoI model. In all cases, it is possible to optionally include seroreversion.

## Examples

```r
prob_seroprev_by_age(
  model = "age",
  foi = data.frame(
    age = 1:80,
    foi = rep(0.01, 80)
  )
)
```
