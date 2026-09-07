import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# extract file
df = pd.read_excel('clean_animal_sleep.xlsx')
# Statical Summary :
print("display statistical information about the dataset")
print(df.describe())
#********
# CORRRELATION MATRIX :
print("display correlation matrix :")
print(df.corr()['total_sleep'].sort_values(ascending=False))

"""-1  ← Negative direction relationship
 0  ← No clear linear relationship
+1  ← Strong positive relationship """

""" Strogest 3 Negative correlation with total_sleep are :
1.sleep_exposure_index → -0.595
2.gestation_time → -0.566
3.danger_index → -0.550
"""
#****************************************************************
# Visualization of Correlation Matrix :
#1.Sleep Exposure Index ↔ Total Sleep
# Scatter plot
plt.scatter(df['sleep_exposure_index'], df['total_sleep'])

plt.xlabel('Sleep Exposure Index')
plt.ylabel('Total Sleep')
plt.title('Sleep Exposure Index vs Total Sleep')

plt.show()
# Box plot
plt.figure(figsize=(8, 5))

df.boxplot(
    column='total_sleep',
    by='sleep_exposure_index'
)

plt.title('Total Sleep by Sleep Exposure Index')
plt.suptitle('')
plt.xlabel('Sleep Exposure Index')
plt.ylabel('Total Sleep')

plt.show()
print(df['danger_index'].nunique())
#****************************************
# 2.Gestation Time ↔ Total Sleep
# Scatter plot
plt.scatter(df['gestation_time'], df['total_sleep'])

plt.xlabel('Gestation Time')
plt.ylabel('Total Sleep')
plt.title('Gestation Time vs Total Sleep')
plt.show()
#*******************************************
#3.Danger Index ↔ Total Sleep
# Scatter plot
plt.scatter(df['danger_index'], df['total_sleep'])

plt.xlabel('Danger Index')
plt.ylabel('Total Sleep')
plt.title('Danger Index vs Total Sleep')
plt.show()
#Box plot
plt.figure(figsize=(8, 5))

df.boxplot(
    column='total_sleep',
    by='danger_index'
)

plt.title('Total Sleep by Danger Index')
plt.suptitle('')
plt.xlabel('Danger Index')
plt.ylabel('Total Sleep')

plt.show()