# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# gooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooood
class TestTestlogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
# 1
# good but there is alert
  def test_login_with_good_email_and_password(self):
    self.driver.get("https://www.manning.com/")
    self.driver.set_window_size(1552, 880)
    # alert
    self.driver.find_element(By.CSS_SELECTOR, "div.nav-dashboard-button.clickable label[for=\'sign-in\']").click()
    self.driver.get("https://login.manning.com/login?service=https%3A%2F%2Fwww.manning.com%2Flogin%2Fcas")
    time.sleep(1)
    self.driver.find_element(By.ID, "username-sign-in").send_keys("reatk193@gmail.com")
    self.driver.find_element(By.ID, "password-sign-in").click()
    self.driver.find_element(By.ID, "password-sign-in").send_keys("kk20012024")
    self.driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    assert self.driver.current_url == "https://www.manning.com/dashboard/index"
    # self.driver.find_element(By.CSS_SELECTOR, ".products-header").click()
    # element = self.driver.find_element(By.CSS_SELECTOR, ".products-header")
    # actions = ActionChains(self.driver)
    # actions.double_click(element).perform()
    # time.sleep(2)
    # self.driver.find_element(By.CSS_SELECTOR, ".nav-dashboard-button > label").click()
    # time.sleep(2)
    # self.driver.find_element(By.CSS_SELECTOR, ".btn-full-width").click()
    time.sleep(2)
    self.driver.close()
# 2
#  good but there is alert 
  def test_login_with_wrong_password(self):
    self.driver.get("https://www.manning.com/")
    self.driver.set_window_size(1552, 880)
    self.driver.find_element(By.CSS_SELECTOR, "div.nav-dashboard-button.clickable label[for=\'sign-in\']").click()
    self.driver.get("https://login.manning.com/login?service=https%3A%2F%2Fwww.manning.com%2Flogin%2Fcas")
    time.sleep(1)
    self.driver.find_element(By.ID, "username-sign-in").send_keys("reatk193@gmail.com")
    self.driver.find_element(By.ID, "password-sign-in").click()
    self.driver.find_element(By.ID, "password-sign-in").send_keys("123456789")
    self.driver.find_element(By.NAME, "submit").click()
    error_message = self.driver.find_element(By.CSS_SELECTOR, "#msg li").text
    assert "Authentication attempt has failed" in error_message
    time.sleep(2)
    self.driver.close()

# 3
# good but there is alert
  def test_login_with_empty_password(self):
    self.driver.get("https://www.manning.com/")
    self.driver.set_window_size(1552, 880)
    self.driver.find_element(By.CSS_SELECTOR, "div.nav-dashboard-button.clickable label[for=\'sign-in\']").click()
    self.driver.get("https://login.manning.com/login?service=https%3A%2F%2Fwww.manning.com%2Flogin%2Fcas")
    time.sleep(1)
    self.driver.find_element(By.ID, "username-sign-in").send_keys("reatk193@gmail.com")
    self.driver.find_element(By.ID, "password-sign-in").click()
    self.driver.find_element(By.ID, "password-sign-in").send_keys("")
    self.driver.find_element(By.NAME, "submit").click()
    msg = self.driver.find_element(By.ID, "password-sign-in").get_attribute("validationMessage")
    assert  msg == "Please fill in this field."
    time.sleep(1)
    self.driver.close()

# 4
# good but there is alert
  def test_login_with_unregistered_email(self):
    self.driver.get("https://www.manning.com/")
    self.driver.set_window_size(1552, 880)
    self.driver.find_element(By.CSS_SELECTOR, "div.nav-dashboard-button.clickable label[for=\'sign-in\']").click()
    self.driver.get("https://login.manning.com/login?service=https%3A%2F%2Fwww.manning.com%2Flogin%2Fcas")
    time.sleep(1)
    self.driver.find_element(By.ID, "username-sign-in").send_keys("kalemat.reat197@gmail.com")
    self.driver.find_element(By.ID, "password-sign-in").click()
    self.driver.find_element(By.ID, "password-sign-in").send_keys("123456789")
    time.sleep(1)
    self.driver.find_element(By.NAME, "submit").click()
    error_message = self.driver.find_element(By.CSS_SELECTOR, "#msg li").text
    assert "Your account is not recognized and cannot login at this time." in error_message
    self.driver.close()









  