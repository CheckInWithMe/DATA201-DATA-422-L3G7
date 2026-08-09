import glob
import pandas as pd
import csv

# NEED TO CHECK THAT ALL ENTRIES ARE IN CONTENTANATED FILE
def concatenate_files():
    # get all the csv files in raw_data folder
    raw_csvs = glob.glob("/Users/phuongnguyen/Desktop/2026_UC/data201/dev_3/raw_data/*.csv")

    # read all the raw csvs into a dataframe and put it in a list
    df_list = [pd.read_csv(file) for file in raw_csvs]

    # concatenate all dataframes into a single dataframe
    combined_df = pd.concat(df_list)

    # write the combined df into a csv
    combined_df.to_csv("concatenated_data.csv")


# def filter_data(input_file, filter_conditon):
    # output_file = input_file[input_file[filter_conditon]]

    # return output_file

def filter_to_christchurch(file_link):
    # read.csv -> take csv and turn it into a dataframe
    output_file = "christchurch.csv"
    concatenated_file = pd.read_csv(file_link)
    christchurch_data = concatenated_file[concatenated_file["neighbourhood_group"] == "Christchurch City"]
    christchurch_data.to_csv(output_file)

    return output_file

def select_columns(file_link):
    output_name = "christchurch_col_filtered.csv"
    input_file = pd.read_csv(file_link)
    output_file = input_file[["id", "name", "neighbourhood_group", "number_of_reviews"]]
    output_file.to_csv(output_name)

    return output_name


def filter_top_ten_percent(file_link):
    output_name = "christchurch_top_ten_filtered.csv" # you need to name the file type as well
    input_file = pd.read_csv(file_link)
    ten_percent_cutoff = round(len(input_file)*0.1)
    output_file = input_file.sort_values(by='number_of_reviews', ascending=False)
    output_file = output_file.head(ten_percent_cutoff)
    output_file.to_csv(output_name)

    return output_name

concatenated_file = "/Users/phuongnguyen/Desktop/2026_UC/data201/dev_3/concatenated_data.csv"
christchurch = f"/Users/phuongnguyen/Desktop/2026_UC/data201/dev_3/{filter_to_christchurch(concatenated_file)}"
christchurch_col_filtered = f"/Users/phuongnguyen/Desktop/2026_UC/data201/dev_3/{select_columns(christchurch)}"
christchurch_top_ten_percent_filtered = f"/Users/phuongnguyen/Desktop/2026_UC/data201/dev_3/{filter_top_ten_percent(christchurch_col_filtered)}"

print(f"Total amount of AirBnb listings in Christchurch: {len(pd.read_csv(christchurch).index)}")
final_df = pd.read_csv(christchurch_top_ten_percent_filtered)
print(final_df)
# pandas.set_option('display.max_columns', None)

