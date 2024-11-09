# Delete blank rows from CSVs
# Replace blank balues with 0's

import pandas as pd
import numpy as np

def data_cleaner():
  batter_df = pd.read_csv("batters.csv")
  print("Starting batter df has " + str(len(batter_df.index)) + " rows")
  
  pitcher_df = pd.read_csv("pitchers.csv")
  print("Starting pitcher df " + str(len(pitcher_df.index)) + " rows")
  
  #Drop index column from csv to dataframe process
  batter_df.drop('Unnamed: 0',axis=1,inplace=True)
  pitcher_df.drop('Unnamed: 0',axis=1,inplace=True)
  
  
  #sub blank values with NaN
  batter_df['Batter'].replace('', np.nan, inplace=True)
  pitcher_df['Pitcher'].replace('', np.nan, inplace=True)
  
  #remove rows with blank player names
  batter_df.dropna(subset=['Batter'], inplace=True)
  print("batter df without blank names has " + str(len(batter_df.index)) + " rows")
  
  pitcher_df.dropna(subset=['Pitcher'], inplace=True)
  print("pitcher df without blank names has " + str(len(pitcher_df.index)) + " rows")
  
  #Remove rows with blank value for points
  batter_df['Points'].replace('', np.nan, inplace=True)
  batter_df.dropna(subset=['Points'], inplace = True)
  
  pitcher_df['Points'].replace('', np.nan, inplace=True)
  pitcher_df.dropna(subset=['Points'], inplace = True)
  
  #create new CSV files with cleaned data
  batter_df.to_csv("batters_cleaned.csv")
  pitcher_df.to_csv("pitchers_cleaned.csv")