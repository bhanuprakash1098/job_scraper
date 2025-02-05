import configparser
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def login_page(driver):
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('Resources/config.ini')

    # Access values from the LinkedIn section
    username = config['LinkedIn']['username']
    password = config['LinkedIn']['password']

    # Navigate to LinkedIn
    driver.get("https://www.linkedin.com/login")

    # Locate username and password fields using XPath and enter credentials
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)

    # Locate and click "Sign in" button using Link Text
    driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[4]/button').click()

    # Wait for a few seconds to ensure login attempt
    time.sleep(5)

    navigate_to_jobs(driver)

def navigate_to_jobs(driver):
    # Click on the navigation menu item
    driver.find_element(By.XPATH, '/html/body/div[6]/header/div/nav/ul/li[3]/a').click()

    # Wait until the search box is clickable
    wait = WebDriverWait(driver, 20)
    search_box = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[contains(@id, 'jobs-search-box-keyword-id-ember')]")))

    # Click inside the search box and enter job title
    search_box.click()
    search_box.send_keys('Software Engineer')

    # Hit Enter to search
    search_box.send_keys(Keys.ENTER)

    # Wait until the all filters button is clickable
    all_filters = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='relative mr2']/button")))

    # Click on all filters
    all_filters.click()
    time.sleep(5)
