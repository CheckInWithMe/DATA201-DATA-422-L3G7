# Project Summary

This project focuses on **data wrangling and exploratory data analysis (EDA)** using Airbnb listing data for New Zealand. The objective is to clean, transform, and prepare multiple monthly datasets for analysis by applying common data wrangling techniques such as filtering, handling missing values, creating new features, and combining datasets.

The data used in this project is provided by the **Inside Airbnb** project, which aims to quantify the impact of short-term rentals on housing and residential communities while supporting research, journalism, and public policy discussions.

The datasets were downloaded from the official Inside Airbnb website and are used solely for educational and research purposes.

# Data Source

This data is licensed under a Creative Commons Attribution 4.0 International License.

Source: http://insideairbnb.com/

This project uses Airbnb listing data provided by the **Inside Airbnb** project. The data contains information about Airbnb listings across New Zealand, including property details, host information, location, pricing, availability, and guest reviews.

Only the data required for this project has been downloaded from the official Inside Airbnb website.

# License

Permissions:
1. Share and redistribute the data.
2. Adapt, modify, and build upon the data for any purpose.

Conditions:
1. Give appropriate credit to Inside Airbnb project. 
2. Indicate the changes, made to the original data.
3. Do not apply additional legal terms or technological measures that restrict others from exercising the rights granted by the licence.
4. Provide a link to the CC BY 4.0 licence.


License: https://creativecommons.org/licenses/by/4.0/

# Downloading the Data

1. Visit **http://insideairbnb.com/**.
2. Download the required monthly **New Zealand** `listings.csv` datasets.
3. Place the downloaded files in the `data/raw/` directory.

# Data dictionary

| Variables                        | Data types   | Descrition                                                                                                     
| -------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------- 
| id                               | integer      | Unique identifier for the Airbnb listings.
| name                             | string       | Name of the listing.
| host_id                          | integer      | Unique identifier for the host.
| host_name                        | string       | Name of the host.
| neighbourhood_group              | string       | City or District where the Airbnb listing is located.
| neighbourhood                    | string       | The local area within the city or district the listing is located.
| latitude                         | float        | The geographic latitude coordinate of the Airbnb listing location.
| longitude                        | float        | The geographic longitude coordinate of the Airbnb listing location.
| room_type                        | string       | The type of stay is categorised into 4 types:
|                                  |              | 1. Entire home/apt - Guests have access to the entire property and do not share spaces with the host or other guests.
|                                  |              | 2. Hotel room – Guests book a private or shared room within a hotel or similar accommodation.
|                                  |              | 3. Private room – Guest have a private bedroom but shared common areas.
|                                  |              | 4. Shared room – Guests share the sleeping space and common areas with other people.
| prices                           | integer      | The cost of the Airbnb stay per night
| minimum_nights                   | integer      | Minimum number of night stay for the listing.
| number_of_reviews                | integer      | The total number of reviews received from the guests.
| last_review                      | date         | The date of the latest review received by the listing.
| reviews_per_month                | float        | The average number of reviews received per month. 
| calculated_host_listings_count   | integer      | The number of listings the host has in the city or region.
| availability_365                 | integer      | The number of days the Airbnb listing is available for booking within the next 365 days according to the host's calendar.
| number_of_reviews_ltm            | integer      | The number of reviews the listing has in the last 12 months.
| License                          | string       | The licence, permit or registration number

# Rental bond data

# # Data Source

Source: https://www.tenancy.govt.nz/about-tenancy-services/data-and-statistics/rental-bond-data/
We have downloaded the 'Detailed quarterly report, January 2020 to April 2026' CSV file. This data documents the record of private bonds

# # Columns
Column definitions are paraphrased from the following websites

- Timeframe, Median Rent, Geometric Mean Rent, Upper Quartile Rent, Lower Quartile Rent is provided by Tenancy Services(source: https://www.tenancy.govt.nz/about-tenancy-services/data-and-statistics/rental-bond-data/)

- Location Id, is provided by StatsNZ(source: https://datafinder.stats.govt.nz/layer/98970-statistical-area-2-2019-generalised/attachments/21843/view/, code for getting Location Id: https://portal.api.business.govt.nz/api/market-rent)

- Dwelling Type, equations to calculate Upper Quartile Rent, Lower Quartile Rent and Log Std Dev is provided by Market API(source: https://portal.api.business.govt.nz/api/market-rent).

- Total Bonds, Active Bonds, Closed Bonds is provided by Figure.NZ(source: https://figure.nz/table/vCV1Lmu8Crq2M1KB)

| Variables                        | Data types   | Descrition                                                                                                     
| -------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------- 
| Timeframe                        | date         | Month for which data is recorded(the day of the date is always 01)
| Location Id                      | integer      | 6 digit code determined by SA2-2019 area definitions. (SA2-2019 encompasses areas with 2000-4000 people in city council areas)
| Dwelling Type                    | string       | Can take the values: Apartment, Boarding House, Flat, House, Room, ALL(ALL is for statistics applied across all dwelling types)
| Number of Beds                   | integer      | Number of bedrooms
| Total Bonds                      | integer      | Number of tenancy agreements lodged in the month
| Active Bonds                     | integer      | Number of tenancy agreements that starting from that month, are still active
| Closed Bonds                     | integer      | Number of tenancy agreements that were ended within the month
| Median Rent                      | integer      | Median of the rents in the private properties within the indicated SA2-2019 area.
| Geometric Mean Rent              | integer      | Obtained by multiplying n number of rents within the SA2-2019 area together then taking the nth root of the result. This can be used instead of the median/mean as it is less influenced by outliers.
| Upper Quartile Rent              | integer      | 75th percentile of all rents in the SA2-2019 area(calculated by )
| Lower Quartile Rent              | integer      | 25th percentile of all rents in the SA2-2019 area
| Log Std Dev Weekly               | float        | Sample standard deviation of natural logarithm weekly rent of bonds lodged within the period.

# # Data Cleaning Process

We decided to keep the following columns: Timeframe, Location Id, Dwelling Type, Median Rent, Active Bonds
Using the median rent instead of the geometric mean rent would be adequate for our dataset because the median is not easily influenced by outlier values.

We decided to filter the rows to the time period of October 2025 ~ April 2026. The start month of October 2025 is the same starting month as the AirBnb data. Other than this, we decided to not do any more filtering on the rows as we were not yet sure for which rows will be needed and which are not.
 
