import pandas as pd
import numpy as np
import os

"""
This code reads all CSV files from the raw data folder, combines them into one DataFrame, adds a month_year column based on each filename, 
and filters the data to Christchurch City, along with the required statistical summaries. The final combined Christchurch City dataset is saved as a CSV file in the processed data folder.

Inputs:
    1. CSV files stored in the data/raw folder.

Outputs:
    1. A combined Christchurch City dataset saved as data/processed/christchurch_data.csv.
    2. Statistical summaries printed to the console, including:
        1. number of rows and columns
        2. data types
        3. categorical value counts
        4. numerical summary statistics
        5. monthly numerical summary statistics
        6. missing value counts

Parameters:
    1. Raw data folder: data/raw
    2. Output file: data/processed/christchurch_data.csv
    3. Categorical columns: room_type, neighbourhood, month_year
    4. Numerical columns: price, minimum_nights, number_of_reviews, reviews_per_month, calculated_host_listings_count, availability_365, number_of_reviews_ltm
    5. Monthly numerical columns: price, number_of_reviews, calculated_host_listings_count, number_of_reviews_ltm
    6. Christchurch City filter: neighbourhood_group == "Christchurch City"
    7. Month-year extraction: from filename, first two parts separated by underscore, title-cased
    8. Missing value summary: count of missing values for each column
"""

"""
 FILTER CHRISTCHURCH CITY DATA
"""

folder_path = "data/raw"        # Change the working directory in folder_path if required.
output_file_path = "data/processed/christchurch_data.csv"

def combine_raw_data(folder_path):
    dataframes = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        csv_data = pd.read_csv(file_path)
        month_year = " ".join(file.split("_")[:2]).title()
        csv_data["month_year"] = month_year
        dataframes.append(csv_data)
    combined_result = pd.concat(dataframes, ignore_index=True)
    return combined_result


def filter_christchurch_data(combined_result):
    christchurch_data = combined_result[combined_result["neighbourhood_group"] == "Christchurch City"]
    return christchurch_data

def save_to_csv(christchurch_data, output_file_path):
    christchurch_data.to_csv(output_file_path, index=False)
    print(f"Christchurch City data saved to {output_file_path}")
    print("Number of rows:", christchurch_data.shape[0])
    print("Number of columns:", christchurch_data.shape[1])
    print("\nData types:")
    print(christchurch_data.dtypes)




"""
CATEGORICAL SUMMARY
"""

categorical_columns = [
    "room_type",
    "neighbourhood",
    "room_type",
    "month_year"
]

def categorical_summary(christchurch_data, categorical_columns):
    for column in categorical_columns:
        print("\n", column)
        print(christchurch_data[column].value_counts())
    


"""
NUMERICAL SUMMARY
"""

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

def numerical_summary(christchurch_data, total_numerical_columns, numerical_columns):
    numerical_summary = christchurch_data[total_numerical_columns].describe().loc[
    ["min", "max", "mean", "std"]]
    monthly_summary = christchurch_data.groupby("month_year")[numerical_columns].agg(
    ["min", "max", "mean", "std"])
    print(f"Total Numerical summary:\n{numerical_summary}")
    print(f"Monthly Numerical summary:\n{monthly_summary}")


"""
MISSING VALUES SUMMARY
"""
def missing_values_summary(christchurch_data):
    missing_summary = pd.DataFrame({"missing_count": christchurch_data.isna().sum()})
    print(f"Missing values summary:\n{missing_summary}")


combined_raw_data = combine_raw_data(folder_path)
christchurch_data = filter_christchurch_data(combined_raw_data)
save_to_csv(christchurch_data, output_file_path)
categorical_summary(christchurch_data, categorical_columns)
numerical_summary(christchurch_data, total_numerical_columns, numerical_columns)
missing_values_summary(christchurch_data)
