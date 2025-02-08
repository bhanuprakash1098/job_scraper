import configparser
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.data_store import get_filters


def go_to_linkedin(driver):
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
    time.sleep(3)

    navigate_to_jobs(driver)


def navigate_to_jobs(driver):
    filters_df = get_filters()

    # Extracting values
    job_title = filters_df.get('Job title', [None])[0]  # Extract first value if exists
    location = filters_df.get('Location', [None])[0]
    sort_by = filters_df.get('Sort by', [None])[0]
    date_posted = filters_df.get('Date posted', [None])[0]
    experience_levels = filters_df.get('Experience level', [])  # Keep as list
    job_types = filters_df.get('Job type', [])  # Keep as list
    remotes = filters_df.get('Remote', [])  # Keep as list

    # Click on the navigation menu item
    driver.find_element(By.XPATH, '/html/body/div[6]/header/div/nav/ul/li[3]/a').click()

    # Wait until the show all is clickable
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[contains(@id, 'jobs-search-box-keyword-id-ember')]")))

    # Click inside the search box and enter job title
    search_box.click()
    search_box.send_keys(job_title)

    # Hit Enter to search
    search_box.send_keys(Keys.ENTER)

    # Wait until the location input field is clickable
    location_input = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]")))

    # Click on the location input field to activate it
    location_input.click()

    # Clear any existing text in the input field
    location_input.clear()

    # Enter the desired location (passed as a variable)
    location_input.send_keys(location)

    # Press ENTER to trigger the search or apply the location filter
    location_input.send_keys(Keys.ENTER)

    # Wait until the all filters button is clickable
    all_filters = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='relative mr2']/button")))

    # Click on all filters
    all_filters.click()

    # Applying sort by filter
    driver.find_element(By.XPATH, f"//label[contains(., '{sort_by}')]").click()

    # Applying date posted filter
    driver.find_element(By.XPATH, f"//label[contains(., '{date_posted}')]").click()

    # Applying experience level filter
    for experience_level in experience_levels:
        driver.find_element(By.XPATH, f"//label[contains(., '{experience_level}')]").click()

    # Applying job type filter
    for job_type in job_types:
        driver.find_element(By.XPATH, f"//label[contains(., '{job_type}')]").click()

    # Applying remote filter
    for remote in remotes:
        driver.find_element(By.XPATH, f"//label[contains(., '{remote}')]").click()

    time.sleep(2)

    # Wait until 'Show Results' button is present
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[3]/div/button[2]/span")))

    # Find the element again before clicking
    show_results_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[3]/div/button[2]/span"))
    )
    # Click the button
    show_results_button.click()

    time.sleep(5)
