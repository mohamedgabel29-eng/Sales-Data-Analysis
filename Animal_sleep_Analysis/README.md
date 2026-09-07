# Animal Sleep Data Analysis

A data cleaning and exploratory data analysis (EDA) project on an animal sleep dataset, exploring how physiological and environmental factors relate to total sleep duration across species.

## Project Structure

```
animal-sleep-analysis/
│
├── clean_data.py              # Data cleaning script
├── eda.py                     # Exploratory data analysis script
├── clean_animal_sleep.xlsx    # Cleaned dataset (output of clean_data.py)
└── README.md
```

## Dataset

The dataset contains physiological and behavioral measurements for various animal species, including:

- `body_weight`, `brain_weight` — physical measurements
- `max_life_span`, `gestation_time` — life history traits
- `total_sleep` — total sleep duration (target variable)
- `predation_index`, `sleep_exposure_index`, `danger_index` — indices (rated 1–5) reflecting predation risk and exposure while sleeping

## 1. Data Cleaning (`clean_data.py`)

Steps performed on the raw dataset (`dataset_2191_sleep.xlsx`):

- Replaced `'?'` placeholders with `NaN`
- Converted key columns (`max_life_span`, `gestation_time`, `total_sleep`) to numeric types
- Standardized column names (lowercase, stripped, underscores)
- Detected outliers in numeric columns using the IQR method
- Validated index columns (`predation_index`, `sleep_exposure_index`, `danger_index`) against an expected range of 1–5
- Validated that physical measurement columns contain only positive values
- Handled missing values by imputing with the column median
- Exported the cleaned dataset to `clean_animal_sleep.xlsx`

## 2. Exploratory Data Analysis (`eda.py`)

- Generated descriptive statistics for the cleaned dataset
- Computed the correlation matrix against `total_sleep`

The three strongest negative correlations with `total_sleep` were:

| Rank | Feature | Correlation |
|------|---------|-------------|
| 1 | `sleep_exposure_index` | -0.595 |
| 2 | `gestation_time` | -0.566 |
| 3 | `danger_index` | -0.550 |

### Key Relationships Explored

**Sleep Exposure Index ↔ Total Sleep**
Visualized with a scatter plot and a boxplot grouped by index value.
The relationship is not strictly linear — sleep does not decrease steadily as exposure increases across all levels. However, at `sleep_exposure_index = 5`, there is a sharp drop in total sleep, suggesting a possible threshold effect rather than a gradual trend. This is a notable insight, particularly since the index is built from variables related to predation/exposure risk. Note that the boxplot alone shows an *association*, not causation.

**Gestation Time ↔ Total Sleep**
Visualized with a scatter plot, showing a negative relationship — species with longer gestation periods tend to sleep less.

**Danger Index ↔ Total Sleep**
Visualized with a scatter plot and a boxplot grouped by index value, following the same pattern of analysis used for `sleep_exposure_index`.

## Tools Used

- Python (pandas, numpy, matplotlib)
- Power BI (for further dashboarding, in progress)

## Next Steps

- Build interactive dashboards in Power BI using the cleaned dataset
- Further explore additional relationships in the dataset