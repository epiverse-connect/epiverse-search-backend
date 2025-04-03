# **G**-test for Count Data

## Source

The code for this function is identical to that of `chisq.test()`, except that:

 * The calculation of the statistic was changed to `2 * sum(x * log(x / E))`
 * Yates' continuity correction was removed as it does not apply to a **G**-test
 * The possibility to simulate p values with `simulate.p.value` was removed

```r
g.test(x, y = NULL, p = rep(1/length(x), length(x)), rescale.p = FALSE)
```

## Arguments

- `x`: a numeric vector or matrix. `x` and `y` can also both be factors.
- `y`: a numeric vector; ignored if `x` is a matrix. If `x` is a factor, `y` should be a factor of the same length.
- `p`: a vector of probabilities of the same length as `x`. An error is given if any entry of `p` is negative.
- `rescale.p`: a logical scalar; if TRUE then `p` is rescaled (if necessary) to sum to 1. If `rescale.p` is FALSE, and `p` does not sum to 1, an error is given.

## Returns

A list with class `"htest"` containing the following components: - **statistic**: the value the chi-squared test statistic.

 - **parameter**: the degrees of freedom of the approximate chi-squared distribution of the test statistic, `NA` if the p-value is computed by Monte Carlo simulation.

 - **p.value**: the p-value for the test.

 - **method**: a character string indicating the type of test performed, and whether Monte Carlo simulation or continuity correction was used.

 - **data.name**: a character string giving the name(s) of the data.

 - **observed**: the observed counts.

 - **expected**: the expected counts under the null hypothesis.

 - **residuals**: the Pearson residuals, `(observed - expected) / sqrt(expected)`.

 - **stdres**: standardized residuals, `(observed - expected) / sqrt(V)`, where `V` is the residual cell variance (Agresti, 2007, section 2.4.5 for the case where `x` is a matrix, `n * p * (1 - p)` otherwise).

## Description

`g.test()` performs chi-squared contingency table tests and goodness-of-fit tests, just like `chisq.test()` but is more reliable (1). A **G**-test can be used to see whether the number of observations in each category fits a theoretical expectation (called a _G_-test of goodness-of-fit ), or to see whether the proportions of one variable are different for different values of the other variable (called a _G_-test of independence ).

## Details

If `x` is a matrix with one row or column, or if `x` is a vector and `y` is not given, then a **goodness-of-fit test** is performed (`x` is treated as a one-dimensional contingency table). The entries of `x` must be non-negative integers. In this case, the hypothesis tested is whether the population probabilities equal those in `p`, or are all equal if `p` is not given.

If `x` is a matrix with at least two rows and columns, it is taken as a two-dimensional contingency table: the entries of `x` must be non-negative integers. Otherwise, `x` and `y` must be vectors or factors of the same length; cases with missing values are removed, the objects are coerced to factors, and the contingency table is computed from these. Then Pearson's chi-squared test is performed of the null hypothesis that the joint distribution of the cell counts in a 2-dimensional contingency table is the product of the row and column marginals.

The p-value is computed from the asymptotic chi-squared distribution of the test statistic.

In the contingency table case simulation is done by random sampling from the set of all contingency tables with given marginals, and works only if the marginals are strictly positive. Note that this is not the usual sampling situation assumed for a chi-squared test (such as the **G**-test) but rather that for Fisher's exact test.

In the goodness-of-fit case simulation is done by random sampling from the discrete distribution specified by `p`, each sample being of size `n = sum(x)`. This simulation is done in and may be slow.

### **G**-test Of Goodness-of-Fit (Likelihood Ratio Test)

 Use the **G**-test of goodness-of-fit when you have one nominal variable with two or more values (such as male and female, or red, pink and white flowers). You compare the observed counts of numbers of observations in each category with the expected counts, which you calculate using some kind of theoretical expectation (such as a 1:1 sex ratio or a 1:2:1 ratio in a genetic cross).

If the expected number of observations in any category is too small, the **G**-test may give inaccurate results, and you should use an exact test instead (`fisher.test()`).

The **G**-test of goodness-of-fit is an alternative to the chi-square test of goodness-of-fit (`chisq.test()`); each of these tests has some advantages and some disadvantages, and the results of the two tests are usually very similar.

### **G**-test of Independence

 Use the **G**-test of independence when you have two nominal variables, each with two or more possible values. You want to know whether the proportions for one variable are different among values of the other variable.

It is also possible to do a **G**-test of independence with more than two nominal variables. For example, Jackson et al. (2013) also had data for children under 3, so you could do an analysis of old vs. young, thigh vs. arm, and reaction vs. no reaction, all analyzed together.

Fisher's exact test (`fisher.test()`) is an exact test, where the **G**-test is still only an approximation . For any 2x2 table, Fisher's Exact test may be slower but will still run in seconds, even if the sum of your observations is multiple millions.

The **G**-test of independence is an alternative to the chi-square test of independence (`chisq.test()`), and they will give approximately the same results.

### How the Test Works

 Unlike the exact test of goodness-of-fit (`fisher.test()`), the **G**-test does not directly calculate the probability of obtaining the observed results or something more extreme. Instead, like almost all statistical tests, the **G**-test has an intermediate step; it uses the data to calculate a test statistic that measures how far the observed data are from the null expectation. You then use a mathematical relationship, in this case the chi-square distribution, to estimate the probability of obtaining that value of the test statistic.

The **G**-test uses the log of the ratio of two likelihoods as the test statistic, which is why it is also called a likelihood ratio test or log-likelihood ratio test. The formula to calculate a **G**-statistic is:

`G = 2 * sum(x * log(x / E))`

where `E` are the expected values. Since this is chi-square distributed, the p value can be calculated in with:

 

```
p <- stats::pchisq(G, df, lower.tail = FALSE)
```

 

where `df` are the degrees of freedom.

If there are more than two categories and you want to find out which ones are significantly different from their null expectation, you can use the same method of testing each category vs. the sum of all categories, with the Bonferroni correction. You use **G**-tests for each category, of course.

## Examples

```r
# = EXAMPLE 1 =
# Shivrain et al. (2006) crossed clearfield rice (which are resistant
# to the herbicide imazethapyr) with red rice (which are susceptible to
# imazethapyr). They then crossed the hybrid offspring and examined the
# F2 generation, where they found 772 resistant plants, 1611 moderately
# resistant plants, and 737 susceptible plants. If resistance is controlled
# by a single gene with two co-dominant alleles, you would expect a 1:2:1
# ratio.

x <- c(772, 1611, 737)
g.test(x, p = c(1, 2, 1) / 4)

# There is no significant difference from a 1:2:1 ratio.
# Meaning: resistance controlled by a single gene with two co-dominant
# alleles, is plausible.


# = EXAMPLE 2 =
# Red crossbills (Loxia curvirostra) have the tip of the upper bill either
# right or left of the lower bill, which helps them extract seeds from pine
# cones. Some have hypothesized that frequency-dependent selection would
# keep the number of right and left-billed birds at a 1:1 ratio. Groth (1992)
# observed 1752 right-billed and 1895 left-billed crossbills.

x <- c(1752, 1895)
g.test(x)

# There is a significant difference from a 1:1 ratio.
# Meaning: there are significantly more left-billed birds.
```

## References

1. McDonald, J.H. 2014. Handbook of Biological Statistics (3rd ed.) . Sparky House Publishing, Baltimore, Maryland. [http://www.biostathandbook.com/gtestgof.html](http://www.biostathandbook.com/gtestgof.html).

## See Also

`chisq.test()`



