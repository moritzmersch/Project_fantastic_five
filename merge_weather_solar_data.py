from unicodedata import decimal
import pandas as pd
from pandas_profiling import ProfileReport



df1 = pd.read_csv(r"C:\Users\mersc\Desktop\Solar_Project\Project_fantastic_five\wandersleben_energy_merged.csv", index_col=0, decimal=",")
df2 = pd.read_csv(r"C:\Users\mersc\Desktop\Solar_Project\Project_fantastic_five\Data\Weather_Wandersleben.csv")

  
# overwriting data after changing format
df1["time"]= pd.to_datetime(df1["time"])
df2["time"]= pd.to_datetime(df2["time"])

#df1["PVA Wandersleben / Gesamtertrag / Zaehleraenderung  [kWh]"] = pd.to_numeric(df1['PVA Wandersleben / Gesamtertrag / Zaehleraenderung  [kWh]'])
  

# Merge the two dataframes, using _ID column as key
df3 = pd.merge(df1, df2, on = ['time'])
df3.set_index('time', inplace = True)

# Write it to a new CSV file
df3.to_csv('dataset_wandersleben.csv')

# doing a first analysis using pandas profiling 
profile = ProfileReport(df3, title="Pandas Profiling Report")
profile.to_file("dataset_wandersleben.html")
