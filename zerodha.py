import os,sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from selenium import webdriver

#Download ChromeDriver from https://chromedriver.chromium.org/downloads and Put on Same Folder
chromedriver = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver.exe')
os.environ["webdriver.chrome.driver"] = chromedriver

username=""
password=""
pin=""

driver = webdriver.Chrome(chromedriver)
driver.get("https://kite.zerodha.com")
driver.maximize_window()
time.sleep(5)

username_input = '//*[@id="userid"]'
driver.find_element_by_xpath(username_input).send_keys(username)

password_input = '//*[@id="password"]'
driver.find_element_by_xpath(password_input).send_keys(password)

submit_input = '//*[@id="container"]/div/div/div/form/div[4]/button'
driver.find_element_by_xpath(submit_input).click()
time.sleep(5)

#Pin Part
driver.find_element_by_xpath('//*[@id="pin"]').send_keys(pin)
driver.find_element_by_xpath('//*[@id="container"]/div/div/div/form/div[3]/button').click()
time.sleep(3)

#Click on Postions Page
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div[1]/a[4]').click()
time.sleep(5)

#Take Screenshot of the Positions Page
element = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]')
element_png = element.screenshot_as_png
element_png_url =os.path.join(os.path.dirname(os.path.realpath(__file__)), username+'_ss.png')
with open(element_png_url, "wb") as file:
  file.write(element_png)

