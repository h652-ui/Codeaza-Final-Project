import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from Database import dbConnection
import threading

def scrap():
    # Set up logging
    logging.basicConfig(filename='../Logs/requests.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Set up Selenium options
    firefox_options = Options()

    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox(options=firefox_options)

    # Define the URL of the laptop category on Daraz
    url = "https://finance.yahoo.com/lookup"

    # Navigate to the laptop category
    driver.get(url)
    
    rows = driver.find_elements(By.TAG_NAME, 'tr')[1:]
    
    threads = []
    for row in rows:
        symbol = row.find_element(By.CLASS_NAME, 'data-col0').text
        name = row.find_element(By.CLASS_NAME, 'data-col1').text
        lastPrice = row.find_element(By.CLASS_NAME, 'data-col2').text
        change = row.find_element(By.CLASS_NAME, 'data-col3').text
        percentageChange = row.find_element(By.CLASS_NAME, 'data-col4').text
        thread = threading.Thread(target=dbConnection.insert_data, args=(symbol, name, lastPrice, change, percentageChange))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    driver.quit()