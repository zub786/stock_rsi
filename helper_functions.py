import pandas as pd


def parse_csv(file_path):
   parsed_data = None
   if pd.read_csv(file_path, nrows=1, sep = ';').shape[1] > 1:
      # Use Pandas to parse the CSV file
      parsed_data = pd.read_csv(file_path, sep = ';') # semi_colon_data
   elif pd.read_csv(file_path, nrows=1, sep = ',').shape[1] > 1:
      # Use Pandas to parse the CSV file
      parsed_data = pd.read_csv(file_path, sep = ',') # comma_seprated_data

   # First Col contain 0, 1, 2 and second contains the object of row
   parsed_data_list = [columns_of_file[1] for columns_of_file in parsed_data.iterrows()]
   return parsed_data_list