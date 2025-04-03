 data

# Data Set with 4 957 Common Microorganism Codes

## Format

A tibble with 4 957 observations and 2 variables:

 * `code`
   
   Commonly used code of a microorganism. **This is a unique identifier.**
 * `mo`
   
   ID of the microorganism in the microorganisms data set

```r
microorganisms.codes
```

## Description

A data set containing commonly used codes for microorganisms, from laboratory systems and [WHONET](https://whonet.org). Define your own with `set_mo_source()`. They will all be searched when using `as.mo()` and consequently all the `mo_*` functions.

## Details

Like all data sets in this package, this data set is publicly available for download in the following formats: R, MS Excel, Apache Feather, Apache Parquet, SPSS, SAS, and Stata. Please visit [our website for the download links](https://msberends.github.io/AMR/articles/datasets.html). The actual files are of course available on [our GitHub repository](https://github.com/msberends/AMR/tree/main/data-raw).

## Examples

```r
microorganisms.codes

# 'ECO' or 'eco' is the WHONET code for E. coli:
microorganisms.codes[microorganisms.codes$code == "ECO", ]

# and therefore, 'eco' will be understood as E. coli in this package:
mo_info("eco")

# works for all AMR functions:
mo_is_intrinsic_resistant("eco", ab = "vancomycin")
```

## See Also

`as.mo()` microorganisms



