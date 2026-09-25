import pandas
import numpy
import matplotlib.pyplot
import geopandas

def cleaning(): #run master() to produce a viewable html interactive map!
    pandas.set_option('display.max_columns', None)
    airbnb = pandas.read_csv('christchurch_airbnb_tenancy_joined.csv')
    tenancy = airbnb[numpy.isnan(airbnb['Location Id']) == False] #to distinguish the join of airbnb and tenancy data.
    tenancy['Location Id'] = tenancy['Location Id'].astype(int)
    
    airbnb = airbnb[numpy.isnan(airbnb['Location Id']) == True] #to distinguish the join of airbnb and tenancy data.
    airbnb['sa22026_code'] = airbnb['sa22026_code'].astype(int)
    return tenancy, airbnb
    
def master():
    tenancy, airbnb = cleaning()
    sa2 = geopandas.read_file('statsnz-statistical-area-2-2026-SHP') #Imports official SA2 shapefile.
    sa2 = sa2[['SA22026_V1', 'SA22026__1', 'geometry']] #Reduces data to just necessary columns.
    sa2['SA22026_V1'] = sa2['SA22026_V1'].astype(int) 
    sa2['AirBNB_Count'] =  sa2['SA22026_V1'].map(airbnb['sa22026_code'].value_counts())
    sa2['Rental_Count'] = sa2['SA22026_V1'].map(tenancy['Location Id'].value_counts())
    sa2 = sa2[(sa2['AirBNB_Count'] > 0) | (sa2['Rental_Count'] > 0)]
    sa2 = sa2.rename(columns={'SA22026_V1': 'SA2_2026_Code', 'SA22026__1': 'SA2_2026_Name'}) #Renamed for clarity.
    interactive_map = sa2.explore(tooltip=['SA2_2026_Code', 'SA2_2026_Name', 'AirBNB_Count', 'Rental_Count'], tiles='cartodbpositron') #I picked cartodbpositron as API key warning messages are less annoying.
    interactive_map.save('sa2_areas_map.html')