# How this file was generated
I used ChatGPT to generate the files
This was the chat thread I used: https://chatgpt.com/c/6abdd357-785c-83ec-9c56-439fb5fd6b12

# Data principles

- we tried to divide work(code and documentation) 4 equal ways

- If the pipeline required certain steps to be done by one person before allowing others to do work, we tried to group that work for one person

- When there was not enough work we prioritised having equal work

# Deliverable 3
## Sakshi's processing.py
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

## Dao's

1. Inputs to the pipeline

The pipeline takes multiple Airbnb listing CSV files as input.

Input folder: C:\listing\

Input file pattern: C:\listing\*.csv

Input format: CSV files.

Expected data: Airbnb listing information containing the following columns:

neighbourhood_group: Used to identify listings associated with Christchurch.

last_review: The date of the most recent review for each listing.

The pipeline searches for all CSV files matching the specified file pattern and processes each file individually before combining the results.

2. Outputs from the pipeline

Number of input files

The number of CSV files found in the input folder, printed to the console.

File paths

The paths of all discovered CSV files, printed to the console.

Scrape dates

The most recent review date found in each file's Christchurch listings, printed to the console.

Combined Christchurch dataset

A DataFrame containing Christchurch listings from all input files, including the calculated days_since_last_review column.

Number of Christchurch listings

The total number of Christchurch listing records after combining the datasets, printed to the console.

Review information

The first 10 rows of the last_review and days_since_last_review columns, printed to the console.

Histogram plot

A histogram showing the distribution of days since the last review across Christchurch listing records with valid calculated values.

The histogram is displayed on screen and illustrates how recently listings received reviews relative to the most recent review date found in each individual file.

3. Main steps in the pipeline

Step 1: Find raw data files

Search the C:\listing\ directory for all CSV files and print the number of files found and their paths.

Step 2: Read the datasets

Read each CSV file into a pandas DataFrame.

Step 3: Filter Christchurch listings

Filter each dataset to retain listings where neighbourhood_group contains the word "Christchurch", regardless of capitalisation. Missing values are excluded from the location filter.

Step 4: Convert review dates

Convert the last_review column to datetime format. Values that cannot be converted are treated as missing.

Step 5: Determine the most recent review date

For each file, calculate the latest valid last_review date among its Christchurch listings. This date is printed as the file's reference date.

Step 6: Calculate days since the last review

For each listing, subtract its last_review date from the most recent review date identified in that same file. Store the result in a new column called days_since_last_review.

Step 7: Combine the datasets

Append the filtered Christchurch data from all input files into one combined DataFrame and print the total number of listing records.

Step 8: Display review information

Print the first 10 rows of the last_review and days_since_last_review columns for inspection.

Step 9: Visualise the results

Generate a histogram with 30 bins to show the distribution of days since the last review across the combined Christchurch listings.

Important implementation note: The reference date is calculated separately for each CSV file, rather than using one common date across all files. Therefore, the resulting days_since_last_review values measure the time since each file's most recent Christchurch review, not the time since a shared current date. If the files represent different months, this distinction matters when comparing review recency across them.

## William's "airbnb_christchurch_prices.py"
Data Pipeline Overview
1. Inputs to the pipeline

The pipeline takes multiple CSV files containing Airbnb listing data as its input.

Input files: listings(1).csv through listings(x).csv, where x is entered by the user when the program runs.

Input format: CSV files.

Expected data: Airbnb listing information containing the following columns: neighbourhood_group, price

The user specifies how many listing files to load. For example, entering 9 loads listings(1).csv through listings(9).csv.

2. Outputs from the pipeline

- "airbnb_frequencies.png"

A saved histogram showing the frequency distribution of Airbnb nightly prices in Christchurch City.

- Histogram plot

A visualisation showing the number of listings within specified price ranges.

-X-axis

Airbnb nightly price in NZD.

- Plot title

Christchurch AirBNB price frequencies.

The histogram uses the following price bins: $100–$200, $200–$300, $300–$400, $400–$500, $500–$600, $600–$700, $700–$800, $800–$900, $900–$1,000, and $1,000–$1,500.

The histogram is displayed on screen and saved as a PNG image.

3. Main steps in the pipeline

Step 1: Obtain user input

Ask the user to enter the number of listing CSV files to load.

