# Transform Input to an Antibiotic ID

```r
as.ab(x, flag_multiple_results = TRUE, info = interactive(), ...)

is.ab(x)
```

## Arguments

- `x`: a character vector to determine to antibiotic ID
- `flag_multiple_results`: a logical to indicate whether a note should be printed to the console that probably more than one antibiotic drug code or name can be retrieved from a single input value.
- `info`: a logical to indicate whether a progress bar should be printed - the default is `TRUE` only in interactive mode
- `...`: arguments passed on to internal functions

## Returns

A character vector with additional class `ab`

## Description

Use this function to determine the antibiotic drug code of one or more antibiotics. The data set antibiotics will be searched for abbreviations, official names and synonyms (brand names).

## Details

All entries in the antibiotics data set have three different identifiers: a human readable EARS-Net code (column `ab`, used by ECDC and WHONET), an ATC code (column `atc`, used by WHO), and a CID code (column `cid`, Compound ID, used by PubChem). The data set contains more than 5,000 official brand names from many different countries, as found in PubChem. Not that some drugs contain multiple ATC codes.

All these properties will be searched for the user input. The `as.ab()` can correct for different forms of misspelling:

 * Wrong spelling of drug names (such as "tobramicin" or "gentamycin"), which corrects for most audible similarities such as f/ph, x/ks, c/z/s, t/th, etc.
 * Too few or too many vowels or consonants
 * Switching two characters (such as "mreopenem", often the case in clinical data, when doctors typed too fast)
 * Digitalised paper records, leaving artefacts like 0/o/O (zero and O's), B/8, n/r, etc.

Use the `ab_*` functions to get properties based on the returned antibiotic ID, see **Examples**.

Note: the `as.ab()` and `ab_*` functions may use very long regular expression to match brand names of antimicrobial drugs. This may fail on some systems.

You can add your own manual codes to be considered by `as.ab()` and all `ab_*` functions, see `add_custom_antimicrobials()`.

## Source

 World Health Organization (WHO) Collaborating Centre for Drug Statistics Methodology: [https://www.whocc.no/atc_ddd_index/](https://www.whocc.no/atc_ddd_index/)

European Commission Public Health PHARMACEUTICALS - COMMUNITY REGISTER: [https://ec.europa.eu/health/documents/community-register/html/reg_hum_atc.htm](https://ec.europa.eu/health/documents/community-register/html/reg_hum_atc.htm)

## WHOCC

 This package contains all ~550 antibiotic, antimycotic and antiviral drugs and their Anatomical Therapeutic Chemical (ATC) codes, ATC groups and Defined Daily Dose (DDD) from the World Health Organization Collaborating Centre for Drug Statistics Methodology (WHOCC, [https://www.whocc.no](https://www.whocc.no)) and the Pharmaceuticals Community Register of the European Commission ([https://ec.europa.eu/health/documents/community-register/html/reg_hum_atc.htm](https://ec.europa.eu/health/documents/community-register/html/reg_hum_atc.htm)).

These have become the gold standard for international drug utilisation monitoring and research.

The WHOCC is located in Oslo at the Norwegian Institute of Public Health and funded by the Norwegian government. The European Commission is the executive of the European Union and promotes its general interest.

NOTE: The WHOCC copyright does not allow use for commercial purposes,unlike any other info from this package. See [https://www.whocc.no/copyright_disclaimer/.](https://www.whocc.no/copyright_disclaimer/.)

## Reference Data Publicly Available

 All data sets in this `AMR` package (about microorganisms, antibiotics, SIR interpretation, EUCAST rules, etc.) are publicly and freely available for download in the following formats: R, MS Excel, Apache Feather, Apache Parquet, SPSS, SAS, and Stata. We also provide tab-separated plain text files that are machine-readable and suitable for input in any software program, such as laboratory information systems. Please visit [our website for the download links](https://msberends.github.io/AMR/articles/datasets.html). The actual files are of course available on [our GitHub repository](https://github.com/msberends/AMR/tree/main/data-raw).

## Examples

```r
# these examples all return "ERY", the ID of erythromycin:
as.ab("J01FA01")
as.ab("J 01 FA 01")
as.ab("Erythromycin")
as.ab("eryt")
as.ab("   eryt 123")
as.ab("ERYT")
as.ab("ERY")
as.ab("eritromicine") # spelled wrong, yet works
as.ab("Erythrocin") # trade name
as.ab("Romycin") # trade name

# spelling from different languages and dyslexia are no problem
ab_atc("ceftriaxon")
ab_atc("cephtriaxone") # small spelling error
ab_atc("cephthriaxone") # or a bit more severe
ab_atc("seephthriaaksone") # and even this works

# use ab_* functions to get a specific properties (see ?ab_property);
# they use as.ab() internally:
ab_name("J01FA01")
ab_name("eryt")


if (require("dplyr")) {
  # you can quickly rename 'sir' columns using set_ab_names() with dplyr:
  example_isolates %>%
    set_ab_names(where(is.sir), property = "atc")
}
```

## See Also

 * antibiotics for the data.frame that is being used to determine ATCs
 * `ab_from_text()` for a function to retrieve antimicrobial drugs from clinical text (from health care records)



