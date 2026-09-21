import pandas as pd
import requests 
import os
from tqdm import tqdm


os.chdir("/Users/phuongnguyen/Desktop/2026_UC/data201/dev_5/") # Set working directory, can change it

tqdm.pandas(desc="Processing rows") # Make a progress bar

KEY = "c7407c45afd94de2877ad480d4f37adf"
LAYER_ID = "123515"
INPUT_FILE = "./data/christchurch_airbnb_cleaned.csv"
OUTPUT_FILE = "./data/christchurch_air_bnb_appended.csv"
    
# do the query on koordinates and see if any errors occur
def query(latitude, longitude, type):
    try:
        if latitude < -90 or latitude > 90:
            raise ValueError(f"Latitude({latitude}) is out of range")
        if longitude < -180 or longitude > 180:
            raise ValueError(f"Longitude({longitude}) is out of range")
        
        request = requests.get(f"https://koordinates.com/services/query/v1/vector.json?key={KEY}&layer={LAYER_ID}&x={longitude}&y={latitude}&max_results=3&radius=10000&geometry=true&with_field_names=true")
        if type == "sa22026_code":
            output = request.json()['vectorQuery']['layers'][LAYER_ID]['features'][0]['properties']['SA22026_V1_00']
        
        return output
        
    except IndexError:
        print(f"No output given for coordinates(latitude: {latitude}, longitude: {longitude}). Coordinates not in NZ maybe?")

    except ValueError as e:
        print(f"Caught error: {e}")

    except:
        if type not in ["sa22026_code", "sa22026_name"]:
            print(f"Type is not valid. Coordinates were (latitude: {latitude}, longitude: {longitude}). ")
        

# get the sa22026_code from the query put it into a new column and read it to new csv
def get_sa22026_code_name(input_file, output_file):
    df = pd.read_csv(input_file)
    rows = len(df)
    print("Input file successfully opened")

    df.loc[:rows-1, "sa22026_code"] = df.head(rows).progress_apply(lambda x: query(x.latitude, x.longitude, type="sa22026_code"), axis=1)
    print("Coordinates matched to code")

    df.to_csv(output_file)
    print("Output file successfully written")


get_sa22026_code_name(INPUT_FILE, OUTPUT_FILE)
