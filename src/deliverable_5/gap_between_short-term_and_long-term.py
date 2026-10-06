from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data/processed/"

file = DATA_DIR / "christchurch_airbnb_tenancy_joined.csv"

df = pd.read_csv(file)

print("Number of listings:", len(df))

df=df.dropna(subset=[
    'sa22026_name',
    'minimum_nights',
    'price'])

df['rental_type'] = df['minimum_nights'].apply(
    lambda x: 'Short-term' if x<30
    else ('Long-term' if x>30 else None)
    )

df = df.dropna(subset=['rental_type'])

price_comparison = df.groupby(
    ['sa22026_name', 'rental_type']
)['price'].median().unstack()

price_comparison = price_comparison.dropna(
    subset=['Short-term', 'Long-term'])

price_comparison['price_gap']=(
    price_comparison['Short-term'] - price_comparison['Long-term'])

price_comparison['absolute_gap'] = (price_comparison['price_gap'].abs())

price_comparison = price_comparison.sort_values('absolute_gap', ascending = False)

print(price_comparison)

largest_gap = price_comparison.iloc[0]

print('Area with the largest price gap:')
print(price_comparison.index[0])
print('Short-term median:', largest_gap['Short-term'])
print('Long-term median:', largest_gap['Long-term'])
print('Price gap:', largest_gap['price_gap'])

#the largest 15 areas

top_15 = price_comparison.head(15)

top_15[['Short-term', 'Long-term']].plot( kind='bar', figsize=(14,6))

plt.title('Short-term vs Long-term Airbnb Prices by SA2 Area')
plt.xlabel('SA2 Area')
plt.ylabel('Median price per night(NZD)')
plt.xticks(rotation = 60, ha='right')
plt.legend(title='Rental type')
plt.tight_layout
plt.show()