Step 2: Load the raw datasets

Read the specified listing CSV files into individual pandas DataFrames and combine them into a single DataFrame.

Step 3: Select relevant columns

Keep only the neighbourhood_group and price columns, as these are the variables required for the analysis.

Step 4: Filter Christchurch listings

Retain only Airbnb listings where neighbourhood_group equals Christchurch City.

Step 5: Remove missing values

Remove rows containing missing values in the selected columns to ensure that the histogram uses available location and price information.

Step 6: Generate the histogram

Plot the distribution of Airbnb nightly prices using predefined price intervals, with the frequency of listings displayed on the vertical axis.

Step 7: Display and save the plot

Display the histogram on screen and save it as airbnb_frequencies.png for later use or inclusion in reports.

## Tram's filter_chch_top_ten_review_py
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

# Deliverable 4
## Dao's deliverable_week8.py
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

## William's tenancy_data_cleaning.py
1. Inputs to the pipeline

The pipeline takes a quarterly Tenancy dataset containing rental information from 2020–2026 as its input.

Input file: data/raw/Detailed-Quarterly-Tenancy-Q1-2020-Q3-2026.csv

Input format: CSV file.

Expected data: Tenancy information containing fields such as: TimeFrame, Location Id, Dwelling Type, Number Of Beds, Median Rent, Total Bonds

The pipeline uses these fields to select the required rental information and restrict the data to the specified timeframe and aggregated dwelling categories.

2. Outputs from the pipeline
- "data/processed/Detailed-Quarterly-Tenancy.csv"
  
A cleaned Tenancy dataset containing records within the specified timeframe, valid location IDs, and aggregated dwelling and bedroom categories.

-Printed final row

Displays the final row of the cleaned dataset in the console for verification.

-Printed first rows

Displays the first five rows of the cleaned dataset in the console for verification.

3. Main steps in the pipeline

Step 1. Read raw data: Read the quarterly Tenancy CSV file from data/raw/, skipping the two invalid rows identified in the source file.

Step 2. Select required columns: Keep only the columns required for the analysis: timeframe, location ID, dwelling type, number of beds, median rent, and total bonds.

Step 3. Filter the timeframe: Use a regular expression to retain records from the specified timeframe, covering the relevant 2025 and 2026 quarters.

Step 4. Remove invalid and missing data: Remove rows containing missing values, including records with invalid or missing timeframe and location information.

Step 5. Clean location IDs: Convert Location Id to integers and remove invalid -99 location IDs by retaining only positive location IDs.

Step 6. Filter dwelling and bedroom categories: Keep only records where both Dwelling Type and Number Of Beds are "ALL", ensuring that the dataset contains aggregated rental statistics rather than individual dwelling or bedroom categories.

Step 7. Reset the index: Reset the DataFrame index after filtering the data.

Step 8. Verify and save the data: Print the final row and first five rows for verification, then save the cleaned dataset to data/processed/Detailed-Quarterly-Tenancy.csv.

# Deliverable 5
## Tram's append_sa22026 _code_name.py

1. Inputs to the pipeline

The pipeline takes an Airbnb dataset containing latitude and longitude coordinates as its input.

Input file: ./data/christchurch_air_bnb_code_appended.csv

Input format: CSV file.

Required data: Airbnb listing information containing: latitude, longitude

The pipeline also requires a Koordinates API key, which is entered by the user when the program runs.

The pipeline uses Koordinates Statistical Area 2 (SA2) 2026 layer 123515 to identify the statistical area associated with each Airbnb's coordinates.

2. Outputs from the pipeline

- "./data/christchurch_air_bnb_code_name_appended.csv"
  
A new CSV file containing the original Airbnb data with an additional sa22026_name column containing the SA2 2026 region name associated with each listing's coordinates.

- SA2 region names
  
The Koordinates API is queried using each listing's latitude and longitude to determine its corresponding SA2 2026 region name.
- Progress/status messages
  
The program prints messages indicating when the input has been opened, coordinates have been matched, and the output file has been written.

- Error messages

Invalid coordinates, missing API results, or invalid function inputs are reported in the console.

Note: The code currently appends the SA2 region name. The commented-out line could instead be used to append the SA2 code.

3. Main steps in the pipeline

