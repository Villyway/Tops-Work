''' Question S1:
  Explain why NumPy vectorisation is a technically superior approach to the for-loop suggestion. In your answer,
  describe what broadcasting allows when a single scalar fee rate (e.g., Rs 5 per km) is applied to the entire array, and 
  identify one scenario where a Python loop would still be necessary despite NumPy being available.'''

# ANSWER:
# NumPy vectorisation is technically superior to a Python for-loop because it performs operations on the entire array at once
#  rather than executing one element at a time in Python. This significantly reduces execution time.
#  It also results in shorter, cleaner, and more readable code.

# For example, if the delivery fee is Rs 5 per km and the distances are stored in a NumPy array called distances, the fee for
#  every order can be calculated in one statement:
# fees = distances * 5

# This works because of broadcasting. Broadcasting automatically expands the scalar value (5) to match the shape of the array
#  during the calculation. Instead of manually multiplying each distance inside a loop, NumPy conceptually treats the scalar as
#  if it were an array of the same size and performs the multiplication element-wise.

# A Python loop may still be necessary when the operation cannot be expressed as a vectorized array operation. For example,
#  if each order requires different decision-making, such as checking multiple conditions a loop is more appropriate because these
#  tasks cannot be efficiently vectorized.


# ---------------------------------------------------------------------------------------------------------------------------------------
''' Question S2:
  Explain why groupby() combined with agg() is the correct approach instead of the for-loop strategy. Describe the specific method
  chain you would write to compute average order value, average delivery time, and average rating per restaurant in a single
  operation, and explain what the resulting DataFrame's index represents after the operation.'''

# ANSWER:
# Using groupby() with agg() is the correct approach because it is more efficient, and designed for grouped data analysis
#  A for-loop would repeatedly filter the DataFrame for each restaurant, requiring multiple passes over the data and manual 
# calculations. This approach is slower, more error-prone, and harder to maintain, especially for large datasets. In contrast,
# groupby() groups all rows belonging to the same restaurant in a single pass, and agg() computes multiple summary statistics.

# The required method chain is:
# result = df.groupby("restaurant_name").agg({
#     "order_value": "mean",
#     "delivery_time_mins": "mean",
#     "rating": "mean"
# })

# This single operation computes:
# Average order value for each restaurant.
# Average delivery time for each restaurant.
# Average customer rating for each restaurant.

# The resulting DataFrame will have restaurant_name as its index. This means each row represents one unique restaurant, while the
# columns contain the calculated average values for order_value, delivery_time_mins, and rating.


# ---------------------------------------------------------------------------------------------------------------------------------------
''' Question S3:
 Identify the most appropriate Matplotlib chart type for each of the three metrics and justify each choice based on the
  nature of the data. Then explain how plt.subplots() would be configured to arrange all three charts in a single figure, and
  state whether a shared x-axis would or would not be appropriate for this layout — and why.'''

# ANSWER:
# Total orders placed per month (January–December): Line Chart
# A line chart is the best choice because the data is ordered over time. It clearly shows trends, increases, decreases, and 
# seasonal patterns in monthly orders. A bar chart could also display monthly totals, but a line chart is better for emphasizing
# changes over time.

# Proportion of orders by cuisine type (Fast Food, Indian, Chinese, Desserts): Pie Chart
# A pie chart is appropriate because it shows how each cuisine contributes to the total number of orders. Since the categories
# represent parts of a whole, the pie chart makes it easy to compare their relative proportions.

# Distribution of delivery times across all orders: Histogram
# A histogram is the correct choice because delivery time is continuous numerical data. It groups delivery times into intervals
# (bins) and shows how frequently orders fall within each range, helping identify the overall distribution, spread, and any
# skewness.

# To display all three charts in one figure, plt.subplots() can be configured with 1 row and 3 columns:
# fig, axes = plt.subplots(1, 3, figsize=(18, 5))
# 1 row places all charts side by side.
# 3 columns provide one subplot for each visualization.
# figsize=(18, 5) gives enough space so each chart is readable.

