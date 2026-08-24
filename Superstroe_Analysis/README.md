# Superstore Data Analysis 📊

## 📌 Project Overview

This project focuses on cleaning, preprocessing, and analyzing the **Superstore dataset** using Python.

The main goal is to transform raw and inconsistent data into a clean and analysis-ready dataset that can be used for further data analysis and visualization.

The project was developed using **Pandas, NumPy, and Matplotlib**.

---

## 📂 Dataset

The dataset used in this project is the **Superstore Dataset**, obtained from **Kaggle**.

The dataset contains information about:

* Customers
* Orders
* Products
* Categories
* Sales
* Regions
* Shipping
* Dates

**Source:** Kaggle – Superstore Dataset

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation and cleaning
* **NumPy** – Numerical operations
* **Matplotlib** – Data visualization
* **OpenPyXL** – Reading Excel files

---

## 🧹 Data Cleaning

The project includes several data-cleaning steps:

### 1. Initial Data Inspection

The dataset was inspected using:

* Missing values
* Duplicate rows
* Dataset shape
* Data types
* Number of unique values

### 2. Column Name Cleaning

Column names were cleaned by:

* Removing leading and trailing spaces
* Replacing spaces with underscores

Example:

```text
Product ID → Product_ID
Order Date → Order_Date
```

### 3. Text Cleaning

Text columns were cleaned by:

* Removing unnecessary spaces
* Replacing string `"nan"` values with actual `NaN`
* Standardizing text using title case

### 4. Data Type Conversion

Several columns were converted to appropriate data types:

* `Order_Date` → Datetime
* `Row_ID` → Integer
* `Postal_Code` → Integer
* `Sales` → Numeric

### 5. Missing Sales Values

Missing values in the `Sales` column were handled using a two-step approach:

1. Fill missing sales using the **median sales of the same product**.
2. Remaining missing values were filled using the **overall median of the Sales column**.

This approach helps preserve the relationship between products and their typical sales values.

---

## ⚙️ Feature Engineering

New columns were created from the `Order_Date` column:

* `Order_Year` – Extracted year
* `Order_Month` – Extracted month and year
* `Daily_Date` – Extracted date

These features make time-based analysis easier.

---

## 📊 Analysis

After cleaning the dataset, the processed data can be used to perform different types of analysis, including:

* Sales by Category
* Sales by Sub-Category
* Monthly Sales
* Yearly Sales
* Daily Sales
* Product-level analysis
* Customer analysis
* Regional analysis

---

### `main.py`

Contains the data loading, cleaning, preprocessing, and feature engineering functions.

### `visualization.py`

Contains the visualization and analysis code based on the cleaned dataset.

### `README.md`

Provides documentation about the project.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Install the required libraries

```bash
pip install pandas numpy matplotlib openpyxl
```

### 3. Run the project

```bash
python visualization.py
```

Make sure the dataset file is available in the expected location.

---

## 🎯 Project Objective

The objective of this project is to practice real-world data preprocessing and analysis techniques using Python.

It demonstrates how raw data can be:

**Loaded → Inspected → Cleaned → Transformed → Analyzed → Visualized**

---

## 👨‍💻 Author

**Mohamed Gabal**

AI Student | Aspiring AI 

---

## ⭐ Future Improvements

Possible future improvements include:

* Adding more statistical analysis
* Creating more advanced visualizations
* Performing customer segmentation
* Adding sales forecasting
* Building an interactive dashboard
* Applying machine learning techniques
