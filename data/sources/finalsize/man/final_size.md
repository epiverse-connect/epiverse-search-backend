# Final size of an epidemic

```r
final_size(
  r0,
  contact_matrix = matrix(1),
  demography_vector = 1,
  susceptibility = matrix(1),
  p_susceptibility = matrix(1),
  contact_scaling = 1,
  solver = c("iterative", "newton"),
  control = list()
)
```

## Arguments

- `r0`: The basic reproductive number `R_0` of the disease.
- `contact_matrix`: Social contact matrix. Entry `m_{ij}` gives average number of contacts in group `i` reported by participants in group `j`
    
    . Defaults to the singleton matrix `[1]`, representing a homogeneously mixing population.
- `demography_vector`: Demography vector. Entry `v_{i}` gives proportion of total population in group `i` (model will normalise if needed). Defaults to `1`, representing a population where demographic structure is not important (or not known), and where all individuals are assumed to belong to the same demographic group.
- `susceptibility`: A matrix giving the susceptibility of individuals in demographic group `i` and risk group `k`. Defaults to the singleton matrix `[1]`, representing a population where all individuals are fully susceptible to infection.
- `p_susceptibility`: A matrix giving the probability that an individual in demography group `i` is in risk (or susceptibility) group `k`. Each row represents the overall distribution of individuals in demographic group `i` across risk groups, and each row **must sum to 1.0**. Defaults to the singleton matrix `[1]`, representing a population where all individuals are fully susceptible.
- `contact_scaling`: For `r_eff()`, either a single number or a numeric vector of the same length as `demography_vector`, giving the proportional scaling of contacts of each demographic group. Values must be in the range `[0, 1]`. Defaults to 1.0 for no scaling.
- `solver`: Which solver to use. Options are "iterative" (default) or "newton", for the iterative solver, or the Newton solver, respectively. Special conditions apply when using the Newton solver, see the `control`
    
    argument.
- `control`: A list of named solver options, see **Solver options**.

## Returns

A data.frame of the proportion and number of infected individuals, within each demography group and susceptibility group combination. The sizes of each demography-susceptibility combination are also returned in a column. If the demography groups and susceptibility groups are named, these names are added to relevant columns. If the groups are not named, synthetic names are added of the form `demo_grp_<i>`, for each demographic group `i`.

`final_size` calculates the final size of an epidemic outbreak with a given `R_0`, with options for specifying a population with heterogeneous mixing, and with heterogeneous susceptibility to infection such as that conferred by an immunisation programme.

## Details

### Specifying heterogeneous mixing and susceptibility

`final_size()` allows for heterogeneous population mixing and susceptibility, and this is described in the dedicated vignettes:

1. Heterogeneous population mixing: See vignette on "Modelling heterogeneous social contacts" (`vignette("varying_contacts", package = "finalsize")`);
2. Heterogeneous susceptibility to infection: See vignette on "Modelling heterogeneous susceptibility" (`vignette("varying_susceptibility", package = "finalsize")`).

### Solver options

The `control` argument accepts a list of solver options, with the iterative solver taking two extra arguments than the Newton solver. This is an optional argument, and default options are used within the solver functions if an argument is missing. Arguments provided override the solver defaults.

#### Common options

1. `iterations`: The number of iterations over which to solve for the final size, unless the error is below the solver tolerance. Default = 10000.
2. `tolerance`: The solver tolerance; solving for final size ends when the error drops below this tolerance. Defaults to set `1e-6`. Larger tolerance values are likely to lead to inaccurate final size estimates.

### Iterative solver options

1. `step_rate`: The solver step rate. Defaults to 1.9 as a value found to work well.
2. `adapt_step`: Boolean, whether the solver step rate should be changed based on the solver error. Defaults to TRUE.

## Examples

```r
## For a given R_0
r0 <- 2.0
final_size(r0)

## For a population with multiple demographic groups
# load example POLYMOD data included in the package
data(polymod_uk)
contact_matrix <- polymod_uk$contact_matrix
demography_vector <- polymod_uk$demography_vector

# define the number of age and susceptibility groups
n_demo_grps <- length(demography_vector)
n_risk_grps <- 3

# In this example, all risk groups from all age groups are fully
# susceptible, and the final size in each group is influenced only by
# differences in social contacts
susceptibility <- matrix(
  data = 1, nrow = n_demo_grps, ncol = n_risk_grps
)

p_susceptibility <- matrix(
  data = 1, nrow = n_demo_grps, ncol = n_risk_grps
)
# p_susceptibility rows must sum to 1.0
p_susceptibility <- p_susceptibility / rowSums(p_susceptibility)

# using default arguments for `solver` and `control`
final_size(
  r0 = r0,
  contact_matrix = contact_matrix,
  demography_vector = demography_vector,
  susceptibility = susceptibility,
  p_susceptibility = p_susceptibility
)

## Examining the effect of contact reductions
# In this example, contacts are reduced by 5%
final_size(r0, contact_scaling = 0.95)

# Demography-sepcific reduction in contacts
final_size(
  r0 = r0,
  contact_matrix = contact_matrix,
  demography_vector = demography_vector,
  susceptibility = susceptibility,
  p_susceptibility = p_susceptibility,
  contact_scaling = c(0.95, 0.9, 0.85)
)

## Using manually specified solver settings for the iterative solver
control <- list(
  iterations = 100,
  tolerance = 1e-3,
  step_rate = 1.9,
  adapt_step = TRUE
)

final_size(
  r0 = r0,
  contact_matrix = contact_matrix,
  demography_vector = demography_vector,
  susceptibility = susceptibility,
  p_susceptibility = p_susceptibility,
  solver = "iterative",
  control = control
)

## Using manually specified solver settings for the newton solver
control <- list(
  iterations = 100,
  tolerance = 1e-3
)

final_size(
  r0 = r0,
  contact_matrix = contact_matrix,
  demography_vector = demography_vector,
  susceptibility = susceptibility,
  p_susceptibility = p_susceptibility,
  solver = "newton",
  control = control
)
```
