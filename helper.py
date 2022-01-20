from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


def init_driver(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver.get(url)
    return driver


def scroll_to_bottom(selenium_driver):
    y = 1000
    for timer in range(0,10):
        selenium_driver.execute_script(f"window.scrollTo(0, {str(y)}")
        y += 1000  
        time.sleep(1)
        print("Waiting has ended")        


def get_all_db_entries(mongo_db):
    return mongo_db.find({}, {"_id": 1, "name": 1, "link": 1})
