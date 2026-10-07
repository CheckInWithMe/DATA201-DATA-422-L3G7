from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"

file = DATA_DIR / "christchurch_data.csv"

df = pd.read_csv(file)

columns_to_keep = [
    "id",
    "latitude",
    "longitude",
    "neighbourhood",
    "room_type",
    "price",
    "availability_365",
    "month_year",
    "minimum_nights"
]

cleaned_christchurch = df[columns_to_keep].copy()



OUTPUT_DIR = PROJECT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

cleaned_christchurch.to_csv(
    OUTPUT_DIR / "christchurch_airbnb_cleaned.csv",
    index=False
)
