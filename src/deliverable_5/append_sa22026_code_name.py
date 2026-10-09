'''Given AirBnb data with latitude and longitude columns, get the sa22026 code and/or sa22026 region name 
from Koordinates and append that to the given AirBnb data in a separate file'''

import pandas as pd
import requests 
import os
import threading
from tqdm import tqdm
import time

#os.chdir("") # Set working directory here 

tqdm.pandas(desc="Processing rows") # Make a progress bar that applies to pandas functions

KEY = input("What is your API key?: ")
LAYER_ID = "123515" # taken from https://datafinder.stats.govt.nz/layer/123515-statistical-area-2-2026/
INPUT_FILE = "data/processed/christchurch_airbnb_cleaned.csv"
OUTPUT_FILE = "data/processed/test_sa22026.csv"
    

def query(latitude, longitude):
    """
    Query Koordinates using latitude and longitude
    and return both SA22026 code and SA22026 name.
    """
    try:
        if latitude < -90 or latitude > 90:
            raise ValueError(f"Latitude ({latitude}) is out of range")

        if longitude < -180 or longitude > 180:
            raise ValueError(f"Longitude ({longitude}) is out of range")

        request = requests.get(
            f"https://koordinates.com/services/query/v1/vector.json"
            f"?key={KEY}"
            f"&layer={LAYER_ID}"
            f"&x={longitude}"
            f"&y={latitude}"
            f"&max_results=3"
            f"&radius=10000"
            f"&geometry=true"
            f"&with_field_names=true",
            timeout=30
        )

        request.raise_for_status()

        data = request.json()

        features = data["vectorQuery"]["layers"][LAYER_ID]["features"]

        if not features:
            print(
                f"No output for coordinates "
                f"(latitude: {latitude}, longitude: {longitude})"
            )
            return None, None

        properties = features[0]["properties"]

        code = properties["SA22026_V1_00"]
        name = properties["SA22026_V1_00_NAME"]

        return code, name

    except IndexError:
        print(
            f"No output for coordinates "
            f"(latitude: {latitude}, longitude: {longitude})"
        )
        return None, None

    except ValueError as e:
        print(f"Caught error: {e}")
        return None, None

    except requests.RequestException as e:
        print(
            f"Request error for coordinates "
            f"(latitude: {latitude}, longitude: {longitude}): {e}"
        )
        return None, None

    except Exception as e:
        print(
            f"Unexpected error for coordinates "
            f"(latitude: {latitude}, longitude: {longitude}): {e}"
        )
        return None, None
         

def get_sa22026_code_name(df, index, output_dict):
    '''Get the sa22026 code and name for every row in the dataframe.'''

    # initialise columns 'sa22026_code' and 'sa22026_name'
    if "sa22026_code" not in df.columns:
        df["sa22026_code"] = pd.Series(index=df.index, dtype="string")

    if "sa22026_name" not in df.columns:
        df["sa22026_name"] = pd.Series(index=df.index, dtype="string")

    # get the sa22026 code and name
    for row_index, row in tqdm(
        df.iterrows(),
        total=len(df),
        desc=f"Thread {index}"
    ):
        code, name = query(row.latitude, row.longitude)

        df.loc[row_index, "sa22026_code"] = code
        df.loc[row_index, "sa22026_name"] = name
        time.sleep(0.5)

    output_dict[index] = df


def get_df_chunks(df, number_of_chunks):
    '''Split the dataframe into a specified number of chunks.'''

    chunks = []
    chunk_indexes = []

    chunk_size = len(df) // number_of_chunks

    for i in range(number_of_chunks):
        start = i * chunk_size

        if i == number_of_chunks - 1:
            end = len(df)
        else:
            end = (i + 1) * chunk_size

        chunk = df.iloc[start:end].copy()

        if len(chunk) > 0:
            chunks.append(chunk)
            chunk_indexes.append([chunk.index[0], chunk.index[-1]])

    return chunks, chunk_indexes

def main():
    '''Main function'''

    # read the input file you want to append 'sa22026_code' and 'sa22026_name' columns to
    air_bnb_df = pd.read_csv(INPUT_FILE)
    #air_bnb_df = air_bnb_df.head(10)
    df_len = len(air_bnb_df)

    # separate out the file into 5 separate chunks to make 
    chunk_no = 5
    chunks, chunk_indexes = get_df_chunks(air_bnb_df, chunk_no)

    # put the results in a dictionary to ensure the results of the threads are not randomly put in
    results_dict = {}

    # create the threads, execute them and wait until all the threads have completed running
    thread_1 = threading.Thread(target=get_sa22026_code_name, args=(chunks[0], "0", results_dict))
    thread_2 = threading.Thread(target=get_sa22026_code_name, args=(chunks[1], "1", results_dict))
    thread_3 = threading.Thread(target=get_sa22026_code_name, args=(chunks[2], "2", results_dict))
    thread_4 = threading.Thread(target=get_sa22026_code_name, args=(chunks[3], "3", results_dict))
    thread_5 = threading.Thread(target=get_sa22026_code_name, args=(chunks[4], "4", results_dict))

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
    df_combined.to_csv(OUTPUT_FILE, index=False)

