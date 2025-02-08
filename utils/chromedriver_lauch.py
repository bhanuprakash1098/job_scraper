import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils.data_store import set_filters
from utils.get_filters import extract_filters
from utils.linkedin import *

filters_data = extract_filters()
set_filters(filters_data)


def launch_driver():
    filters_df = get_filters()

    # Automatically find the ChromeDriver path
    chrome_driver_path = os.path.abspath("Resources/chromedriver.exe")

    if chrome_driver_path is None:
        raise Exception("ChromeDriver not found. Ensure it is installed and added to PATH.")

    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Opens browser in full-screen mode
    options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection

    # Initialize WebDriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    # Extracting values
    platform = filters_df.get('Platform', [None])[0]

    if platform == 'LinkedIn':
        go_to_linkedin(driver)
    elif platform == 'Handshake':
        pass

    # Close the browser (optional)
    driver.quit()
