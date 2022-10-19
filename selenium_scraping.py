
# chrome driver
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

# waiting
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# others
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd  

DRIVER_PATH = r"/Users/linhvu/Desktop/CA Projects/Web Scraping/chromedriver"
# find it at chrome://version
USER_DATA_DIR = r'/Users/linhvu/Library/Application Support/Google/Chrome/User Data/Profile 1'

def open_chrome_new():
    options = ChromeOptions() 
    options.add_argument(f"user-data-dir={USER_DATA_DIR}") #Path to chrome profile
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

    driver.get('https://tgif-website.netlify.app/house_data.html')
   
    try:

        wait = WebDriverWait(driver, 10)
        elements = wait.until(EC.presence_of_element_located((By.ID , "table-rows"))).find_elements_by_css_selector("tr>td>a")
        # print(elements)
        list_names = []
        list_urls = []
        for element in elements:
            print(element.text, element.get_attribute("href"))
            list_names.append(element.text)
            list_urls.append(element.get_attribute("href"))
        # dictionary of lists  
        dict = {'name': list_names, 'website': list_urls}  
            
        df = pd.DataFrame(dict) 
        
        # saving the dataframe 
        df.to_csv('./result.csv') 
       
    finally:
        driver.quit()
    
open_chrome_new()


def open_chrome():
    options = webdriver.ChromeOptions() 
    options.add_argument(f"user-data-dir={USER_DATA_DIR}") #Path to your chrome profile
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
    driver.get('https://tgif-website.netlify.app/house_data.html')
    # not working if we don't wait
    elements = driver.find_element_by_id("table-rows").find_elements_by_css_selector("tr>td>a")
    for element in elements:
            print(element.text, element.get_attribute("href"))
    return driver
#open_chrome()

def search_on_google():
    options = webdriver.ChromeOptions() 
    options.add_argument(f"user-data-dir={USER_DATA_DIR}") #Path to  chrome profile
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get('https://www.google.com/')

    try:
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.presence_of_element_located((By.ID , "CXQnmb"))).find_element_by_css_selector("#L2AGLb")
        time.sleep(2)
        button.click()
        searchbar = driver.find_element_by_name("q")
        print(searchbar)

        searchbar.click()
        time.sleep(2)
        searchbar.clear() 
        searchbar.send_keys("code academy berlin")
        time.sleep(2)
        searchbar.send_keys(Keys.RETURN)
    finally:
        driver.quit()


#search_on_google()