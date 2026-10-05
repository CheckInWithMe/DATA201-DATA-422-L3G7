'''Given Airbnb data, filter the data to the top ten percent reviewed Airbnbs in Christchurch and find the number of total Airbnbs in Christchurch'''
import glob
import pandas as pd
import os

os.chdir("") # set working directory here

INPUT = "./data/processed/christchurch_data.csv"
OUTPUT = "./data/processed/christchurch_top_ten_filtered.csv"

def filter_to_ten_percent(input_file, output_file):
    '''filter data to the necessary columns and sort the christchurch data by 
    number of reviews and cut off the bottom 90% '''
    
    christchurch_data = pd.read_csv(input_file)

    ten_percent_cutoff = round(len(christchurch_data)*0.1) 
    columns = ["id","name", "neighbourhood","number_of_reviews"]
    top_ten = christchurch_data[columns].copy()
    top_ten = top_ten.sort_values(by='number_of_reviews', ascending=False)
    top_ten = top_ten.head(ten_percent_cutoff)

    top_ten.to_csv(output_file)

    return len(christchurch_data)


chch_len = filter_to_ten_percent(INPUT, OUTPUT)

print(f"Total amount of AirBnb listings in Christchurch: {chch_len}")
