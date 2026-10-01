'''Given Airbnb data, filter the data to the top ten percent reviewed Airbnbs in Christchurch and find the number of total Airbnbs in Christchurch'''
import glob
import pandas as pd

INPUT = glob.glob("./data/raw/*.csv")
OUTPUT = "./data/processed/christchurch_top_ten_filtered.csv"

def filter_to_ten_percent(input_files, output_file):

    # Concantenate all the files together
    df_list = [pd.read_csv(file) for file in input_files]
    concatenated_file = pd.concat(df_list)
    print("All csvs concatenated")
    
    # filter data to just data on Christchurch City with columns id, name, neighbourhood_group, number_of_reviews
    christchurch_data = concatenated_file[concatenated_file["neighbourhood_group"] == "Christchurch City"]
    christchurch_data = christchurch_data[["id", "name", "neighbourhood_group", "number_of_reviews"]]
    christchurch_len = len(christchurch_data) # note down the number of entries in christchurch_data
    print("Filtered to Christchurch data")

    # sort the christchurch data by reviews and cut off the bottom 90% 
    ten_percent_cutoff = round(len(christchurch_data)*0.1)
    top_ten = christchurch_data.sort_values(by='number_of_reviews', ascending=False)
    top_ten = top_ten.head(ten_percent_cutoff)
    top_ten.to_csv(output_file)
    print("Top ten filtered data")

    return christchurch_len


chch_len = filter_to_ten_percent(INPUT, OUTPUT)

print(f"Total amount of AirBnb listings in Christchurch: {chch_len}")
final_df = pd.read_csv(OUTPUT)
print(final_df)
