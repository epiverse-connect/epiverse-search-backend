# Convert a vector string of spelled numbers in a supported language to its numeric equivalent.

```r
numberize(text, lang = c("en", "fr", "es"))
```

## Arguments

- `text`: String vector of spelled numbers in a supported language.
- `lang`: The text's language. Currently one of `c("en", "fr", "es")`. Default is "en"

## Returns

A numeric vector.

The range of words supported is between zero and nine hundred and ninety nine trillion, nine hundred and

ninety nine billion, nine hundred and ninety nine million, nine

hundred and ninety nine thousand, nine hundred and ninety nine

## Examples

```r
# convert to numbers a scalar
numberize("five hundred and thirty eight")

# convert a vector of values
numberize(c("dix", "soixante-cinq", "deux mille vingt-quatre"), lang = "fr")
```
