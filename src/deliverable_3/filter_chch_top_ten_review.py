'''Given Airbnb data, filter the data to the top ten percent reviewed Airbnbs in Christchurch and find the number of total Airbnbs in Christchurch'''
import glob
import pandas as pd
import os

#os.chdir("") # set working directory here


def filter_to_ten_percent(christchurch_data, output_file):
    '''filter data to the necessary columns and sort the christchurch data by 
    number of reviews and cut off the bottom 90% '''
    
    copied_christchurch_data = christchurch_data.copy()

    ten_percent_cutoff = round(len(copied_christchurch_data)*0.1) 
    columns = ["id","name", "neighbourhood","number_of_reviews"]
    top_ten = copied_christchurch_data[columns].copy()
    top_ten = top_ten.sort_values(by='number_of_reviews', ascending=False)
    top_ten = top_ten.head(ten_percent_cutoff)

    top_ten.to_csv(output_file)
    print(f"Total amount of AirBnb listings in Christchurch: {len(copied_christchurch_data)}")
    return len(copied_christchurch_data)


#chch_len = filter_to_ten_percent(INPUT, OUTPUT)


