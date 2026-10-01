import pandas as pd
import numpy as np
import os


# read all the list of csv files from raw folder and concatenate them into a single dataframe with an additional column for month and year

dataframes = []
folder_path = "data/raw"


for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    csv_data = pd.read_csv(file_path)
    month_year = " ".join(file.split("_")[:2]).title()
    csv_data["month_year"] = month_year
    dataframes.append(csv_data)

combined_result = pd.concat(dataframes, ignore_index=True)


# filter based on christchurch city ans save the result in a new csv file

christchurch_data = combined_result[combined_result["neighbourhood_group"] == "Christchurch City"]
christchurch_data.to_csv("data/processed/christchurch_data.csv", index=False)

# statistical summary  (categories + counts or min + max + mean + std) and number of missing values (per column))

# Basic information

print("Number of rows:", christchurch_data.shape[0])
print("Number of columns:", christchurch_data.shape[1])

print("\nData types:")
print(christchurch_data.dtypes)

# Categorical summary

categorical_columns = [
    "room_type",
    "neighbourhood",
    "room_type",
    "month_year"
]

for column in categorical_columns:
    print("\n", column)
    print(christchurch_data[column].value_counts())


# Numerical summary

total_numerical_columns = [
    "price",
    "minimum_nights",
    "number_of_reviews",
    "reviews_per_month",
    "calculated_host_listings_count",
    "availability_365",
    "number_of_reviews_ltm"
]

numerical_columns = [
    "price",
    "number_of_reviews",
    "calculated_host_listings_count",
    "number_of_reviews_ltm"
]

numerical_summary = christchurch_data[total_numerical_columns].describe().loc[
    ["min", "max", "mean", "std"]
]

monthly_summary = christchurch_data.groupby("month_year")[numerical_columns].agg(
    ["min", "max", "mean", "std"]
)

print(f"Total Numerical summary:\n{numerical_summary}")
print(f"Monthly Numerical summary:\n{monthly_summary}")


# Missing values

missing_summary = pd.DataFrame({
    "missing_count": christchurch_data.isna().sum()
})

print(f"Missing values summary:\n{missing_summary}")
