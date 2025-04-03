# Filter list of available datasets based on keywords given by the user

```r
look_up(keywords, module = "all", logic = "or", language = "EN")
```

## Arguments

- `keywords`: character or vector of characters to be look up in the description.
- `module`: character with module to be consulted (`"demographic"`, `"geospatial"`, `"climate"`). Default is `"all"`.
- `logic`: A character string specifying the matching logic. Can be either `"or"` or `"and"`. Default is `"or"`:
    
     * `logic = "or"`: Matches rows containing at least one of the specified keywords in their descriptions.
     * `logic = "and"`: Matches rows containing all of the specified keywords in their descriptions.
- `language`: character with the language of the keywords (`"EN"` or `"ES"`. Default is `"EN"`.

## Returns

`data.frame` object with the available datasets containing information related to the consulted keywords.

List available datasets containing user-specified keywords in their descriptions.

## Examples

```r
found <- look_up(c("sex", "age"), "demographic", "and", "EN")
head(found)
```
