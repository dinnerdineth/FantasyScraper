#scrape daily roster and points
import pandas 
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time



#link to each day
#scoring period goes from 1 - 186
#https://fantasy.espn.com/baseball/team?leagueId=209255785&seasonId=2023&teamId=10&scoringPeriodId=1&statSplit=singleScoringPeriod

def batter_scraper(driver,batters):
  # start_time = time.perf_counter()
  totals_row = False  
  row_num = 1
  while totals_row == False: #check if the row being scraped has the daily total
  
    is_totals_row_object = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[%s]/td[3]/div' % row_num)
    if is_totals_row_object.get_attribute('innerText') == "TOTALS":
      totals_row = True
    else:
      batter_name_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[%s]/td[2]/div/div/div[2]/div/div[1]' %  row_num)
      try:
        batter_name = batter_name_obj.get_attribute('title')
      except NoSuchElementException:
        batter_name = "NaN"
    print(batter_name)
    batters.append(batter_name)
    row_num += 1
    
  # end_time = time.perf_counter()
  # function_run_time = end_time - start_time
  # print("Batter Function took %s seconds to run" % function_run_time)
  


def pitcher_scraper(driver,pitchers):
  # start_time = time.perf_counter()
  totals_row = False  
  row_num = 1
  while totals_row == False: #check if the row being scraped has the daily total
    
    is_totals_row_object = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/table[1]/tbody/tr[%s]/td[3]/div' % row_num)
    #print(is_totals_row_object.get_attribute('innerText'))
    if is_totals_row_object.get_attribute('innerText') == "TOTALS":
      totals_row = True
    else: #get player name and daily points total
      pitcher_name_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/table[1]/tbody/tr[%s]/td[2]/div/div/div[2]/div/div[1]' % row_num)
      try:
        pitcher_name = pitcher_name_obj.get_attribute('title')
      except NoSuchElementException:
        pitcher_name = "NaN"
      
      print(pitcher_name)  
      pitchers.append(pitcher_name)
      row_num += 1
      
  # end_time = time.perf_counter()
  # function_run_time = end_time - start_time
  # print("Pitcher Function took %s seconds to run" % function_run_time)
  
  return pitchers
  

def roster_scraper():
  start_time = time.perf_counter()
  x = 1
  pitchers = []
  batters = []
  #Create for loop to scrape each day
  for x in range(1,2):
    
    url = ("https://fantasy.espn.com/baseball/team?leagueId=209255785&seasonId=2023&teamId=10&scoringPeriodId=%s&statSplit=singleScoringPeriod"% x)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    #driver.implicitly_wait(5)
    
    #identify object to detect page is loaded    
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div[1]/div[2]/div[1]/div/span')))


    #Perform scrape  
    batter_scraper(driver,batters)
    pitcher_scraper(driver,pitchers)

    
    
  print(pitchers)
  print(batters)
  end_time = time.perf_counter()
  function_run_time = end_time - start_time
  print("Scraping Function took %s seconds to run" % function_run_time)
  
  