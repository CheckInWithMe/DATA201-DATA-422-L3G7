import pandas
import numpy
import matplotlib.pyplot

def load_func():
    airbnb = pandas.read_csv('listings.csv')
    clean_airbnb = clean_data(airbnb)
    pandas.set_option('display.max_columns', None)
    print(clean_airbnb.head())
    return display_data(clean_airbnb)

def clean_data(airbnb):
    clean_airbnb = airbnb[['neighbourhood_group', 'price']]
    clean_airbnb = clean_airbnb[clean_airbnb['neighbourhood_group'] == 'Christchurch City']
    clean_airbnb = clean_airbnb.dropna()
    return clean_airbnb

def display_data(airbnb): #
    matplotlib.pyplot.hist(airbnb['price'], bins=[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500])
    matplotlib.pyplot.xlabel('AirBNB nightly price ($NZD)')
    matplotlib.pyplot.title('Christchurch AirBNB price frequencies')
    matplotlib.pyplot.show()