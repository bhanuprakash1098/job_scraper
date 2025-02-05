import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils.linkedin import *


def launch_driver():
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

    login_page(driver)

    # Close the browser (optional)
    driver.quit()
