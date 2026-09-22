import pandas as pd


# Load datasets
tenancy_data = pd.read_csv(
    "data/processed/Detailed-Quarterly-Tenancy.csv"
)

christchurch_data = pd.read_csv(
    "data/processed/christchurch_air_bnb_appended.csv"
)


# Convert Airbnb month to monthly period
# Handles both full and abbreviated month names
christchurch_data['month'] = pd.to_datetime(
    christchurch_data['month_year'],
    format='mixed'
).dt.to_period('M')


# Convert Tenancy timeframe to monthly period
tenancy_data['month'] = pd.to_datetime(
    tenancy_data['TimeFrame']
).dt.to_period('M')


# Join Airbnb and Tenancy data by area code and month
# Left join keeps all Airbnb observations
merged_data = christchurch_data.merge(
    tenancy_data,
    left_on=['sa22026_code', 'month'],
    right_on=['Location Id', 'month'],
    how='left'
)


# Check merge results
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

# Save joined dataset as Excel file
merged_data.to_csv(
    "data/processed/christchurch_airbnb_tenancy_joined.csv",
    index=False
)

# Calculate median Airbnb price in Christchurch Central
christchurch_central = christchurch_data[
    christchurch_data['sa22026_code'] == 326600
]

median_price = christchurch_central['price'].median()

print("Median Airbnb price in Christchurch Central:", median_price)