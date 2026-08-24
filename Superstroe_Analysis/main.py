from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
BASE_DIR = Path(__file__).resolve().parent
#********************************
def load_and_clean_data():
 df = pd.read_excel(BASE_DIR / "train.xlsx")
#********************************
# Data cleaning :
#cleaning Headers :
 print(df.isna().sum())
 print(df.duplicated().sum())
 print(df.shape)
 print(df.info())
 print(df.nunique())
#********************************
# celaning column names and  text cells in columns :
 df.columns = df.columns.str.strip().str.replace(' ', '_')
 print(df.columns)
 dup_product_id=df[df.duplicated(subset=['Product_ID'], keep=False)] # checking for duplicate Product_IDs
 print(dup_product_id)
 text_columns = [    'Customer_Name',
    'City',
    'State',
    'Region',
    'Category',
    'Sub-Category',
    'Product_Name',
    'Order_ID',
    'Ship_Mode',
    'Segment',
     'Customer_ID',
     'Customer_Name',
     'Product_ID',
     'Product_Name'
     ] # selecting text columns 
 for col in text_columns:
    df[col] = df[col].str.strip() # cleaning text columns
    df[col] = df[col].replace('nan', np.nan) # replacing strings with NaN
    df[col] = df[col].str.title() # converting  first letter from each word to title case (upper case)
#********************************
# celaning Dates and  int cells in columns :
 df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce') # converting to datetime format
 df['Row_ID']=pd.to_numeric(df['Row_ID'], errors='coerce').astype("Int64") # converting to numeric format and make sure to keep NaN values Integer type
 df['Postal_Code'] = pd.to_numeric(df['Postal_Code'], errors='coerce').astype("Int64") # converting to numeric format and make sure to keep NaN values Integer type
 df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce') # converting to numeric format
# Feature engineering
 df['Order_Year'] = df['Order_Date'].dt.year # extracting year from Order_Date column
 df['Order_Month'] = df['Order_Date'].dt.to_period('M').dt.to_timestamp() # extracting month with his yearfrom Order_Date column
 df['Daily_Date'] = df['Order_Date'].dt.date # converting to date format
#*********************************
  # Fill missing Sales values with the median of each product and then fill remaining NaN values with the median of the whole column
 df['Sales'] = df.groupby('Product_Name')['Sales'].transform(lambda x: x.fillna(x.median())) # filling NaN values in Sales column with the median of each product
 df['Sales'] = df['Sales'].fillna(df['Sales'].median()) # filling NaN values in Sales column with the median of the whole column ,that is for the products that have all NaN values in Sales column or new products that have no sales yet. 
 df.to_excel(BASE_DIR / "cleaned_data.xlsx", index=False)
 return df
#*****************************************************************************************
