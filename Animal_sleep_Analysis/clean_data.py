import pandas as pd
import numpy as np
# extract file
df = pd.read_excel('dataset_2191_sleep.xlsx')
df = df.replace('?', np.nan) # replace '?' with NaN
# info about the dataset
print("display information about the dataset")
print(df.info())
print("*"*50)
print("display statistical information about the dataset")
print(df.describe())
print("*"*50)
#*****************
# Data Cleaning
#cleaning Headers :
print("display number of missing values in each column")
print(df.isna().sum())
print("*"*50)
print("display number of duplicate rows")
print(df.duplicated().sum())
print("*"*50)
print("display shape of the dataset")
print(df.shape)
print("*"*50)
print("display number of unique values in each column")
print(df.nunique())
print("*"*50)
# convert columns to numeric types
cols = ['max_life_span', 'gestation_time', 'total_sleep']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
print(df.info())
#*********************************
print("Rows with missing values:")
print(df[df.isna().any(axis=1)])
print("*"*50)
#***********************
# cleainng column names :
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
)
#************************
# Outlier Detection using IQR :

print("Outliers in each column:")
numeric_cols = [
    'body_weight',
    'brain_weight',
    'max_life_span',
    'gestation_time',
    'total_sleep'
]

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    
    print(f"{col}: {len(outliers)} outliers")
print("*"*50)
#***********************
#Validate ranges :
print("Validating ranges:")
index_cols = [
    'predation_index',
    'sleep_exposure_index',
    'danger_index'
]

for col in index_cols:
    invalid = df[~df[col].between(1, 5)]
    print(f"{col}: {len(invalid)} invalid values")
print("*"*50)
#****************************************************
# physical measuers :
print("Validating physical measures:")
positive_cols = [
    'body_weight',
    'brain_weight',
    'max_life_span',
    'gestation_time',
    'total_sleep'
]

for col in positive_cols:
    invalid = df[df[col] <= 0]
    print(f"{col}: {len(invalid)} invalid values")
print("*"*50)
#************************************************
# processing Missing Values :
print("Processing Missing Values:")
print(df[['max_life_span', 'gestation_time', 'total_sleep']].median())
for col in  ['max_life_span', 'gestation_time', 'total_sleep']:
    df[col] = df[col].fillna(df[col].median())
print(df.isna().sum())    
"""now we have cleaned the dataset and handled missing values, outliers,
 and invalid ranges. The next steps would typically involve further analysis or modeling based on the cleaned data."""
# Export cleaned dataset
df.to_excel('clean_animal_sleep.xlsx', index=False)
print("\nCleaned dataset exported successfully!")