from unittest import skip
import pandas as pd
import glob
import os

# merging all the csv files from the solar unit in wandersleben into a single csv file

path = "/Users/mersc/Desktop/Solar_Project/Project_fantastic_five/Data/Solar Wandersleben"

# joining all files that start with "20"
all_files = glob.glob(os.path.join(path, "20*.csv"))

# iterate over the files, seperate where a ";" is and skip erroneous lines
df_from_each_file = (pd.read_csv(f, engine='python', on_bad_lines=skip, sep=';') for f in all_files)

df_merged   = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv( "wandersleben_energy_merged.csv")