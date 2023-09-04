from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--force-dark-mode')
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--window-size=1280,720")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://kite.zerodha.com/positions")

zerodha_username = "your_username"
zerodha_password = "your_oassword"
zerodha_totp="IZEKKYSVDHCQ2DQ445XIQYIS3SA444L6"


element1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/form/div[2]/input")
element1.clear()
element1.send_keys(zerodha_username)
time.sleep(2)

element2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/form/div[3]/input")
element2.clear()
element2.send_keys(zerodha_password)
time.sleep(2)

element3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/form/div[4]/button")
element3.click()
time.sleep(5)

zerodha_totp = pyotp.parse_uri('otpauth://totp/Zerodha:'+str(zerodha_username)+'?algorithm=SHA1&digits=6&issuer=Zerodha&period=30&secret='+zerodha_totp+'')
zerodha_totp = zerodha_totp.now().zfill(6)

element4 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/form/div[1]/input")
element4.clear()
element4.send_keys(zerodha_totp)
time.sleep(2)

# element5 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/form/div[2]/button")
# element5.click()
# time.sleep(5)

element6 = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/div[3]/div/div/div/button")
element6.click()
time.sleep(5)


# Format the datetime as a string (e.g., "YYYY-MM-DD_HH-MM-SS")
formatted_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

file_path='kite_'+str(zerodha_username)+'_screenshot_'+str(formatted_datetime)+'.png'
driver.save_screenshot(file_path)

driver.quit()

print(file_path)
