# Generate seropositivity counts by bin given the probability and sample size per age group bin

```r
get_seroprev_counts_by_bin(
  prob_seroprev_by_age,
  sample_size_by_age_random,
  survey_features
)
```

## Arguments

- `prob_seroprev_by_age`: Probability of seropositivity by age
- `sample_size_by_age_random`: Random sample size by age
- `survey_features`: A dataframe containing information about the binned age groups and sample sizes for each. It should contain columns:
    
    - **age_min**: Left limits of the age groups to be considered in the serosurvey
    - **age_max**: Right limits of the age groups to be considered in the serosurvey
    - **n_sample**: Number of samples by age group
    
    The resulting age intervals are closed to the left `[` and open to the right `)`.

Generate seropositivity counts by bin given the probability and sample size per age group bin