# A shared x-axis (sharex=True) is not appropriate for this layout because the three plots use completely different x-axis data:
# The line chart uses months.
# The pie chart does not have an x-axis.
# The histogram uses delivery time intervals (minutes).
# Since the x-axes represent different types of information, sharing them would be meaningless and could produce confusing or 
# incorrect visualizations. Therefore, each subplot should have its own independent axis.


# ---------------------------------------------------------------------------------------------------------------------------------------
''' Question S4:
 Describe how you would use plt.annotate() to programmatically identify and mark the maximum order day with an arrow pointing to the peak 
 and a text label showing the day number and volume. Name at least two specific parameters you would pass to plt.annotate() and explain what 
 each one controls in the rendered chart'''

# ANSWER:
#  first calculate the maximum order day (max_day) and its corresponding volume (max_volume). Then, call plt.annotate() with parameters that 
# control the annotation:
# plt.annotate(
#     text=f"Day {max_day}\nVolume: {max_volume}",
#     xy=(max_day, max_volume),                         # point to annotate
#     xytext=(max_day+1, max_volume+50),                # text position offset
#     arrowprops=dict(facecolor='black', shrink=0.05)
# )

# Two Specific Parameters are :
# 1) xy = This parameter specifies the exact data point we want to annotate.
# 2) xytext = This parameter defines the position of the text label relative to the annotated point.


# ---------------------------------------------------------------------------------------------------------------------------------------
''' QUESTION S5:
 Compare sns.boxplot() and sns.violinplot() for this specific task. Which would you recommend and why? Provide at least two
  data-specific reasons that reference properties of this dataset (10,000 rows, 3 categories, discrete 1–5 scale), and explain
  one situation where the other chart type would be preferable.'''

# Answer:
# For this dataset, I would recommend sns.boxplot() because the ratings are on a discrete 1–5 scale and there are only 3
#  restaurant categories.
# Boxplot is easier to compare the three categories because it clearly shows the median, spread, and possible outliers for Fast Food, Fine Dining, and Casual.
# Since the dataset has 10,000 rows, a boxplot gives a simple summary without making the graph too crowded.
# Because ratings only range from 1 to 5, a violin plot's smooth distribution shape may be less meaningful for this discrete data.

# A sns.violinplot() would be preferable if the ratings were continuous values or had many possible values. It would show the shape and density 
# of the distribution more clearly, helping us see whether ratings are concentrated around certain values or have multiple peaks.


# ---------------------------------------------------------------------------------------------------------------------------------------
''' Question S6:
 Explain how you would generate and interpret a Seaborn correlation heatmap to identify multicollinearity risks among these 
 features. In your answer, describe what the colour scale in the heatmap represents, how to read a specific cell value, and what
  correlation magnitude threshold you would use to flag a potential multicollinearity problem — and why that threshold is 
 conventionally chosen.'''

# ANSWER:
# I would use a Seaborn correlation heatmap to check how strongly the eight numeric features are related to each other before
# training the regression model.

# import seaborn as sns
# import matplotlib.pyplot as plt
# corr = df.corr()
# sns.heatmap(corr, annot=True, cmap="coolwarm")
# plt.show()

# Interpretation:
# The colour scale represents the strength and direction of correlation. Values close to +1 show a strong positive relationship, 
# values close to -1 show a strong negative relationship, and values near 0 show little or no linear relationship.
# A specific cell shows the correlation between two features. For example, if distance_km and delivery_time_mins have a value of
#  0.85, it means they have a strong positive relationship: as distance increases, delivery time tends to increase.
# I would generally flag a correlation of |r| ≥ 0.8 as a potential multicollinearity problem. This threshold is commonly used 
# because a correlation this strong indicates that two features contain very similar information, which can make regression 
# coefficients unstable and difficult to interpret.


# ---------------------------------------------------------------------------------------------------------------------------------------