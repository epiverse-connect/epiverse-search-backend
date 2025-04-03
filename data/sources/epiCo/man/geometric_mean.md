# Returns the geometric mean of a vector of real numbers.

```r
geometric_mean(
  x,
  method = c("positive", "shifted", "optimized", "weighted"),
  shift = 1,
  epsilon = 0.001
)
```

## Arguments

- `x`: A numeric vector of real values
- `method`: Description of methods:
    
     * positive = only positive values within x are used in the calculation.
     * shifted = positive and zero values within x are used by adding a shift value before the calculation and subtracting it to the final result.
     * optimized = optimized shifted method. See: De La Cruz, R., & Kreft, J. U. (2018). Geometric mean extension for data sets with zeros. arXiv preprint arXiv:1806.06403.
     * weighted = a probability weighted calculation of gm for negative, positive, and zero values. See: Habib, E. A. (2012). Geometric mean for negative and zero values. International Journal of Research and Reviews in Applied Sciences, 11(3), 419-432.
- `shift`: = 1 (default) a positive value to use in the shifted method
- `epsilon`: = 1e-5 (default) the minimum positive value to consider in the optimized method.

## Returns

The geometric mean of the x vector, and the epsilon value if optimized method is used.

Function that returns the geometric mean of a vector of real numbers according to the selected method.

## Examples

```r
x <- c(4, 5, 3, 7, 8)
geometric_mean(x, method = "optimized")
```
