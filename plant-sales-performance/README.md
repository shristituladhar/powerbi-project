# Plant Co. Power BI Sales Performance Dashboard

An interactive Power BI dashboard analyzing plant sales performance from 2022 to 2024, focusing on year-over-year trends, profitability, and segmentation across accounts, countries, and product types.

> Final report is filtered to **2023 & 2024** only, as 2022 data does not support previous-year comparisons.

---

## Dataset Structure

**Source**: Excel file with the following sheets:
- `Fact_Sales` - transactional sales data (quantity, prices, cost, date, product/account IDs)
- `Dim_Product` - product hierarchy (name, type, family, group)
- `Dim_Account` - customer/account data (region, location, name)

**Custom tables created:**
- `Dim_Date` - continuous date table (Jan 2022 to Dec 2024)
- `Slc_Values` - disconnected slicer for metric switching (`Sales`, `Quantity`, `Gross Profit`)

---

## Key Metrics & DAX Logic

- **Sales, Quantity, Gross Profit**
- **YTD** & **PYTD** for all metrics (via `TOTALYTD` + `SAMEPERIODLASTYEAR`)
- **Dynamic measures** using `SWITCH` based on user-selected metric
- **GP%** calculated using `DIVIDE([Gross Profit], [Sales])`
- **Inpast flag** (`TRUE/FALSE`) in `Dim_Date` for controlling PYTD boundaries

---

## Dashboard Features

| Element                                | Description |
|----------------------------------------|-------------|
| KPI Cards                           | YTD, PYTD, YTD vs PYTD, GP% - all dynamic |
| Treemap                             | Bottom 10 countries by YTD vs PYTD drop |
| Waterfall Chart                     | YTD vs PYTD breakdown by month |
| Combo Bar + Line                    | Monthly comparison of YTD and PYTD |
| Scatter Plot                        | Account-level segmentation by GP% and Quantity |
| Date Slicer                         | Year filtered to **2023 & 2024** |
| Metric Selector (Slicer)            | Switches entire report between Sales, Quantity, Gross Profit |
| Dynamic Visual Titles               | Powered by slicer with `SELECTEDVALUE` |
| Conditional Formatting              | Applied to highlight negative growth |
| Drilldown Enabled                   | For exploring trends by month, product, or country |

---

## Data Modeling Approach

- **Star schema**: Fact table joined cleanly to `Dim_Product`, `Dim_Account`, and `Dim_Date`
- **One-to-many relationships** with surrogate keys
- **Disconnected tables** for slicers and dynamic visuals
- **Display folders** for measure organization (`YTD`, `PYTD`, `SWITCH`, `Base Measures`, etc.)
- **Columns and helper measures hidden** to maintain a clean report view

---

## Tools Used

- Power BI Desktop
- Power Query Editor
- DAX (`CALCULATE`, `SWITCH`, `TOTALYTD`, `SAMEPERIODLASTYEAR`, `DIVIDE`, `SELECTEDVALUE`)
- Conditional formatting & dynamic field-driven titles

---

## Insights Unlocked

- Drop in Quantity performance in March–April 2024 vs PYTD
- Major YTD underperformance by countries like Canada & USA
- Profitability cluster analysis by account (high GP% vs high volume)
- Dynamic, user-driven exploration of performance metrics

---
