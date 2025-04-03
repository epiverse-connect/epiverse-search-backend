# Neighborhoods from real travel distances in Colombia

```r
neighborhoods(query_vector, threshold = 2)
```

## Arguments

- `query_vector`: Codes of the municipalities to consider for the neighborhoods.
- `threshold`: Maximum traveling time around each municipality.

## Returns

neighborhood object according to the introduced threshold.

Function to build neighborhoods from real travel distances inside Colombia by land or river transportation.

## Examples

```r
query_vector <- c("05001", "05002", "05004", "05021", "05030", "05615")
neighborhoods(query_vector, 2)
```
