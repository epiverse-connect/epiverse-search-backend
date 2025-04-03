# Generate probabilities of seropositivity by age based on a general Force-of-Infection (FoI) model.

```r
prob_seroprev_gen_by_age(
  construct_A_fun,
  calculate_seroprev_fun,
  initial_conditions,
  max_age,
  ...
)
```

## Arguments

- `construct_A_fun`: A function that constructs a matrix that defines the multiplier term in the linear ODE system.
- `calculate_seroprev_fun`: A function which takes the state vector and returns the seropositive fraction.
- `initial_conditions`: The initial state vector proportions for each birth cohort.
- `max_age`: The maximum age to simulate seropositivity for.
- `...`: Additional parameters for `construct_A_fun`

## Returns

A dataframe with columns 'age' and 'seropositivity'.

This function calculates the probabilities of seropositivity by age based on an abstract model of the serocatalytic system.

## Examples

```r
# define age- and time-specific multipliers
foi_df_time <- data.frame(
  year = seq(1946, 2025, 1),
  foi = c(rep(0, 40), rep(1, 40))
)

foi_df_age <- data.frame(
  age = 1:80,
  foi = 2 * dlnorm(1:80, meanlog = 3.5, sdlog = 0.5)
)

u <- foi_df_age$foi
v <- foi_df_time$foi

# function to construct A matrix for one piece
construct_A <- function(t, tau, u, v) {
  u_bar <- u[t - tau]
  v_bar <- v[t]

  A <- diag(-1, ncol = 12, nrow = 12)
  A[row(A) == (col(A) + 1)] <- 1
  A[1, 1] <- -u_bar * v_bar
  A[2, 1] <- u_bar * v_bar
  A[12, 12] <- 0

  A
}

# determines the sum of seropositive compartments of those still alive
calculate_seropositivity_fn <- function(Y) {
  sum(Y[2:11]) / (1 - Y[12])
}

# initial conditions in 12D state vector
initial_conditions <- rep(0, 12)
initial_conditions[1] <- 1

# calculate probability
seropositive_hiv <- prob_seroprev_gen_by_age(
  construct_A,
  calculate_seropositivity_fn,
  initial_conditions,
  max_age = 80,
  u,
  v
)
```
