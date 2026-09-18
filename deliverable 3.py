import pandas as pd
import glob
import matplotlib.pyplot as plt

# Find all 9 CSV files
files = glob.glob(
    r"C:\Users\daole\Downloads\listing\*.csv"
)

print("Number of files:", len(files))

for file in files:
    print(file)


# Read and filter Christchurch from all 9 datasets
christchurch_data = []

for file in files:
    df = pd.read_csv(file)

    # Filter Christchurch
    df_christchurch = df[
        df["neighbourhood_group"].astype(str).str.contains(
            "Christchurch",
            case=False,
            na=False
        )
    ].copy()

    # Convert last_review to datetime
    df_christchurch["last_review"] = pd.to_datetime(
        df_christchurch["last_review"],
        errors="coerce"
    )

    # Find the most recent review date for this month
    scrape_date = df_christchurch["last_review"].max()

    print("Scrape date:", scrape_date)

    # Calculate days since last review
    df_christchurch["days_since_last_review"] = (
        scrape_date - df_christchurch["last_review"]
    ).dt.days

    # Add this month's Christchurch data
    christchurch_data.append(df_christchurch)


# Combine all Christchurch data
combined = pd.concat(
    christchurch_data,
    ignore_index=True
)

print(
    "Number of Christchurch listings:",
    len(combined)
)


# Display the results
print(
    combined[
        [
            "last_review",
            "days_since_last_review"
        ]
    ].head(10)
)


# Plot distribution
plt.hist(
    combined["days_since_last_review"].dropna(),
    bins=30
)

plt.xlabel("Days Since Last Review")
plt.ylabel("Number of Listings")
plt.title(
    "Distribution of Days Since Last Review - Christchurch"
)

plt.show()