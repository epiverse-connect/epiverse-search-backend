# Climate aggregation rules

```r
daily_tssm(group)
```

## Arguments

- `group`: `data.frame` object with filtered and grouped data.

## Returns

numeric value calculated.

Climate temporal aggregation rules are provided by the source, and guarantee data quality given missing information. These rules are included in the package to make the download and aggregation process easier for the user. The aggregation is not available for all climate data, and is only available for information under the tags `TSSM_CON`, `TMN_CON`, `TMX_CON`, `PTPM_CON`, and `BSHG_CON`. Internal functions are provided as a set of comprehensible rules to aggregate the data for daily, monthly and annual frequencies.

## Methods

Aggregation can only be performed from the previous level, meaning for monthly aggregation, the data must be already aggregated daily, and for annual aggregation the data must be monthly.
