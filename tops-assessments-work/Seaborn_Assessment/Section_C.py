''' MINI PROJECT
Food Delivery Analytics Console - Full EDA Report '''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


''' Generate Synthetic Dataset (200+ rows) '''
np.random.seed(42)
n = 250

restaurants = [
    "Pizza Hub",
    "Burger Point",
    "Biryani House",
    "Chinese Corner",
    "Taco Tacko",
    "Food Mahal",
    "Spice Villa",
    "Healthy Bowl"
]

cities = [
    "Delhi",
    "Mumbai",
    "Bangalore",
    "Pune",
    "Ahmedabad"
]

df = pd.DataFrame({

    "Restaurant": np.random.choice(restaurants, n),

    "City": np.random.choice(cities, n),

    "Order_Value": np.random.randint(150, 1200, n),

    "Delivery_Time": np.random.randint(15, 70, n),

    "Rating": np.round(np.random.uniform(2.5, 5.0, n), 1),

    "Distance_km": np.round(np.random.uniform(1, 12, n), 2),

    "Delivery_Fee": np.random.randint(20, 120, n)

})

# ============================================================
# Introduce Missing Values
# ============================================================

for col in ["Order_Value", "Delivery_Time",
            "Rating", "Distance_km", "Delivery_Fee"]:

    index = np.random.choice(df.index, 6, replace=False)
    df.loc[index, col] = np.nan


# ============================================================
# Fill Missing Numeric Values BEFORE Analysis
# ============================================================

numeric_cols = df.select_dtypes(include=np.number).columns

df[numeric_cols] = df[numeric_cols].fillna(
    df[numeric_cols].mean()
)

print("\nMissing Values Filled Successfully!\n")


# ============================================================
# OPTION 1
# Summary Statistics (NumPy)
# ============================================================

def summary_statistics():

    print("\n========== SUMMARY STATISTICS ==========\n")

    delivery = df["Delivery_Time"].to_numpy()
    order = df["Order_Value"].to_numpy()

    print("Mean Delivery Time :", np.mean(delivery))
    print("Median Delivery Time :", np.median(delivery))
    print("Std Delivery Time :", np.std(delivery))

    print()

    print("Average Order Value :", np.mean(order))
    print("Maximum Order Value :", np.max(order))
    print("Minimum Order Value :", np.min(order))


# ============================================================
# OPTION 2
# Distribution Analysis (Matplotlib)
# ============================================================

def distribution_analysis():

    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    ax[0].hist(df["Delivery_Time"],
               bins=15)

    ax[0].set_title("Delivery Time Distribution")
    ax[0].set_xlabel("Minutes")
    ax[0].set_ylabel("Frequency")

    ax[1].hist(df["Order_Value"],
               bins=15)

    ax[1].set_title("Order Value Distribution")
    ax[1].set_xlabel("Order Value")
    ax[1].set_ylabel("Frequency")

    plt.tight_layout()

    plt.savefig(
        "distribution_analysis.png",
        dpi=150
    )

    plt.close()

    print("Chart saved as distribution_analysis.png")


# ============================================================
# OPTION 3
# Correlation Heatmap (Seaborn)
# ============================================================

def correlation_heatmap():

    plt.figure(figsize=(8, 6))

    corr = df[numeric_cols].corr()

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig(
        "correlation_heatmap.png",
        dpi=150
    )

    plt.close()

    print("Chart saved as correlation_heatmap.png")


# ============================================================
# OPTION 4
# Restaurant Performance Report (Pandas GroupBy)
# ============================================================

def restaurant_report():

    report = df.groupby("Restaurant").agg({

        "Rating": "mean",
        "Order_Value": "mean",
        "Delivery_Time": "mean"

    }).round(2)

    print("\n========== RESTAURANT REPORT ==========\n")
    print(report)

    report["Rating"].sort_values().plot(
        kind="barh",
        figsize=(8, 5),
        title="Average Restaurant Rating"
    )

    plt.tight_layout()

    plt.savefig(
        "restaurant_rating_report.png",
        dpi=150
    )

    plt.close()

    print("\nChart saved as restaurant_rating_report.png")


# ============================================================
# MENU-DRIVEN Program
# ============================================================

while True:

    print("\n=========== FOOD DELIVERY ANALYTICS ===========")

    print("1. Summary Statistics")
    print("2. Distribution Analysis")
    print("3. Correlation Heatmap")
    print("4. Restaurant Performance Report")
    print("5. Exit the Program")

    choice = input("\nEnter Your Choice From the Menu: ")

    if choice == "1":
        summary_statistics()

    elif choice == "2":
        distribution_analysis()

    elif choice == "3":
        correlation_heatmap()

    elif choice == "4":
        restaurant_report()


# ============================================================
# FINAL REPORT
# ============================================================
    elif choice == "5":
        print("\n")
        print("=" * 55)
        print("FINAL EDA SUMMARY REPORT")
        print("=" * 55)

        # Top 3 Restaurants

        top3 = (
            df.groupby("Restaurant")["Rating"]
            .mean()
            .sort_values(ascending=False)
            .head(3)
        )

        print("\nTop 3 Restaurants by Mean Rating\n")
        print(top3)


        # Highest Pearson Correlation

        corr = df[numeric_cols].corr().abs()

        # Work on a copy so it's writable
        corr_values = corr.values.copy()
        np.fill_diagonal(corr_values, 0)

        # Re-wrap into a DataFrame
        corr_no_diag = pd.DataFrame(corr_values, index=corr.index, columns=corr.columns)

        highest = corr_no_diag.unstack().idxmax()
        print("\nHighest Absolute Pearson Correlation")
        print(f"{highest[0]}  <-->  {highest[1]}")
        print("Correlation :", corr_no_diag.unstack().max())

        # Delivery Statistics

        print("\nDelivery Time Statistics")

        print(
            "Mean :",
            round(df["Delivery_Time"].mean(), 2)
        )

        print(
            "Standard Deviation :",
            round(df["Delivery_Time"].std(), 2)
        )

        print("\nThank You!")
        break

    else:
        print("Invalid Choice!")