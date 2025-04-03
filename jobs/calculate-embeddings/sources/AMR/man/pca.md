# Principal Component Analysis (for AMR)

```r
pca(
  x,
  ...,
  retx = TRUE,
  center = TRUE,
  scale. = TRUE,
  tol = NULL,
  rank. = NULL
)
```

## Arguments

- `x`: a data.frame containing numeric columns
- `...`: columns of `x` to be selected for PCA, can be unquoted since it supports quasiquotation.
- `retx`: a logical value indicating whether the rotated variables should be returned.
- `center`: a logical value indicating whether the variables should be shifted to be zero centered. Alternately, a vector of length equal the number of columns of `x` can be supplied. The value is passed to `scale`.
- `scale.`: a logical value indicating whether the variables should be scaled to have unit variance before the analysis takes place. The default is `FALSE` for consistency with S, but in general scaling is advisable. Alternatively, a vector of length equal the number of columns of `x` can be supplied. The value is passed to `scale`.
- `tol`: a value indicating the magnitude below which components should be omitted. (Components are omitted if their standard deviations are less than or equal to `tol` times the standard deviation of the first component.) With the default null setting, no components are omitted (unless `rank.` is specified less than `min(dim(x))`.). Other settings for tol could be `tol = 0` or `tol = sqrt(.Machine$double.eps)`, which would omit essentially constant components.
- `rank.`: optionally, a number specifying the maximal rank, i.e., maximal number of principal components to be used. Can be set as alternative or in addition to `tol`, useful notably when the desired rank is considerably smaller than the dimensions of the matrix.

## Returns

An object of classes pca and prcomp

## Description

Performs a principal component analysis (PCA) based on a data set with automatic determination for afterwards plotting the groups and labels, and automatic filtering on only suitable (i.e. non-empty and numeric) variables.

## Details

The `pca()` function takes a data.frame as input and performs the actual PCA with the function `prcomp()`.

The result of the `pca()` function is a prcomp object, with an additional attribute `non_numeric_cols` which is a vector with the column names of all columns that do not contain numeric values. These are probably the groups and labels, and will be used by `ggplot_pca()`.

## Examples

```r
# `example_isolates` is a data set available in the AMR package.
# See ?example_isolates.


if (require("dplyr")) {
  # calculate the resistance per group first
  resistance_data <- example_isolates %>%
    group_by(
      order = mo_order(mo), # group on anything, like order
      genus = mo_genus(mo)
    ) %>% #   and genus as we do here;
    filter(n() >= 30) %>% # filter on only 30 results per group
    summarise_if(is.sir, resistance) # then get resistance of all drugs

  # now conduct PCA for certain antimicrobial drugs
  pca_result <- resistance_data %>%
    pca(AMC, CXM, CTX, CAZ, GEN, TOB, TMP, SXT)

  pca_result
  summary(pca_result)

  # old base R plotting method:
  biplot(pca_result)
  # new ggplot2 plotting method using this package:
  if (require("ggplot2")) {
    ggplot_pca(pca_result)

    ggplot_pca(pca_result) +
      scale_colour_viridis_d() +
      labs(title = "Title here")
  }
}
```



