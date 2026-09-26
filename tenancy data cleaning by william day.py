'''Module that cleans quarterly 2020-2026 Tenancy data to specified requirements: Location Id, TimeFrame between 2025-10-01 and 2026-04-01, Dwelling Type and Median Rent.'''
import pandas
import numpy
import re
regex = re.compile(r'2026-|2025-(1[012])')

def date_filter(date): #matches regex to dates.
    match = regex.search(date)
    if match:
        return date #keeps original string. No need to convert to date format yet.
    return numpy.nan

def master(): #run master() to import and clean the data!
    tenancy = pandas.read_csv('data/raw/Detailed-Quarterly-Tenancy-Q1-2020-Q3-2026.csv', skiprows=[1, 2]) #These two rows instantly are invalid.
    pandas.set_option('display.max_columns', None) #For nice printing view to verify the data.
    tenancy = tenancy[['TimeFrame', 'Location Id', 'Dwelling Type','Number Of Beds', 'Median Rent', 'Total Bonds']]
    tenancy['TimeFrame'] = tenancy['TimeFrame'].apply(date_filter)
    tenancy = tenancy.dropna() #removes all NA rows. This includes some rows with no Location ID, and some with TimeFrame converted to NaN (outside date range)
    tenancy['Location Id'] = tenancy['Location Id'].astype(int)
    tenancy = tenancy[tenancy['Location Id'] > 0] #Removes '-99' Location Id values.
    tenancy = tenancy[(tenancy['Dwelling Type'] == 'ALL') & (tenancy['Number Of Beds'] == 'ALL')] #Since these are aggregated summary statistics.
    tenancy = tenancy.reset_index()
    print(tenancy.iloc[-1]) #to hide, put a # in front of this line and the line below.
    print(tenancy.head())
    return tenancy.to_csv('data/processed/Detailed-Quarterly-Tenancy.csv')




master()