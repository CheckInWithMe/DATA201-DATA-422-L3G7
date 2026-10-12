import pandas as pd
import matplotlib.pyplot as plt
import os

#os.chdir("") # Set working directory

def get_days_since_last_review(christchurch_data):
    '''create a dataframe with days_since_last_review column for each entry in input data'''
    df_christchurch = christchurch_data.copy()
    # Convert last_review to datetime
    df_christchurch["last_review"] = pd.to_datetime(
        df_christchurch["last_review"],
        errors="coerce"
    )

    # Find the most recent review date for this month
    scrape_date = df_christchurch["last_review"].max()

    # Calculate days since last review
    df_christchurch["days_since_last_review"] = (
        scrape_date - df_christchurch["last_review"]
    ).dt.days

    # Get the number of missing values before dropping the rows with null values in "days_since_last_review" column
    missing_values = df_christchurch["days_since_last_review"].isna().sum()
    df_last_review = df_christchurch["days_since_last_review"]

    # Summary of scraped date and missing values
    print("Most recent review date:", scrape_date)
    print(f"Number of rows missing values in days_since_last_review colunm: {missing_values}")

    return df_last_review


def plot_distribution(df, output):
    '''Plot a histogram of distribution of days since last review'''

    plt.hist(
        df,
        bins=30
    )
    plt.xlabel("Days Since Last Review")
    plt.ylabel("Number of Listings")
    plt.title(
        "Distribution of Days Since Last Review - Christchurch"
    )

    plt.savefig(output)
    plt.show()

# Main program
"""df_last_review = get_days_since_last_review(INPUT)
plot_distribution(df_last_review, OUTPUT)"""