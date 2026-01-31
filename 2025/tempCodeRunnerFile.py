def roster_scraper():
  start_time = time.perf_counter()
  x = 1
  #Create blank dataframes for pitchers and batters
  pitchers = pd.DataFrame(columns=['Date','Pitcher','IP','Hits','ER','Walks','Strike Outs','W','L','Saves','Holds','Points'])
  batters = pd.DataFrame(columns = ['Date','Position','Batter','Runs','Total Bases','Walks','Strike Outs','Stolen Bases','Points'])
  #Create for loop to scrape each day
  for x in range(1,196):
    
    url = ("https://fantasy.espn.com/baseball/team?leagueId=909280170&teamId=1&seasonId=2025&scoringPeriodId=%s"% x)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    #driver.implicitly_wait(5)
    
    #identify object to detect page is loaded    
    wait = WebDriverWait(driver, 20)
    #Troubleshooting time out
    print(driver.current_url)
    print(driver.page_source[:2000])

    #End troubleshooting
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.croppable-image img')))
    


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
  