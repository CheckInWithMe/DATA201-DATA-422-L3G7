
import pandas as pd

christchurch = pd.read_csv(
    "data/processed/christchurch_airbnb_cleaned.csv",
    encoding="latin1",
    nrows=5
)

print(christchurch.columns.tolist())
print("Number of columns:", len(christchurch.columns))


christchurch_sa= pd.read_csv("data/processed/christchurch_air_bnb_code_name_appended.csv")

merged_data = christchurch.merge(
    christchurch_sa,
    on="id",
    how="left"
)

print("Rows:", merged_data.shape[0])
print("Columns:", merged_data.shape[1])
print(merged_data.head())