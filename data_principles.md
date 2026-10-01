## Data principles

- we tried to divide work 4 equal ways
- If the pipeline required certain steps to be done by one person before allowing others to do work, we tried to group that work for one person
- When there was not enough work we prioritised having equal work

## Deliverable 3
# Sakshi's processing.py
1. Inputs to the pipeline

The pipeline takes multiple raw CSV files containing Airbnb listing data as its input.
Input folder: data/raw/*.csv
Input format: CSV files.
Expected data: Airbnb listing information, including columns such as: neighbourhood_group, neighbourhood, room_type, price, minimum_nights, number_of_reviews, reviews_per_month, calculated_host_listings_count, availability_365, number_of_reviews_ltm
Each input file is expected to have the required columns, and its filename is used to derive a month_year value.

2. Outputs from the pipeline

The pipeline produces a processed dataset and statistical summaries:
- "data/processed/christchurch_data.csv"
A combined dataset containing only Airbnb listings where neighbourhood_group is Christchurch City. Includes a month_year column.
- Basic information
Number of rows, number of columns, and data types of the processed dataset.
- Categorical summaries
Frequency counts for room_type, neighbourhood, and month_year.
Overall numerical summary
- Minimum, maximum, mean, and standard deviation for selected numerical columns.
Monthly numerical summary
- Minimum, maximum, mean, and standard deviation for selected numerical columns, grouped by month_year.
Missing values summary
- Number of missing values in each column of the processed dataset.

Note: The statistical summaries are printed to the console; they are not currently saved to separate files.

3. Main steps in the pipeline
Step 1. Read raw data: read CSV files from data/raw/ using pandas.
Step 2. Add time information: extract the month and year from each filename and add a month_year column.
Step 3. Combine datasets: concatenate the individual DataFrames into one combined DataFrame.
Step 4. Filter and save: keep only Christchurch City listings and save them to data/processed/christchurch_data.csv.
Step 5. Generate statistical summaries: calculate dataset dimensions, data types, categorical frequencies, overall numerical statistics, and monthly numerical statistics.
Step 6. Assess data completeness: count missing values in each column and print the results.
# Dao's

# William's 

# Tram's filter_chch_top_ten_review_py
1. Inputs to the pipeline

The pipeline takes multiple raw Airbnb listing CSV files as input from the ./data/raw/ directory. These files are read using pandas and combined into a single DataFrame.
The input data is expected to contain the following columns: id, name, neighbourhood_group, number_of_reviews

2. Outputs from the pipeline

- "./data/processed/christchurch_top_ten_filtered.csv"
A CSV file intended to contain the top 10% of Airbnb listings in Christchurch City, ranked by number of reviews.
- Total Christchurch listings
The number of Airbnb listings in Christchurch City before applying the top 10% filter, printed to the console.
- Filtered dataset display
The contents of the output CSV file, read back into a DataFrame and printed to the console.

3. Main steps in the pipeline

Step 1. Read raw data: Identify and read all CSV files from ./data/raw/.
Step 2. Combine datasets: Concatenate the individual DataFrames into one combined dataset.
Step 3. Filter Christchurch listings: Keep only rows where neighbourhood_group equals Christchurch City and select the four relevant columns.
Step 4. Count Christchurch listings: Calculate the total number of Christchurch listings before filtering to the top 10%.
Step 5. Rank and filter listings: Sort listings by number_of_reviews in descending order and select the top 10%.
Step 6. Save and display results: Save the filtered listings to a CSV file, print the total Christchurch listing count, and display the saved dataset.

## Deliverable 4
# Dao's deliverable_week8
1. Inputs to the pipeline

The pipeline takes multiple raw Airbnb listing CSV files as input.

Input folder: listing/
Input format: CSV files.
Expected data: Airbnb listing information containing columns such as: id, latitude, longitude, neighbourhood_group, neighbourhood, room_type, price, availability_365, month_year
The neighbourhood_group column is used to identify listings associated with Christchurch.

2. Outputs from the pipeline

- "output/christchurch_airbnb_cleaned.csv"
A cleaned dataset containing Christchurch Airbnb listings and the required columns: id, latitude, longitude, neighbourhood, room_type, price, availability_365, and month_year.
- Number of input files
The number of CSV files found in the listing/ folder, printed to the console.
- Number of Christchurch listings
The total number of Christchurch listings after filtering and combining the input files.
- Dataset shape
The number of rows and columns in the cleaned dataset.
- Missing-value summary
The number of missing values in each column of the cleaned dataset.

3. Main steps in the pipeline

Step 1. Find raw data: Find all CSV files in the listing/ directory.

Step 2. Read the raw datasets: Read each CSV file into a pandas DataFrame.

Step 3. Filter Christchurch listings: Filter each dataset to retain listings where neighbourhood_group contains "Christchurch", regardless of capitalisation and while ignoring missing values.

Step 4. Combine datasets: Combine the Christchurch listings from all input files into a single DataFrame.

Step 5. Select required columns: Keep only the columns needed for the cleaned dataset: listing ID, geographic coordinates, neighbourhood, room type, price, availability, and month/year.

Step 6. Check data quality: Check the shape of the cleaned dataset and calculate the number of missing values in each column.

Step 7. Save the processed data: Create the output folder if necessary and save the cleaned Christchurch Airbnb dataset as "output/christchurch_airbnb_cleaned.csv".

## Deliverable 5