Step 1. Set up the pipeline: Set the working directory, obtain the Koordinates API key, and specify the input/output files and Koordinates SA2 2026 layer.

Step 2. Read the Airbnb data: Read the input CSV file into a pandas DataFrame and determine the number of rows that will be processed.

Step 3. Validate the number of rows: Determine whether the pipeline should process all rows or a specified number of rows and check that the requested number is valid.

Step 4. Query Koordinates: For each Airbnb listing, use its latitude and longitude to send a request to the Koordinates API. The API identifies the Statistical Area 2 2026 region corresponding to those coordinates.

Step 5. Append the SA2 region name: Extract the SA22026_V1_00_NAME value returned by Koordinates and add it to the Airbnb dataset as a new sa22026_name column.

Step 6. Handle errors: Check for invalid latitude/longitude values, coordinates that produce no matching result, and invalid query types, reporting these issues in the console.

Step 7. Save the processed data: Save the original Airbnb data together with the newly appended SA2 region names to ./data/christchurch_air_bnb_code_name_appended.csv.

## Saksi's combine_data.py

1. Inputs to the pipeline

The pipeline takes two processed datasets as inputs.

Tenancy input: data/processed/Detailed-Quarterly-Tenancy.csv

Airbnb input: data/processed/christchurch_airbnb_appended.csv

The Airbnb dataset contains information such as: sa22026_code, month_year, price

The Tenancy dataset contains information such as: Location Id, TimeFrame, Median Rent, Total Bonds

The two datasets are matched using their SA2 area code and month.

2. Outputs from the pipeline

- "data/processed/christchurch_airbnb_tenancy_joined.csv"
  
A combined dataset containing Airbnb observations joined with the corresponding Tenancy data by SA2 area code and month.

- Airbnb rows before merge
  
The number of Airbnb observations before joining the datasets, printed to the console.

- Rows after merge

The total number of rows in the joined dataset, printed to the console.

- Rows with rental data
  
The number of Airbnb observations that successfully matched to Tenancy data based on area and month.

- Rows without rental data
  
The number of Airbnb observations that did not have corresponding Tenancy data.

- Median Airbnb price in Christchurch Central
  
The median Airbnb price for listings with SA2 code 326600, calculated and printed to the console.

4. Main steps in the pipeline

Step 1. Load the datasets: Read the processed Airbnb and Tenancy CSV files into pandas DataFrames.

Step 2. Standardise the Airbnb dates: Convert the Airbnb month_year values into monthly periods so they can be matched consistently with the Tenancy data.

Step 3. Standardise the Tenancy dates: Convert the Tenancy TimeFrame values into the same monthly period format.

Step 4. Join the datasets: Merge the Airbnb and Tenancy datasets using sa22026_code from the Airbnb data and Location Id from the Tenancy data, together with the corresponding month. A left join is used so that all Airbnb observations are retained, even when matching rental data is unavailable.

Step 5. Check the merge: Compare the number of Airbnb rows before and after the merge and count how many observations have matching rental data and how many do not.

Step 6. Save the joined dataset: Save the merged Airbnb and Tenancy dataset to data/processed/christchurch_airbnb_tenancy_joined.csv.

Step 7. Calculate Christchurch Central Airbnb price: Filter the Airbnb dataset to SA2 code 326600, representing Christchurch Central, and calculate the median Airbnb price for those listings.

## Dao's "gap between short-term and long-term.py"

1. Inputs to the pipeline

The pipeline takes two datasets as inputs.

Tenancy input: data/Detailed-Quarterly-Tenancy-Q1-2020-Q3-2026.csv

Airbnb input: data/christchurch_airbnb_tenancy_joined.csv

The Airbnb dataset contains information including: sa22026_code, month_year, price

The Tenancy dataset contains information including: Location Id, TimeFrame, Dwelling Type, Median Rent

These datasets are used to compare short-term Airbnb prices with long-term rental prices across Christchurch locations.

2. Outputs from the pipeline
   
- Tenancy rows after filtering
  
The number of Tenancy records remaining after filtering to Dwelling Type == "ALL", printed to the console.

- Joined dataset
  
A dataset combining Airbnb and long-term rental information by location and quarter.

- Rows available for analysis
  
The number of observations remaining after removing rows without price, rental, price-gap, or location information.

