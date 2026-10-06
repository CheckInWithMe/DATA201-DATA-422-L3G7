import pandas as pd
import os

# create class so that i can use it in different files
# Read files
def read_csv_file(file_path):
    data = pd.read_csv(file_path)
    return data

# write files
def save_to_csv(file_data, output_file_path):
    file_data.to_csv(output_file_path, index=False)
    print(f"{file_data.shape[0]} rows saved to {output_file_path}")

# Join files based on any variables

# joinmultiple files
def combine_multiple_files(folder_path):
    dataframes = []
    for file in os.listdir(folder_path):
        if not file.endswith("_listings.csv"): continue
        csv_data = read_csv_file(os.path.join(folder_path, file))
        month_year = " ".join(file.split("_")[:2]).title()
        csv_data["month_year"] = month_year
        dataframes.append(csv_data)
    print("Number of CSV files read:", len(dataframes))
    combined_result = pd.concat(dataframes, ignore_index=True)
    return combined_result

# add rows to csv

# remove rows of csv
def remove_rows(data, column_name, filter_value):
    print("Number of rows before removing:", data.shape[0])
    filtered_data = data[data[column_name] != filter_value]
    print(f"Number of rows after removing:{filtered_data.shape[0]}\nNumber of columns: {filtered_data.shape[1]}")
    return filtered_data

# filter rows of csv
def filter_christchurch_data(data, column_name, filter_value):
    print("Number of rows before filtering:", data.shape[0])
    filtered_data = data[data[column_name] == filter_value]
    print(f"Number of rows:{filtered_data.shape[0]}\nNumber of columns: {filtered_data.shape[1]}")
    return filtered_data
