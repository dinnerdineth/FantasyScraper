#Testing using different scraping methods

import pandas 
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#library for no such element exception
from selenium.common.exceptions import NoSuchElementException


#Load website..this is constant
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

#Scrape 1 player only - position player
adley_object = driver.find_element(By.XPATH,'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[1]/td[2]/div/div/div[2]/div/div[1]') #picked up correct object
#adley_object = driver.find_element(By.CLASS_NAME,'jsx-1811044066 player-column__athlete flex')
adley_name = adley_object.get_attribute('title')
#print(adley_object)
print(adley_name)

#Scrape 1 player only - pitcher
sandy_object = driver.find_element(By.XPATH,'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/table[1]/tbody/tr[1]/td[2]/div/div/div[2]/div/div[1]')
sandy_name = sandy_object.get_attribute('title')
print(sandy_name)

#Attempt to scrape if row has no player name
try:
  blank_object = driver.find_element(By.XPATH,'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/table[1]/tbody/tr[8]/td[2]/div/div/div[2]/div/div[1]') #Jhoan Druan + 1 row
  blank_name = blank_object.get_attribute('title')
except NoSuchElementException:
  blank_name = "NaN"  
print(blank_name)

#Comparing xpaths for position and name
#Row 1 = position
#//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[11]/td[1]/div

#Row 2 = Name
#//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[11]/td[2]/div/div/div[2]/div/div[1]

driver.quit()

def pos_batter_scraper(driver,batters):
  catcher = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[1]/td[1]/div')
  print(catcher.get_attribute('title'))
  fst_bse = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[2]/td[1]/div')
  print(fst_bse.get_attribute('title'))
  
  #row number is controlled by tr
  
  catcher_name = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[1]/td[2]/div/div/div[2]/div/div[1]')
  print(catcher_name.get_attribute('title'))
  fst_bse_name = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[2]/td[2]/div/div/div[2]/div/div[1]')
  print(fst_bse_name.get_attribute('title'))
  snd_bse_name = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[3]/td[2]/div/div/div[2]/div/div[1]')
  print(snd_bse_name.get_attribute('title'))
  
  #Player name column is controlled by td
  
  catcher_points = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[2]/tbody/tr[1]/td/div').get_attribute('title')
  catcher_points_val = catcher_points.strip(" points")
  print(catcher_points_val)
  
  fst_bse_points = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[2]/tbody/tr[2]/td/div').get_attribute('title')
  fst_bse_points_val = fst_bse_points.strip(" points")
  print(fst_bse_points_val)
  #print(fst_bse_points.get_attribute('title'))
  
  #Table 2, TR changes row number
  
def pos_pitcher_scraper(driver,pitchers):
  pitcher_one_object = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/table[1]/tbody/tr[1]/td[1]/div')
  pitcher_one_title = pitcher_one_object.get_attribute('title')
  print(pitcher_one_title)
  pitcher_two_object = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/table[1]/tbody/tr[2]/td[1]/div')
  print(pitcher_two_object.get_attribute('title'))
  #Tr value changes row
      
  pitcher_one_name_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/table[1]/tbody/tr[1]/td[2]/div/div/div[2]/div/div[1]')
  print(pitcher_one_name_obj.get_attribute('title'))
  pitcher_two_name_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/table[1]/tbody/tr[2]/td[2]/div/div/div[2]/div/div[1]')
  print(pitcher_two_name_obj.get_attribute('title'))
  
  il_pitcher_one_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/table[1]/tbody/tr[9]/td[1]/div')
  print(il_pitcher_one_obj.get_attribute('title'))
  
  #for IL players need to get name of row x column 1 and check for title
  # or
  #check for blank row and end loop
  # or check for totals title
  totals_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/table[1]/tbody/tr[8]/td[3]/div')
  print(totals_obj.get_attribute('title'))
  #td 3


#Blank batter - scoring period 93
#Blank pitcher - scoring period 54