# Construct a new vaccination regime for an epidemic model

```r
vaccination(name = NA_character_, nu, time_begin, time_end)

is_vaccination(x)

## S3 method for class 'vaccination'
c(x, ...)
```

## Arguments

- `name`: String for the name of the vaccination regime.
- `nu`: Matrix for the group-specific rate of vaccination, expressed as the rate parameter `nu`. Each element of the matrix `nu_{ij}` represents the rate of delivering vaccine dose `j` to demographic group `i`.
- `time_begin`: Matrix for the start time of delivering vaccination dose `j` to demographic group `i`. demographic group `i`.
- `time_end`: Matrix for the end time of delivering vaccination dose `j` to demographic group `i`.
- `x`: A `<vaccination>` object, or an object to be checked as being a `<vaccination>`.
- `...`: Vaccination objects to combine with `x` to create a multi-dose `<vaccination>` object.

## Returns

An object of the `<vaccination>` S3 class.

`vaccination()` returns a `<vaccination>` object with the specified parameters.

Concatenating two or more `<vaccination>` objects using `c()` also returns a `<vaccination>` object. This object holds the group-specific start and end times, and group-specific vaccination rates specified by all the constituent vaccination regimes.

`.no_vaccination()` returns a `<vaccination>` that has no effect on the population, with start and end times set to 0.0, and the rate of vaccination `nu` also set to 0.0.

`is_vaccination()` return a logical for whether the object is of the `<vaccination>` class.

Prepare a `<vaccination>` object that specifies a vaccination regime for use in an epidemic model. These objects can handle different vaccination start and end times, as well as different vaccination rates, for each demographic group in the epidemic modelling scenario.

Combine `<vaccination>` objects to create multi-dose vaccination regimes using `c()` on two or more `<vaccination>` objects.

## Details

Multi-dose vaccinations can be passed to all epidemic models, but not all models accommodate multi-dose vaccinations. For example, the default SEIR-V model provided by `model_default()` has only a single vaccinated compartment, and will only use the first parameter set of a multi-dose regime to determine how individuals transition into the vaccinated compartment.

In contrast, the Vacamole model considers two doses, and will make use of the first two parameter sets of a multi-dose regime. More doses can be specified, but will be disregarded by this model.

## Examples

```r
# Assuming a population with two age groups, children 0 -- 5, and others 5+
# an example for childhood vaccination only
childhood_vaccination <- vaccination(
  name = "childhood_vaccination",
  time_begin = matrix(c(0, 100)), # assuming a simulation over 100 days
  time_end = matrix(c(100, 100)),
  nu = matrix(c(0.0001, 0.0)) # over 5s never vaccinated
)
childhood_vaccination

# check whether the object is a <vaccination>
is_vaccination(childhood_vaccination)

# Concatenating vaccinations
# create first dose regime
vax_1 <- vaccination(
  name = "vax_regime",
  time_begin = matrix(1),
  time_end = matrix(100),
  nu = matrix(0.001)
)

# second dose regime
vax_2 <- vaccination(
  name = "vax_regime",
  time_begin = matrix(101),
  time_end = matrix(200),
  nu = matrix(0.001)
)

c(vax_1, vax_2)
```
