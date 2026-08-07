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