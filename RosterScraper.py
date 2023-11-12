#scrape daily roster and points
import pandas 
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#link to each day
#scoring period goes from 1 - 186
#https://fantasy.espn.com/baseball/team?leagueId=209255785&seasonId=2023&teamId=10&scoringPeriodId=1&statSplit=singleScoringPeriod

def roster_scraper():
  x = 1
  url = ("https://fantasy.espn.com/baseball/team?leagueId=209255785&seasonId=2023&teamId=10&scoringPeriodId=%s&statSplit=singleScoringPeriod"% x)
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get(url)
  driver.implicitly_wait(30)
  #identify object to detect page is loaded
  #trade_limit_label = driver.find_element(By.NAME,'Trade & Acquisition Limits')
  trade_limit_label =  driver.find_element("xpath",'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/span')
  #print(trade_limit_label)
  wait = WebDriverWait(driver, 20)
  wait.until(lambda d : trade_limit_label.is_displayed())
  
  #create blank list with player names
  players = []
  
  #Get player name
  wait = WebDriverWait(driver, 10)
  
  #players = [title.text for title in wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'jsx-1811044066 player-column__athlete flex')))]
  elements = driver.find_elements(By.CLASS_NAME,"jsx-1811044066 player-column__athlete flex")
  #elements = driver.find_elements("class name","jsx-1811044066 player-column__athlete flex")
  print(elements)
  # for element in elements:
  #   player = element.get_attribute('title')
  #   print(player)
  #   players.append(player)
  
  print(players)
  #div class for player names
  #jsx-1811044066 player-column__athlete flex
  #get title

  
