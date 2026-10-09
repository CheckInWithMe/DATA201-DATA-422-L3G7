'''Compares prices of AirBNB's in Christchurch in a histogram plot.'''
import pandas
import numpy
import matplotlib.pyplot

"""def load_func(): #Master program. Imports, cleans, and plots. X can be changed if temporal scope of listings change, assuming data starts from listings(1).
    airbnb = pandas.read_csv('data/processed/christchurch_data.csv')
    clean_airbnb = clean_data(airbnb)
    #pandas.set_option('display.max_columns', None)
    #print(clean_airbnb.head()) #to view dataset, change the last line to 'return clean_airbnb.head().
    return display_data(clean_airbnb)"""

def clean_data(christchurch_data): #Removes NaN values, simplifies DataFrame to necessary columns and scope.
    copied_christchurch_data = christchurch_data.copy()
    clean_airbnb = copied_christchurch_data[['neighbourhood_group', 'price']]
    clean_airbnb = clean_airbnb.dropna()
    return clean_airbnb

def display_data(airbnb,output): #Produces histogram with custom bins the same as the no-code solution
    output_plot = matplotlib.pyplot.figure()
    matplotlib.pyplot.hist(airbnb['price'], bins=[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500])
    matplotlib.pyplot.xlabel('AirBNB nightly price ($NZD)')
    matplotlib.pyplot.title('Christchurch AirBNB price frequencies')
    matplotlib.pyplot.show()
    output_plot.savefig(output, dpi=output_plot.dpi, bbox_inches='tight')
    