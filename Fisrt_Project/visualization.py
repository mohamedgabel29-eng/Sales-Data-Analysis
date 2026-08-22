import matplotlib.pyplot as plt
from main import load_and_clean_data
"""Data clreaning and wrangling is done, now we can start with data visualization and analysis with Matplotlib libraries"""
# Get cleaned data
df = load_and_clean_data()
# =========================
# Data Analysis
# =========================
#Grouped by Category and Sub-Category,Order_Monthly,Order_Year to calculate total revenue 
cat_revenue = df.groupby('Category').agg(cat_revenue=('Sales', 'sum'), items=('Sales', 'count')).sort_values('cat_revenue', ascending=False) # calculating total revenue for each category and the number of items sold in each category
print(cat_revenue)
subcat_revenue = df.groupby('Sub-Category').agg(subcat_revenue=('Sales', 'sum'), items=('Sales', 'count')).sort_values('subcat_revenue', ascending=False).head(10) # calculating total revenue for each sub-category and the number of items sold in each sub-category with the top 10 sub-categories by revenue
print(subcat_revenue)
#***********************
daily_revenue = df.groupby('Daily_Date').agg(daily_revenue=('Sales', 'sum'), items=('Sales', 'count')).reset_index() # calculating total revenue for each day and the number of items sold in each day
daily_revenue=daily_revenue.sort_values('Daily_Date')
print(daily_revenue)
monthly_revenue = df.groupby('Order_Month').agg(monthly_revenue=('Sales', 'sum'), items=('Sales', 'count')).reset_index() # calculating total revenue for each month and the number of items sold in each month
monthly_revenue=monthly_revenue.sort_values('Order_Month')
print(monthly_revenue)
yearly_revenue = df.groupby('Order_Year').agg(yearly_revenue=('Sales', 'sum'), items=('Sales', 'count')).reset_index() # calculating total revenue for each year and the number of items sold in each year
yearly_revenue=yearly_revenue.sort_values('Order_Year')
print(yearly_revenue)
# =========================
# Visualization
# =========================
plt.figure(figsize=(5,5))
#Category revenue bar chart
plt.bar(
    cat_revenue.index,
    cat_revenue['cat_revenue'],
    color='skyblue'
)
plt.title('Total Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#Sub-Category revenue bar chart
plt.figure(figsize=(5,5))
plt.pie(
    subcat_revenue['subcat_revenue'],
    labels=subcat_revenue.index,
    autopct='%1.1f%%',
    startangle=90
)
plt.title('Revenue Distribution by Sub-Category (Top 10)')
plt.tight_layout()
plt.show()
#Monthly revenue line chart
plt.figure(figsize=(10,5))
plt.plot(
    monthly_revenue['Order_Month'],
    monthly_revenue['monthly_revenue'],
    color='green',
    marker='o',
)
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(monthly_revenue['Order_Month'][::3], rotation=45) # showing every 3rd month on x-axis for better readability
plt.tight_layout()
plt.show()
#Yearly revenue line chart
plt.figure(figsize=(10,5))
plt.plot(
    yearly_revenue['Order_Year'],
    yearly_revenue['yearly_revenue'],
    color='blue',
    marker='o',
)
plt.title('Yearly Revenue Trend')
plt.xlabel('Year')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
