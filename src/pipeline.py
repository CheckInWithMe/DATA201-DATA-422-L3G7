import deliverable_3 as d3

folder_path = "data/raw"        # Change the working directory in folder_path if required.
output_file_path = "data/processed/christchurch_data.csv"

#processing airbnb data
combined_raw_data = d3.combine_raw_data(folder_path)
christchurch_data = d3.filter_and_save_christchurch(combined_raw_data, output_file_path)
d3.christchurch_data_summary(christchurch_data)

#histogram of airbnb prices in christchurch
d3.display_data(christchurch_data)