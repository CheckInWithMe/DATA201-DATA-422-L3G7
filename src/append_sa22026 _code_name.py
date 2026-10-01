'''Given AirBnb data with latitude and longitude columns, get the sa22026 code and/or sa22026 region name 
from Koordinates and append that to the given AirBnb data in a separate file'''

import pandas as pd
import requests 
import os
from tqdm import tqdm


os.chdir("/Users/phuongnguyen/Desktop/2026_UC/data201/dev_5/") # Set working directory here 

tqdm.pandas(desc="Processing rows") # Make a progress bar that applies to pandas functions

KEY = input("What is your API key?: ")
LAYER_ID = "123515" # taken from https://datafinder.stats.govt.nz/layer/123515-statistical-area-2-2026/
INPUT_FILE = "./data/christchurch_air_bnb_code_appended.csv"
OUTPUT_FILE = "./data/christchurch_air_bnb_code_name_appended.csv"
    

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
        

def get_sa22026_code_name(input_file, output_file, rows="ALL"):
    '''get the sa22026_code or the sa22026 region name from the query, put it into a new column and read it to new csv
    '''
    df = pd.read_csv(input_file)
    df_rows = len(df)
    print("Input file successfully opened")

    if rows == "ALL": # if no input given for rows, assume we want to append a sa22026 code/name to every row
        rows = df_rows
    elif type(rows) is not int: # terminate the function if the input given for rows is not an integer
        print("Input for rows parameter is not an integer")
        return
    elif rows > df_rows or rows < 1: # terminate the function if the integer input given for rows is unreasonable
        print("Input for rows parameter is out of range")
        return
    else:
        rows = rows+1 

    # df.loc[:rows-1, "sa22026_code"] = df.head(rows).progress_apply(lambda x: query(x.latitude, x.longitude, type="sa22026_code"), axis=1) <- code to get the sa22026 code
    df.loc[:rows-1, "sa22026_name"] = df.head(rows).progress_apply(lambda x: query(x.latitude, x.longitude, type="sa22026_name"), axis=1) # code to get the sa22026 name
    print("Coordinates matched to code/name")

    df.to_csv(output_file)
    print("Output file successfully written")


get_sa22026_code_name(INPUT_FILE, OUTPUT_FILE)
