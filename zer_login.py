# Import necessary modules
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyotp
import json

try:
    # Load the JSON configuration
    with open('zer_login_1.json', 'r') as json_file:
        config = json.load(json_file)

    # Extract configuration values
    username = config["username"]
    password = config["password"]
    totp = config["totp"]

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--force-dark-mode')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--start-maximized')

    # Disable notifications in Chrome
    prefs = {
        "profile.default_content_setting_values.notifications": 2
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://kite.zerodha.com/positions")

    # Locate and interact with web elements
    element1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/form/div[2]/input")
    element1.clear()
    element1.send_keys(username)
    time.sleep(2)

    # (Repeat similar steps for other form fields and buttons)

    # Add an input statement to pause the script
    input("Press Enter to close the program")

    # Quit the WebDriver
    driver.quit()

except Exception as e:
    # Print any exceptions that occur
    print("An error occurred:", e)

    # Add an input statement to pause the script
    input("Press Enter to close the program")
