# Load ESPN Website and login
#Then navigate to fantasy baseball page

#import login function
from Login import get_login

#import Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def espn_login():
  
  #get login credentials
  credentials = get_login()
  un = credentials.username
  pw = credentials.password
  
  #Load webpage
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.implicitly_wait(2)
  
  url = "https://www.espn.com/fantasy/"
  driver.get(url)
  
  login_button = driver.find_element("xpath",'//*[@id="sideLogin-left-rail"]/button[2]')
  #login_button = driver.find_element("link text","Log In")
  
  login_button.click()
  
  #enter email
  driver.implicitly_wait(2)
  address_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME,'Email')))
  #address_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[3]/div/div[2]/div/div/form/label/div/label')))
  #address_box = driver.find_element("xpath",'//*[@id="root"]/div[3]/div/div[2]/div/div/form/label')
  address_box.send_keys(un)
  
  continue_button = driver.find_element("xpath",'//*[@id="BtnSubmit"]')
  continue_button.Click()
  
  driver.implicitly_wait(2)
  pw_box = driver.find_element("xpath",'//*[@id="InputPassword"]')
  pw_box.send_keys(pw)
  pw_box.send_keys("[Enter]")
  
  
  
  
  
  
