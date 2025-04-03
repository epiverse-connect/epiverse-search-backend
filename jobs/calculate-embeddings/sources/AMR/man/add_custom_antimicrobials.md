# Add Custom Antimicrobials

```r
add_custom_antimicrobials(x)

clear_custom_antimicrobials()
```

## Arguments

- `x`: a data.frame resembling the antibiotics data set, at least containing columns "ab" and "name"

## Description

With `add_custom_antimicrobials()` you can add your own custom antimicrobial drug names and codes.

## Details

Important: Due to how works, the `add_custom_antimicrobials()` function has to be run in every session - added antimicrobials are not stored between sessions and are thus lost when is exited.

There are two ways to circumvent this and automate the process of adding antimicrobials:

Method 1: Using the package option `AMR_custom_ab`, which is the preferred method. To use this method:

1. Create a data set in the structure of the antibiotics data set (containing at the very least columns "ab" and "name") and save it with `saveRDS()` to a location of choice, e.g. `"~/my_custom_ab.rds"`, or any remote location.
2. Set the file location to the package option `AMR_custom_ab`: `options(AMR_custom_ab = "~/my_custom_ab.rds")`. This can even be a remote file location, such as an https URL. Since options are not saved between sessions, it is best to save this option to the `.Rprofile` file so that it will be loaded on start-up of . To do this, open the `.Rprofile` file using e.g. `utils::file.edit("~/.Rprofile")`, add this text and save the file:
   
    
   
   ```
   # Add custom antimicrobial codes:
   options(AMR_custom_ab = "~/my_custom_ab.rds")
   ```
   
    
   
   Upon package load, this file will be loaded and run through the `add_custom_antimicrobials()` function.

Method 2: Loading the antimicrobial additions directly from your `.Rprofile` file. Note that the definitions will be stored in a user-specific file, which is a suboptimal workflow. To use this method:

1. Edit the `.Rprofile` file using e.g. `utils::file.edit("~/.Rprofile")`.
2. Add a text like below and save the file:
   
    
   
   ```
   # Add custom antibiotic drug codes:
    AMR::add_custom_antimicrobials(
      data.frame(ab = "TESTAB",
            name = "Test Antibiotic",
            group = "Test Group")
    )
   ```

Use `clear_custom_antimicrobials()` to clear the previously added antimicrobials.

## Examples

```r
# returns NA and throws a warning (which is suppressed here):
suppressWarnings(
  as.ab("testab")
)

# now add a custom entry - it will be considered by as.ab() and
# all ab_*() functions
add_custom_antimicrobials(
  data.frame(
    ab = "TESTAB",
    name = "Test Antibiotic",
    # you can add any property present in the
    # 'antibiotics' data set, such as 'group':
    group = "Test Group"
  )
)

# "testab" is now a new antibiotic:
as.ab("testab")
ab_name("testab")
ab_group("testab")

ab_info("testab")


# Add Co-fluampicil, which is one of the many J01CR50 codes, see
# https://www.whocc.no/ddd/list_of_ddds_combined_products/
add_custom_antimicrobials(
  data.frame(
    ab = "COFLU",
    name = "Co-fluampicil",
    atc = "J01CR50",
    group = "Beta-lactams/penicillins"
  )
)
ab_atc("Co-fluampicil")
ab_name("J01CR50")

# even antibiotic selectors work
x <- data.frame(
  random_column = "some value",
  coflu = as.sir("S"),
  ampicillin = as.sir("R")
)
x
x[, betalactams()]
```

## See Also

`add_custom_microorganisms()` to add custom microorganisms.



