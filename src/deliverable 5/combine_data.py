import pandas as pd


"""
This code joins Christchurch Airbnb data with quarterly tenancy data using area code and month.

Inputs:
    1. Christchurch Airbnb data from data/processed/christchurch_air_bnb_appended.csv
    2. Detailed quarterly tenancy data from data/processed/Detailed-Quarterly-Tenancy.csv

Outputs:
    1. A joined dataset saved as
      data/processed/christchurch_airbnb_tenancy_joined.csv
    2. The median Airbnb price for Christchurch Central printed to the console.
    3. Information about the number of rows successfully matched with tenancy data.

Parameters:
    1. Airbnb data: data/processed/christchurch_air_bnb_appended.csv
    2. Tenancy data: data/processed/Detailed-Quarterly-Tenancy.csv
    3. Output file: data/processed/christchurch_airbnb_tenancy_joined.csv
    4. Christchurch Central area code: 326600
"""
# change the file paths if required
airbnb_file_path="data/processed/christchurch_air_bnb_code_name_appended.csv"
tenancy_file_path="data/processed/Detailed-Quarterly-Tenancy.csv"
output_file_path="data/processed/christchurch_airbnb_tenancy_joined.csv"

"""
Reads the Airbnb and tenancy CSV files and returns them as DataFrames.
"""
def read_csv_file(airbnb_file_path, tenancy_file_path):
    tenancy_data = pd.read_csv(tenancy_file_path)
    christchurch_data = pd.read_csv(airbnb_file_path)
    return christchurch_data, tenancy_data


""" 
CONVERT DATES TO MONTHLY PERIODS 
"""

def convert_to_monthly_period(christchurch_data, tenancy_data):
    christchurch_data['month'] = pd.to_datetime(
        christchurch_data['month_year'],
        format='mixed'
    ).dt.to_period('M')

    tenancy_data['month'] = pd.to_datetime(
        tenancy_data['TimeFrame']
    ).dt.to_period('M')



"""
JOIN AIRBNB DATA WITH TENANCY DATA
"""
def join_airbnb_with_tenancy(christchurch_data, tenancy_data):
    merged_data = christchurch_data.merge(
        tenancy_data,
        left_on=['sa22026_code', 'month'],
        right_on=['Location Id', 'month'],
        how='left'
    )
    return merged_data




"""
SAVE MERGED DATASET
"""
def save_data_to_csv(data, output_file_path):
    data.to_csv(
        output_file_path,
        index=False
    )


"""
CALCULATE MEDIAN AIRBNB PRICE FOR CHRISTCHURCH CENTRAL
"""
def calculate_median_price(christchurch_data, area_code):
    christchurch_central = christchurch_data[
        christchurch_data['sa22026_code'] == area_code
    ]
    median_price = christchurch_central['price'].median()
    return median_price


christchurch_data, tenancy_data = read_csv_file(airbnb_file_path, tenancy_file_path)
convert_to_monthly_period(christchurch_data, tenancy_data)
merged_data = join_airbnb_with_tenancy(christchurch_data, tenancy_data)
save_data_to_csv(merged_data, output_file_path)
median_price = calculate_median_price(christchurch_data, 326600)
"""
CHECK MERGE RESULTS
"""
print("Airbnb rows before merge:", len(christchurch_data))
print("Rows after merge:", len(merged_data))
print(
    "Rows with rental data:",
    merged_data['Median Rent'].notna().sum()
)
print(
    "Rows without rental data:",
    merged_data['Median Rent'].isna().sum()
)

print("Median Airbnb price in Christchurch Central:", median_price)
