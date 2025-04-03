# Add Custom Microorganisms

```r
add_custom_microorganisms(x)

clear_custom_microorganisms()
```

## Arguments

- `x`: a data.frame resembling the microorganisms data set, at least containing column "genus" (case-insensitive)

## Description

With `add_custom_microorganisms()` you can add your own custom microorganisms, such the non-taxonomic outcome of laboratory analysis.

## Details

This function will fill in missing taxonomy for you, if specific taxonomic columns are missing, see **Examples**.

Important: Due to how works, the `add_custom_microorganisms()` function has to be run in every session - added microorganisms are not stored between sessions and are thus lost when is exited.

There are two ways to circumvent this and automate the process of adding microorganisms:

Method 1: Using the package option `AMR_custom_mo`, which is the preferred method. To use this method:

1. Create a data set in the structure of the microorganisms data set (containing at the very least column "genus") and save it with `saveRDS()` to a location of choice, e.g. `"~/my_custom_mo.rds"`, or any remote location.
2. Set the file location to the package option `AMR_custom_mo`: `options(AMR_custom_mo = "~/my_custom_mo.rds")`. This can even be a remote file location, such as an https URL. Since options are not saved between sessions, it is best to save this option to the `.Rprofile` file so that it will be loaded on start-up of . To do this, open the `.Rprofile` file using e.g. `utils::file.edit("~/.Rprofile")`, add this text and save the file:
   
    
   
   ```
   # Add custom microorganism codes:
   options(AMR_custom_mo = "~/my_custom_mo.rds")
   ```
   
    
   
   Upon package load, this file will be loaded and run through the `add_custom_microorganisms()` function.

Method 2: Loading the microorganism directly from your `.Rprofile` file. Note that the definitions will be stored in a user-specific file, which is a suboptimal workflow. To use this method:

1. Edit the `.Rprofile` file using e.g. `utils::file.edit("~/.Rprofile")`.
2. Add a text like below and save the file:
   
    
   
   ```
   # Add custom antibiotic drug codes:
    AMR::add_custom_microorganisms(
      data.frame(genus = "Enterobacter",
            species = "asburiae/cloacae")
    )
   ```

Use `clear_custom_microorganisms()` to clear the previously added microorganisms.

## Examples

```r
# a combination of species is not formal taxonomy, so
# this will result in "Enterobacter cloacae cloacae",
# since it resembles the input best:
mo_name("Enterobacter asburiae/cloacae")

# now add a custom entry - it will be considered by as.mo() and
# all mo_*() functions
add_custom_microorganisms(
  data.frame(
    genus = "Enterobacter",
    species = "asburiae/cloacae"
  )
)

# E. asburiae/cloacae is now a new microorganism:
mo_name("Enterobacter asburiae/cloacae")

# its code:
as.mo("Enterobacter asburiae/cloacae")

# all internal algorithms will work as well:
mo_name("Ent asburia cloacae")

# and even the taxonomy was added based on the genus!
mo_family("E. asburiae/cloacae")
mo_gramstain("Enterobacter asburiae/cloacae")

mo_info("Enterobacter asburiae/cloacae")


# the function tries to be forgiving:
add_custom_microorganisms(
  data.frame(
    GENUS = "BACTEROIDES / PARABACTEROIDES SLASHLINE",
    SPECIES = "SPECIES"
  )
)
mo_name("BACTEROIDES / PARABACTEROIDES")
mo_rank("BACTEROIDES / PARABACTEROIDES")

# taxonomy still works, even though a slashline genus was given as input:
mo_family("Bacteroides/Parabacteroides")


# for groups and complexes, set them as species or subspecies:
add_custom_microorganisms(
  data.frame(
    genus = "Citrobacter",
    species = c("freundii", "braakii complex"),
    subspecies = c("complex", "")
  )
)
mo_name(c("C. freundii complex", "C. braakii complex"))
mo_species(c("C. freundii complex", "C. braakii complex"))
mo_gramstain(c("C. freundii complex", "C. braakii complex"))
```

## See Also

`add_custom_antimicrobials()` to add custom antimicrobials.



