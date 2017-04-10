import pandas as pd
from os.path import split
import mypkg

def clean_data(df):
  df.drop([df.columns[0]], axis = 1, inplace = True)
  print("You can see here the dataframe header:\n", df.head())
  return df


