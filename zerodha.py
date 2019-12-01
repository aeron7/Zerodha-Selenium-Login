#!/usr/local/bin/python

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
import pdb
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class ZerodhaSelenium( object ):

   def __init__( self ):
      self.timeout = 5
      self.loadCredentials()
      self.driver = webdriver.Chrome()

   def getCssElement( self, cssSelector ):
      '''
      To make sure we wait till the element appears
      '''
      return WebDriverWait( self.driver, self.timeout ).until( EC.presence_of_element_located( ( By.CSS_SELECTOR, cssSelector ) ) )

   def loadCredentials( self ):
      self.username = "your_username"
      self.password = "your_pass"
      self.security = "your_pin"

   def doLogin( self ):
      #let's login
      self.driver.get( "https://kite.zerodha.com/")
      try:
         passwordField = self.getCssElement( "input[placeholder=Password]" )
         print(passwordField)
         passwordField.send_keys( self.password )
         userNameField = self.getCssElement( "input[placeholder='User ID']" )
         print(userNameField)
         userNameField.send_keys( self.username )
         loginButton = self.getCssElement( "button[type=submit]" )
         loginButton.click()

         # 2FA
         form2FA = self.getCssElement( "form.twofa-form" )
         print(form2FA)
         fieldAnswer1 = form2FA.find_element_by_css_selector( "div:nth-child(2) > div > input[type=password]" )
         print(fieldAnswer1)
         buttonSubmit = self.getCssElement( "button[type=submit]" )

         fieldAnswer1.send_keys( self.security)
         buttonSubmit.click()

      except TimeoutException:
         print( "Timeout occurred" )

      pdb.set_trace()
      # close chrome
      self.driver.quit()

if __name__ == "__main__":
   obj = ZerodhaSelenium()
   obj.doLogin()
