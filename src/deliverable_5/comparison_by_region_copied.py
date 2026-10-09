'''Compares counts of AirBNB and Tenancy properties by SA2 area codes, displaying them in an interactive HTML map that is saved locally.'''
import pandas
import numpy
import matplotlib.pyplot
import geopandas

def cleaning(): #Splits joined data into AirBNB and Tenancy data again.
    pandas.set_option('display.max_columns', None)
    airbnb = pandas.read_csv("data/processed/christchurch_airbnb_tenancy_joined.csv")
    print("Column names:", airbnb.columns.tolist())
    print("First 5 rows:")
    print(airbnb.head())
    tenancy = airbnb[pandas.isna(airbnb['Location Id']) == False] #to distinguish the join of airbnb and tenancy data.
    tenancy['Location Id'] = tenancy['Location Id'].astype(int)
    tenancy['Total Bonds'] = tenancy['Total Bonds'].astype(int) 
    airbnb = airbnb[numpy.isnan(airbnb['Location Id']) == True] #to distinguish the join of airbnb and tenancy data.
    airbnb['sa22026_code'] = airbnb['sa22026_code'].astype(int)
    return tenancy, airbnb
    
def master(): #Produces a viewable html interactive map!
    tenancy, airbnb = cleaning()
    sa2 = geopandas.read_file('data/raw/statsnz-statistical-area-2-2026-SHP') #Imports official SA2 shapefile.
    sa2 = sa2[['SA22026_V1', 'SA22026__1', 'geometry']] #Reduces data to just necessary columns.
    sa2['SA22026_V1'] = sa2['SA22026_V1'].astype(int) 
    sa2['AirBNB_Count'] =  sa2['SA22026_V1'].map(airbnb['sa22026_code'].value_counts())
    merger = tenancy[['Location Id', 'Total Bonds']]
    sa2 = sa2.merge(merger, left_on='SA22026_V1', right_on='Location Id', how='left')
    sa2 = sa2.rename(columns={'SA22026_V1': 'SA2_2026_Code', 'SA22026__1': 'SA2_2026_Name', 'Total Bonds': 'Rental_Count'}) #Renamed for clarity.
    sa2 = sa2[(sa2['AirBNB_Count'] > 0) | (sa2['Rental_Count'] > 0)] #selects only polygons with at least one entry in either polygon
    interactive_map = sa2.explore(tooltip=['SA2_2026_Code', 'SA2_2026_Name', 'AirBNB_Count', 'Rental_Count'], tiles="https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
                   attr="Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ") #Esri doesn't block public wifi, so using this as tile provider.
    interactive_map.save('data/processed/sa2_areas_map.html')

#master()
