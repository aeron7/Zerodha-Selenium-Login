import os,sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from selenium import webdriver

#Download ChromeDriver from https://chromedriver.chromium.org/downloads and Put on Same Folder
chromedriver = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver.exe')
os.environ["webdriver.chrome.driver"] = chromedriver
# write your User Id
loginid = ""
# write your Password
password = ""
# write your PIN
loginpin = ""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get('https://kite.zerodha.com')
def loginkite():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"userid"))).send_keys(loginid)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"password"))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"pin"))).send_keys(loginpin)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']"))).click()
loginkite()

#Click on Postions Page
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div[1]/a[4]').click()
time.sleep(5)

#Take Screenshot of the Positions Page
element = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]')
element_png = element.screenshot_as_png
element_png_url =os.path.join(os.path.dirname(os.path.realpath(__file__)), username+'_ss.png')
with open(element_png_url, "wb") as file:
  file.write(element_png)

