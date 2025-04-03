# Sample the number of susceptible offspring from all possible offspring

```r
.get_susceptible_offspring(new_offspring, susc_pop, pop)
```

## Arguments

- `new_offspring`: A numeric vector of the possible new offspring per chain produced by `.sample_possible_offspring()`.
- `pop`: Population size; An `<Integer>`. Used alongside `percent_immune`
    
    to define the susceptible population. Defaults to `Inf`.

## Returns

A numeric vector of the number of offspring that can be infected given the current susceptible population size.

Sample susceptible offspring to be infected from all possible offspring. This function is used internally, and input checking is not performed here, only in the context where it is used. Using it directly is not recommended.
