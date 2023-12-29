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
  #batters = []
  for i in range(1,15):
    start_time = time.perf_counter()
    try:
      player_name_object =driver.find_element(By.XPATH,'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[%s]/td[2]/div/div/div[2]/div/div[1]' % i)
      player_name = player_name_object.get_attribute('title')
    except NoSuchElementException:
      player_name = "NaN"
    batters.append(player_name)
    
    end_time = time.perf_counter()
    for_loop_runtime = end_time - start_time
    print("%s took %s to scrape" % (player_name,for_loop_runtime))
  return batters




def pitcher_scraper(driver,pitchers):
  #pitchers = []
  for i in range(1,15):
    start_time = time.perf_counter()
    try:
      player_name_object = driver.find_element(By.XPATH,'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/table[1]/tbody/tr[%s]/td[2]/div/div/div[2]/div/div[1]' % i)
      player_name = player_name_object.get_attribute('title')
    except NoSuchElementException:
      player_name = "NaN"
    pitchers.append(player_name)
    
    end_time = time.perf_counter()
    for_loop_runtime = end_time - start_time
    print("%s took %s to scrape" % (player_name,for_loop_runtime))
  return pitchers
      

def batter_scraper_by_pos(driver,batters):
  positions = ['C','1B','2B','3B','SS','OF','OF','OF','UTIL']
  catcher_row = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[1]/td[1]/div')
  catcher_name = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[1]/td[2]/div/div/div[2]/div/div[1]')
  catcher_opp = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[1]/td[3]/div/div/a/span')
  
  #Based off the above rows the td[x] is the column number

def roster_scraper():
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
    #trade_limit_label =  driver.find_element("xpath",'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/span')
    #wait.until(lambda d : trade_limit_label.is_displayed())

    #Perform scrape  
    batter_scraper(driver,batters)
    pitcher_scraper(driver,pitchers)
    print(x)  
    
  print(pitchers)
  print(batters)
  
def pos_roster_scraper():
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
    pos_batter_scraper(driver, batters)
    
    #Close webdriver
    driver.quit()  
  