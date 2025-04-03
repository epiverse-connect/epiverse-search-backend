# Converts between epidemiological parameters related to `R_0`

```r
lambda_to_r0(
  lambda,
  contact_matrix,
  demography_vector,
  susceptibility,
  p_susceptibility,
  infectious_period = 1.8
)

r0_to_lambda(
  r0,
  contact_matrix,
  demography_vector,
  susceptibility,
  p_susceptibility,
  infectious_period = 1.8
)

r_eff(
  r0,
  contact_matrix,
  demography_vector,
  susceptibility,
  p_susceptibility,
  contact_scaling = 1
)
```

## Arguments

- `lambda`: The transmission rate of the disease, also called the 'force of infection' (`\lambda`). This is different from the effective transmission rate (`\beta`).
- `contact_matrix`: Social contact matrix. Entry `m_{ij}` gives average number of contacts in group `i` reported by participants in group `j`
- `demography_vector`: Demography vector. Entry `v_{i}` gives proportion of total population in group `i`.
- `susceptibility`: A matrix giving the susceptibility of individuals in demographic group `i` and risk group `k`.
- `p_susceptibility`: A matrix giving the probability that an individual in demography group `i` is in risk (or susceptibility) group `k`. Each row represents the overall distribution of individuals in demographic group `i` across risk groups, and each row **must sum to 1.0**.
- `infectious_period`: Duration of the infectious period in days. Default value is 1.8 days.
- `r0`: The basic reproductive number `R_0` of the infection.
- `contact_scaling`: For `r_eff()`, either a single number or a numeric vector of the same length as `demography_vector`, giving the proportional scaling of contacts of each demographic group. Values must be in the range `[0, 1]`. Defaults to 1.0 for no scaling.

## Returns

Returns a single number for the calculated value.

Converts between `R_0` and the transmission rate `\lambda`, or calculates the effective reproduction number `R_\text{eff}` for a population, while accounting for population characteristics including demographic heterogeneity in social contacts, heterogeneity in the demographic distribution, and heterogeneity in susceptibility to infection.

Uses the R0 (`R_0`), contact matrix (`C`), population (`N`), and infectious period (`\gamma`) to calculate the transmission rate using the following equation. `\lambda = R_0 / ({Max}(EV(C)) \gamma)`

where `EV(C)` denotes the eigenvalues of the matrix `C` which is calculated from the social contacts matrix scaled by the number of individuals in each demographic and susceptibility group in the population.

## Details

Given the transmission rate (`\lambda`), social contacts matrix (`c`), demography (`N`), the distribution `P` of each demographic group `i` into susceptibility groups `S`, and the infectious period (`\gamma`)

 * `r_eff()` calculates the effective reproductive number;
 * `lamda_to_r0()` calculates the `R_0` from the transmission rate as `R_0 = {Max}(EV(C)) \times \lambda \gamma`
 * `r0_to_lambda()` calculates the transmission rate as `\lambda = R_0 / ({Max}(EV(C)) \gamma)`
   
   Note that this is also called the 'force of infection' and is different from the effective transmission rate often denoted `\beta`.

Here, `EV(C)` denotes the eigenvalues of the matrix `C` which is calculated from the social contacts matrix scaled by the number of individuals in each demographic and susceptibility group in the population.

## Examples

```r
#### Prepare data ####
# Get example dataset and prepare contact matrix and demography
data(polymod_uk)
contact_matrix <- polymod_uk$contact_matrix
demography_vector <- polymod_uk$demography_vector

# define lambda
lambda <- 0.3

# define infectious period of 5 days
infectious_period <- 5
# define the number of age and susceptibility groups
n_demo_grps <- length(demography_vector)
n_risk_grps <- 3

# In this example, risk varies across groups
susceptibility <- matrix(
  data = c(0.5, 0.7, 1.0), nrow = n_demo_grps, ncol = n_risk_grps
)

# risk does not vary within groups
p_susceptibility <- matrix(
  data = 1, nrow = n_demo_grps, ncol = n_risk_grps
)
# p_susceptibility rows must sum to 1.0
p_susceptibility <- p_susceptibility / rowSums(p_susceptibility)

#### Effective R ####
r0 <- 2.0
r_eff(
  r0 = r0,
  contact_matrix = contact_matrix,
  demography_vector = demography_vector,
  susceptibility = susceptibility,
  p_susceptibility = p_susceptibility
)

# With a 5% reduction in contacts
r_eff(
  r0 = r0,
  contact_matrix = contact_matrix,
  demography_vector = demography_vector,
  susceptibility = susceptibility,
  p_susceptibility = p_susceptibility,
  contact_scaling = 0.95
)

#### Transmission rate to R0 ####
lambda_to_r0(
  lambda, contact_matrix, demography_vector,
  susceptibility, p_susceptibility,
  infectious_period
)

#### R0 to Transmission rate ####
r0 <- 1.5
r0_to_lambda(
  r0, contact_matrix, demography_vector,
  susceptibility, p_susceptibility,
  infectious_period
)
```
