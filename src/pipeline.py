from deliverable_3 import processing, last_review_fixed, filter_chch_top_ten_review, airbnb_christchurch_prices
from deliverable_4 import clean_christchurch_data, tenancy_data_cleaning
#from deliverable_5 import append_sa22026_code_name
from deliverable_5 import combine_data, comparison_by_region, gap_between_shortterm_and_longterm
import pandas as pd

#Seggregate christchurch data from the combined raw data and save it to a csv file
combined_raw_data = processing.combine_raw_data("data/raw") # Change the working directory in folder_path if required.
christchurch_data = processing.filter_christchurch_data(combined_raw_data, "data/processed/christchurch_data.csv")

#Airbnb data analysis
categorical_columns = ["room_type", "neighbourhood", "room_type", "month_year"]
processing.categorical_summary(christchurch_data, categorical_columns)

total_numerical_columns = ["price", "minimum_nights", "number_of_reviews", "reviews_per_month", "calculated_host_listings_count", "availability_365", "number_of_reviews_ltm"]

numerical_columns = ["price", "number_of_reviews", "calculated_host_listings_count", "number_of_reviews_ltm"]

processing.numerical_summary(christchurch_data, total_numerical_columns, numerical_columns)
processing.missing_values_summary(christchurch_data)

df_last_review = last_review_fixed.get_days_since_last_review(christchurch_data)
last_review_fixed.plot_distribution(df_last_review, "./data/processed/days_since_last_review_histogram.png") # Save output histogram as png

clean_airbnb = airbnb_christchurch_prices.clean_data(christchurch_data)
airbnb_christchurch_prices.display_data(clean_airbnb, "./data/processed/airbnb_frequencies.png")

filter_chch_top_ten_review.filter_to_ten_percent(christchurch_data,"./data/processed/christchurch_top_ten_filtered.csv")


#clean airbnb data
airbnb_columns_to_keep = ["id", "latitude", "longitude", "neighbourhood", "room_type", "price", "availability_365", "month_year", "minimum_nights"]
cleaned_christchurch_data = clean_christchurch_data.clean_data(christchurch_data, airbnb_columns_to_keep, "./data/processed/christchurch_airbnb_cleaned.csv")

#clean tenancy data
tenancy_columns_to_keep = ['TimeFrame', 'Location Id', 'Dwelling Type','Number Of Beds', 'Median Rent', 'Total Bonds']
tenancy_data = tenancy_data_cleaning.clean_data('data/raw/Detailed-Quarterly-Tenancy-Q1-2020-Q3-2026.csv', tenancy_columns_to_keep, 'data/processed/Detailed-Quarterly-Tenancy.csv')

#api for sa code
#append_sa22026_code_name.main()

#join both
christchurch_data_with_codes = pd.read_csv("data/processed/test_sa22026.csv")
merged_data = combine_data.join_airbnb_with_tenancy(christchurch_data_with_codes, tenancy_data, "data/processed/christchurch_airbnb_tenancy_joined.csv")
median_price = combine_data.calculate_median_price(christchurch_data_with_codes, 326600)
combine_data.display_results(christchurch_data_with_codes, merged_data, median_price)

comparison_by_region.master()

gap_between_shortterm_and_longterm.main()
