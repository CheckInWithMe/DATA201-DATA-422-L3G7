from pathlib import Path
import pandas as pd

"""PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

file = DATA_DIR / "christchurch_data.csv"

df = pd.read_csv(file)"""




def clean_data(christchurch_data, columns_to_keep, output):
    copied_christchurch_data = christchurch_data.copy()
    cleaned_christchurch = copied_christchurch_data[columns_to_keep].copy()
    cleaned_christchurch.to_csv(output,index=False)
    return cleaned_christchurch