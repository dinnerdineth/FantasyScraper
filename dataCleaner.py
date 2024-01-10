# Delete blank rows from CSVs
# Replace blank balues with 0's

import pandas as pd


def data_cleaner():
  batter_df = pd.read_csv("batters.csv")
  print("Starting batter df has " + str(len(batter_df.index)) + " rows")
  
  pitcher_df = pd.read_csv("pitchers.csv")
  print("Starting pitcher df " + str(len(pitcher_df.index)) + " rows")
  
  #remove rows with blank player names
  batter_df = batter_df[batter_df['Batter'] != '']
  print("batter df without blank names has " + str(len(batter_df.index)) + " rows")
  
  pitcher_df = pitcher_df[pitcher_df['Pitcher'] != '']
  print("pitcher df without blank names has " + str(len(pitcher_df.index)) + " rows")