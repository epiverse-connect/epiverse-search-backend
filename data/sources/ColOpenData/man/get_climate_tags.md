# List climate (IDEAM) tags

```r
get_climate_tags(language = "ES")
```

## Arguments

- `language`: character with the language of the tags (`"EN"` or `"ES"`. Default is `"ES"`.

## Returns

`data.frame` object with available climate tags.

Retrieve available climate tags to be consulted. The list is only available in Spanish.

## Examples

```r
dict <- get_climate_tags("ES")
head(dict)
```
