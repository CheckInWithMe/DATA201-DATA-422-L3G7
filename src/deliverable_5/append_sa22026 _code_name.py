'''Given AirBnb data with latitude and longitude columns, get the sa22026 code and/or sa22026 region name 
from Koordinates and append that to the given AirBnb data in a separate file'''

import pandas as pd
import requests 
import os
import threading
from tqdm import tqdm

os.chdir("") # Set working directory here 

tqdm.pandas(desc="Processing rows") # Make a progress bar that applies to pandas functions

KEY = input("What is your API key?: ")
LAYER_ID = "123515" # taken from https://datafinder.stats.govt.nz/layer/123515-statistical-area-2-2026/
INPUT_FILE = "./data/christchurch_airbnb_cleaned.csv"
OUTPUT_FILE = "./data/christchurch_air_bnb_code_name_appended_threaded.csv"
    

def query(latitude, longitude, type):
    '''do the query on koordinates and see if any errors occur eg. latitude or longitude is out of range, incorrect inputs for function
    '''
    try:
        if latitude < -90 or latitude > 90:
            raise ValueError(f"Latitude({latitude}) is out of range")
        if longitude < -180 or longitude > 180:
            raise ValueError(f"Longitude({longitude}) is out of range")
        
        request = requests.get(f"https://koordinates.com/services/query/v1/vector.json?key={KEY}&layer={LAYER_ID}&x={longitude}&y={latitude}&max_results=3&radius=10000&geometry=true&with_field_names=true")
        if type == "sa22026_code":
            output = request.json()['vectorQuery']['layers'][LAYER_ID]['features'][0]['properties']['SA22026_V1_00']
        if type == "sa22026_name":
            output = request.json()['vectorQuery']['layers'][LAYER_ID]['features'][0]['properties']['SA22026_V1_00_NAME']
        
        return output
        
    except IndexError:
        print(f"No output given for coordinates(latitude: {latitude}, longitude: {longitude}). Coordinates not in NZ maybe?")

    except ValueError as e:
        print(f"Caught error: {e}")

    except:
        if type not in ["sa22026_code", "sa22026_name"]:
            print(f"Type is not valid. Coordinates were (latitude: {latitude}, longitude: {longitude}). ")
        

def get_sa22026_code_name(df, index, output_dict, rows="ALL"):
    '''get the sa22026_code or the sa22026 region name from the query, put it into a new column and read it to new csv
    '''
    df_rows = len(df)

    # see if there are any errors in the rows parameter
    if rows == "ALL": # if no input given for rows, assume we want to append a sa22026 code/name to every row
        rows = [1, df_rows]
    elif type(rows) is not list: # terminate the function if the input given for rows is not a list
        print("Input for rows parameter is not an list")
        return
    elif len(rows) != 2: # terminate the function if the integer input given for rows does not contain 2 values
        print("Input for rows parameter does not contain 2 values")
        return 
    start, end = rows

    # initialise columns 'sa22026_code' and 'sa22026_name' to be string types
    if "sa22026_code" not in df.columns:
        df["sa22026_code"] = pd.Series(index= df.index, dtype="string")
    if "sa22026_name" not in df.columns:
        df["sa22026_name"] = pd.Series(index=df.index, dtype="string")

    # getting the sa22026 code and names
    df.loc[start:end, "sa22026_code"] = df.loc[start:end].progress_apply(lambda x: query(x.latitude, x.longitude, type="sa22026_code"), axis=1) 
    df.loc[start:end, "sa22026_name"] = df.loc[start:end].progress_apply(lambda x: query(x.latitude, x.longitude, type="sa22026_name"), axis=1) 

    output_dict[index] = df


def get_df_chunks(df,final_row, chunk_no):
    '''Get the indices for the start and end for 1/chunk_no of the input 
    csv as well as the separated chunks'''
    chunk_length = round(final_row/chunk_no)
    chunks = []
    chunk_indexes = []
    start = 0
    end = 0
    for index in range(chunk_no):
        if end > 0:
            start += chunk_length

        if start == 0:
            end += (chunk_length-1)
        else:
            end += chunk_length
        
        if index == chunk_no-1 and end != final_row-1:
            end = final_row-1

        chunks.append(df.loc[start:end].copy())
        chunk_indexes.append([start, end])

    return chunks, chunk_indexes

def main(input, output):
    '''Main function'''

    # read the input file you want to append 'sa22026_code' and 'sa22026_name' columns to
    air_bnb_df = pd.read_csv(input)
    df_len = len(air_bnb_df)

    # separate out the file into 5 separate chunks to make 
    final_row = df_len
    chunk_no = 5
    chunks, chunk_indexes = get_df_chunks(air_bnb_df,final_row,chunk_no)

    # put the results in a dictionary to ensure the results of the threads are not randomly put in
    results_dict = {}

    # create the threads, execute them and wait until all the threads have completed running
    thread_1 = threading.Thread(target=get_sa22026_code_name, args=(chunks[0], "0", results_dict, chunk_indexes[0]))
    thread_2 = threading.Thread(target=get_sa22026_code_name, args=(chunks[1], "1", results_dict, chunk_indexes[1]))
    thread_3 = threading.Thread(target=get_sa22026_code_name, args=(chunks[2], "2", results_dict, chunk_indexes[2]))
    thread_4 = threading.Thread(target=get_sa22026_code_name, args=(chunks[3], "3", results_dict, chunk_indexes[3]))
    thread_5 = threading.Thread(target=get_sa22026_code_name, args=(chunks[4], "4", results_dict, chunk_indexes[4]))

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_5.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()
    thread_5.join()

    # append results from results_dict into sorted_results in the correct order and append all the results from each chunk into one csv
    sorted_results = []

    for index in range(len(results_dict)):
        sorted_results.append(results_dict[str(index)])
        
    df_combined = pd.concat(sorted_results, ignore_index=True)

    # read final concatenated data to a csv
    df_combined.to_csv(output)

main(INPUT_FILE, OUTPUT_FILE)
