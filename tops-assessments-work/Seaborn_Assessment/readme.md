# Food Delivery Data Analytics & Visualization Assessment

## Overview

This project is a Python-based assessment focused on **data analysis and visualization** using synthetic food delivery datasets. The assessment demonstrates practical use of **NumPy, Pandas, Matplotlib, and Seaborn** through conceptual questions, programming tasks, dashboards, and exploratory data analysis (EDA).

---

## Project Structure

- **Section_A.py** — Conceptual and theoretical questions
- **Section_B.ipynb** — NumPy, Pandas, Matplotlib, and complete EDA tasks
- **Section_C.py** — Menu-driven food delivery analytics program
- **Section_D.ipynb** — Seaborn pairplots, correlation heatmaps, and debugging

---

## Main Topics Covered

### NumPy
- Vectorized calculations and broadcasting
- Delivery fee calculation
- Boolean indexing
- Minimum, maximum, mean, and standard deviation

### Pandas
- Creating and managing DataFrames
- Missing value handling
- `groupby()` and `agg()` operations
- Filtering and sorting restaurant performance
- Feature engineering and categorization using `pd.qcut()`

### Matplotlib
- Monthly order trend line chart
- Revenue bar chart with performance threshold
- Delivery time histogram
- Subplots and data annotations

### Seaborn
- Pairplots for comparing numerical variables
- Pearson correlation heatmaps
- Visualization using categories such as `speed_band` and `Cuisine_Type`

---

## EDA Workflow

The project includes an end-to-end exploratory data analysis pipeline:

1. Generate synthetic food delivery data using NumPy.
2. Load the data into Pandas DataFrames.
3. Introduce and handle missing values using median or mean values.
4. Create derived features such as delivery speed.
5. Categorize delivery records into **Slow, Normal, and Fast** groups.
6. Analyse relationships between numerical variables using correlation.
7. Create pairplots and heatmaps to visualize the dataset.

---

## Visualizations Included

The assessment produces several visual outputs, including:

- Food Delivery Monthly Performance Dashboard
- Monthly Total Orders trend
- Monthly Revenue comparison
- Delivery Time Distribution
- Correlation Heatmaps
- Pairplots colored by delivery speed
- Pairplots colored by cuisine type
- Restaurant performance charts

---

## Section C Analytics Features

The menu-driven analytics program provides options for:

- Summary statistics
- Distribution analysis
- Correlation heatmap
- Restaurant performance report
- Final EDA summary

It combines NumPy, Pandas, Matplotlib, and Seaborn into a single interactive analysis workflow.

---

## Libraries Used

```bash
pip install numpy pandas matplotlib seaborn jupyter
```

---

## How to Run

### Python Files

```bash
python Section_A.py
python Section_C.py
```

### Jupyter Notebooks

```bash
jupyter notebook
```

Then open and run:

- `Section_B.ipynb`
- `Section_D.ipynb`

---

## Learning Outcomes

This assessment demonstrates understanding of:

- Numerical computing with NumPy
- Data manipulation with Pandas
- Data cleaning and missing value treatment
- Grouped data analysis
- Statistical visualization
- Correlation analysis
- Feature engineering
- Exploratory Data Analysis (EDA)
- Debugging basic visualization issues

---

## Conclusion

The **Food Delivery Data Analytics & Visualization Assessment** demonstrates a complete workflow from **synthetic data generation and cleaning** to **data analysis, visualization, and EDA**. The project applies the core concepts of NumPy, Pandas, Matplotlib, and Seaborn to analyse food delivery data and present the results through meaningful visualizations.
