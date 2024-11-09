#scrape daily roster and points
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) #suppress the warning about append getting removed in the future
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time



#link to each day
#scoring period goes from 1 - 186
#https://fantasy.espn.com/baseball/team?leagueId=1561118529&teamId=8&seasonId=2024&scoringPeriodId=1

def batter_scraper(driver,batters):
  # start_time = time.perf_counter()
  totals_row = False  
  row_num = 1
  while totals_row == False: #check if the row being scraped has the daily total
  
    is_totals_row_object = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[%s]/td[3]/div' % row_num)
    if is_totals_row_object.get_attribute('innerText') == "TOTALS":
      totals_row = True
      break
    else:
      batter_dict = {'Date' : '','Position': '', 'Batter' : '','Runs' : 0,'Total Bases' : 0,'Walks' : 0,'Strike Outs' : 0,'Stolen Bases' : 0,'Points' : 0}
      
      try:
        batter_name_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[%s]/td[2]/div/div/div[2]/div/div[1]' %  row_num)
        batter_name = batter_name_obj.get_attribute('title')
        
      except NoSuchElementException:
        batter_name = "NaN"
        
        
    if batter_name != "NaN": #if valid player get other stats
      batter_dict['Batter'] = batter_name
      
      date_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/thead/tr[1]/th[2]')
      date = date_obj.get_attribute('innerText')
      batter_dict['Date'] = date
      
      pos_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/tbody/tr[%s]/td[1]/div' % row_num)
      pos = pos_obj.get_attribute('innerText')
      batter_dict['Position'] = pos
      
      runs_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/div/div[2]/table/tbody/tr[%s]/td[1]/div' % row_num)
      runs = runs_obj.get_attribute('innerText')
      batter_dict['Runs'] = runs
      
      total_base_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/div/div[2]/table/tbody/tr[%s]/td[2]/div' % row_num)
      total_bases = total_base_obj.get_attribute('innerText')
      batter_dict['Total Bases'] = total_bases
      
      walks_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/div/div[2]/table/tbody/tr[%s]/td[3]/div' % row_num)
      walks = walks_obj.get_attribute('innerText')
      batter_dict['Walks'] = walks
      
      ks_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/div/div[2]/table/tbody/tr[%s]/td[4]/div' % row_num)
      ks = ks_obj.get_attribute('innerText')
      batter_dict['Strike Outs'] = ks

      sb_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/div/div[2]/table/tbody/tr[%s]/td[5]/div' % row_num)
      sb = sb_obj.get_attribute('innerText')
      batter_dict['Stolen Bases'] = sb
      
      points_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[2]/tbody/tr[%s]/td/div' % row_num)
      points = points_obj.get_attribute('title')
      points = points.strip(" points")
      batter_dict['Points'] = points
        
        #print(batters)
        #print(batter_dict)
     
        
    batters = batters.append(batter_dict, ignore_index=True)
    row_num += 1
  #print(batters)
  return batters
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
      break
    else: #get player name and daily points total
      pitcher_dict = {'Date' : '', 'Pitcher' : '', 'IP' : 0.0, 'Hits' : 0, 'ER': 0, 'Walks' : 0, 'Strike Outs' : 0, 'W' : 0, 'L' : 0, 'Saves' : 0, 'Holds': 0, 'Points': 0}
      
      try:
        pitcher_name_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/table[1]/tbody/tr[%s]/td[2]/div/div/div[2]/div/div[1]' % row_num)
        pitcher_name = pitcher_name_obj.get_attribute('title')
        
      except NoSuchElementException:
        pitcher_name = "NaN"
        
        
    if pitcher_name != "NaN":
      pitcher_dict['Pitcher'] = pitcher_name
      
      date_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[1]/div/div/table[1]/thead/tr[1]/th[2]')
      date = date_obj.get_attribute('innerText')
      pitcher_dict['Date'] = date
      
      ip_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[%s]/td[1]/div' % row_num)
      ip = ip_obj.get_attribute('innerText')
      pitcher_dict['IP'] = ip
      
      hits_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[%s]/td[2]/div' % row_num)
      hits = hits_obj.get_attribute('innerText')
      pitcher_dict['Hits'] = hits
      
      er_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[%s]/td[3]/div' % row_num)
      er = er_obj.get_attribute('innerText')
      pitcher_dict['ER'] = er
      
      walks_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[%s]/td[4]/div' % row_num)
      walks = walks_obj.get_attribute('innerText')
      pitcher_dict['Walks'] = walks
      
      ks_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[%s]/td[5]/div' % row_num)
      ks = ks_obj.get_attribute('innerText')
      pitcher_dict['Strike Outs'] = ks
      
      wins_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[%s]/td[6]/div' % row_num)
      wins = wins_obj.get_attribute('innerText')
      pitcher_dict['W'] = wins
      
      loss_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[%s]/td[7]/div' % row_num)
      loss = loss_obj.get_attribute('innerText')
      pitcher_dict['L'] = loss
      
      saves_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[%s]/td[8]/div' % row_num)
      saves = saves_obj.get_attribute('innerText')
      pitcher_dict['Saves'] = saves
      
      hold_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/table/tbody/tr[%s]/td[9]/div' % row_num)
      hold = hold_obj.get_attribute('innerText')
      pitcher_dict['Holds'] = hold
      
      points_obj = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div[2]/div/div/table[2]/tbody/tr[%s]/td/div' % row_num)
      points = points_obj.get_attribute('title')
      points = points.strip(" points")
      pitcher_dict['Points'] = points
      
    pitchers = pitchers.append(pitcher_dict,ignore_index=True)
    row_num += 1
      
  # end_time = time.perf_counter()
  # function_run_time = end_time - start_time
  # print("Pitcher Function took %s seconds to run" % function_run_time)
  
  #print(pitchers)
  return pitchers
  

def roster_scraper():
  start_time = time.perf_counter()
  x = 1
  #Create blank dataframes for pitchers and batters
  pitchers = pd.DataFrame(columns=['Date','Pitcher','IP','Hits','ER','Walks','Strike Outs','W','L','Saves','Holds','Points'])
  batters = pd.DataFrame(columns = ['Date','Position','Batter','Runs','Total Bases','Walks','Strike Outs','Stolen Bases','Points'])
  #Create for loop to scrape each day
  for x in range(1,195):
    
    url = ("https://fantasy.espn.com/baseball/team?leagueId=1561118529&teamId=8&seasonId=2024&scoringPeriodId=%s&statSplit=singleScoringPeriod"% x)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    #driver.implicitly_wait(5)
    
    #identify object to detect page is loaded    
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/span')))


    #Perform scrape  
    #batters = batters.append(batter_scraper(driver,batters),ignore_index=True)
    #pitchers = pitchers.append(pitcher_scraper(driver,pitchers),ignore_index=True)
    batters = batter_scraper(driver, batters)
    pitchers = pitcher_scraper(driver, pitchers)
    print(x)

    
  
  batters.to_csv("batters.csv")
  pitchers.to_csv("pitchers.csv")
  print(pitchers)
  print(batters)
  end_time = time.perf_counter()
  function_run_time = end_time - start_time
  print("Scraping Function took %s seconds to run" % function_run_time)
  
  
