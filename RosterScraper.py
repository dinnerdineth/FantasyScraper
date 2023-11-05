#scrape daily roster and points
import pandas 
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


#link to each day
#scoring period goes from 1 - 186
#https://fantasy.espn.com/baseball/team?leagueId=209255785&seasonId=2023&teamId=10&scoringPeriodId=1&statSplit=singleScoringPeriod

def roster_scraper():
  x = 1
  url = ("https://fantasy.espn.com/baseball/team?leagueId=209255785&seasonId=2023&teamId=10&scoringPeriodId=%s&statSplit=singleScoringPeriod"% x)
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.implicitly_wait(2)
  driver.get(url)
  driver.implicitly_wait(2)
  
  #create blank list with player names
  players = []
  
  #Get player name
  elements = driver.find_elements(By.CLASS_NAME,"jsx-1811044066 player-column__athlete flex")
  
  for element in elements:
    player = element.get_attribute('title')
    print(player)
    players.append(player)
  
  print(players)
  #div class for player names
  #jsx-1811044066 player-column__athlete flex
  #get title

  