- Location summary
  
Summary statistics for the Airbnb price gap for each location, including median, mean, maximum, minimum, and number of Airbnb listings.

- Top 20 locations
  
The 20 locations with the largest median Airbnb-to-long-term-rent price gap, printed to the console.

- Largest-gap location
  
The location with the largest median price gap and its median price gap, printed to the console.

- Airbnb details
  
Airbnb price, long-term rental price, and price gap information for the location with the largest median gap.

- Price-gap boxplot
  
A boxplot showing the distribution of Airbnb price gaps for the top 10 locations.

- Price comparison chart
  
A bar chart comparing median short-term Airbnb prices with median long-term rental prices per night for the top 10 locations.

3. Main steps in the pipeline

Step 1. Load the datasets: Read the Tenancy and Airbnb datasets from the data directory.

Step 2. Convert dates: Convert the Airbnb month_year and Tenancy TimeFrame columns into datetime values and then convert them into quarterly periods.

Step 3. Filter Tenancy data: Keep the Tenancy records where Dwelling Type is "ALL" and retain the location ID, quarter, dwelling type, and median rent.

Step 4. Prepare the datasets for joining: Rename the Tenancy Location Id to `

## William's "comparison_by_region.py"

1. Inputs to the pipeline

The pipeline takes a combined Airbnb and Tenancy dataset and an official Statistical Area 2 (SA2) geographic shapefile as inputs.

Input dataset: christchurch_airbnb_tenancy_joined.csv

Input shapefile: data/raw/statsnz-statistical-area-2-2026-SHP

Input formats: CSV and ESRI Shapefile.

Expected data: The combined dataset contains Airbnb listing information and Tenancy rental information, including: sa22026_code, location id, geographic data

The pipeline uses these inputs to calculate Airbnb and rental property counts for each SA2 area and display them on an interactive map.

2. Outputs from the pipeline

- "data/processed/sa2_areas_map.html"
  
An interactive HTML map displaying SA2 geographic areas with Airbnb and Tenancy counts.

- SA2_2026_Code
  
The SA2 2026 geographic area code for each mapped region.

- SA2_2026_Name
  
The name of each mapped SA2 region.

- AirBNB_Count
  
The number of Airbnb listings associated with each SA2 code.

- Rental_Count
  
The number of Tenancy records associated with each SA2 code.

The interactive map displays the SA2 code, area name, Airbnb count, and rental count when users interact with the geographic regions.

Only areas containing at least one Airbnb listing or one Tenancy record are included in the final map.

3. Main steps in the pipeline

Step 1. Load the combined dataset: Read the combined Airbnb and Tenancy CSV file into a pandas DataFrame.

Step 2. Separate Airbnb and Tenancy records: Use the presence or absence of Location Id to distinguish Tenancy records from Airbnb records. Convert the relevant location codes to integers.

Step 3. Load the SA2 geographic data: Read the official SA2 2026 shapefile using GeoPandas and retain only the SA2 code, SA2 name, and geographic boundary columns.

Step 4. Standardise geographic codes: Convert the SA2 geographic codes to integers so they can be matched with the codes in the Airbnb and Tenancy datasets.

Step 5. Count Airbnb listings by SA2 area: Count the Airbnb records associated with each SA2 code and map these counts onto the geographic dataset as AirBNB_Count.

Step 6. Count Tenancy records by SA2 area: Count the Tenancy records associated with each Location Id and map these counts onto the geographic dataset as Rental_Count.

Step 7. Filter geographic areas: Retain only SA2 regions that have at least one Airbnb listing or one Tenancy record.

Step 8. Rename columns: Rename the geographic code and name columns to SA2_2026_Code and SA2_2026_Name for clarity.

Step 9. Generate the interactive map: Use GeoPandas to create an interactive map with the cartodbpositron basemap. Configure the map to display the SA2 code, region name, Airbnb count, and rental count in the interactive tooltips.

Step 10. Save the map: Save the interactive map as data/processed/sa2_areas_map.html, allowing it to be opened in a web browser.

Important implementation note: The code counts Tenancy records, not necessarily unique rental properties. If the Tenancy dataset contains multiple records for the same area across different quarters or dwelling categories, Rental_Count will count those records rather than distinct properties.
