import pytest
import time
import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# 5
class Test_login(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    # self.driver = webdriver.Firefox()
    self.driver.get("https://www.manning.com/")
    self.driver.set_window_size(1552, 880)
    try:
      cancel_button = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.ID, "onesignal-slidedown-cancel-button")))
      cancel_button.click()
      print("Alert appeared and was handled.")
    except TimeoutException:
        print("No alert appeared; continuing with the test.")
    except Exception as e:
        print(f"An unexpected exception occurred: {e}")
        print("The alert was not handled properly.")
    self.vars = {}
  def teardown_method(self, method):
    self.driver.quit()

# 1 /subTest 
  def test_login_form_visibility(self):
      WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.nav-dashboard-button.clickable label[for='sign-in']"))).click()
      username_field = self.driver.find_element(By.ID, "username-sign-in")
      password_field = self.driver.find_element(By.ID, "password-sign-in")
      login_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.NAME, "submit")))
      time.sleep(1)
      with self.subTest("username_field"):
        assert username_field.is_displayed(), "First Name field is not visible"
      with self.subTest("password_field"):
        assert password_field.is_displayed(), "Password field is not visible"
      with self.subTest("login_button"):
        assert login_button.is_displayed(), "Create Account button is not visible"
      self.driver.close()
# 2
  def test_good_email_and_password(self):
    self.driver.find_element(By.CSS_SELECTOR, "div.nav-dashboard-button.clickable label[for='sign-in']").click()
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username-sign-in"))).send_keys("kalemat2001k@gmail.com")
    password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password-sign-in")))
    password_field.click()
    password_field.send_keys("k1234567890")
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
    WebDriverWait(self.driver, 10).until(EC.url_to_be("https://www.manning.com/dashboard/index"))
    assert self.driver.current_url == "https://www.manning.com/dashboard/index"
    self.driver.close()
# 3
  def test_wrong_password(self):
    self.driver.find_element(By.CSS_SELECTOR, "div.nav-dashboard-button.clickable label[for='sign-in']").click()
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username-sign-in"))).send_keys("kalemat2001k@gmail.com")
    password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password-sign-in")))
    password_field.click()
    password_field.send_keys("88888 ")
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
    error_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#msg li"))).text
    assert "Authentication attempt has failed" in error_message
    time.sleep(1)
    self.driver.close()
# 4
  def test_empty_password(self):
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.nav-dashboard-button.clickable label[for='sign-in']"))).click()
    self.driver.get("https://login.manning.com/login?service=https%3A%2F%2Fwww.manning.com%2Flogin%2Fcas")
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username-sign-in"))).send_keys("kalemat2001k@gmail.com")
    password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password-sign-in")))
    password_field.click()
    password_field.send_keys("")  # empty
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
    validation_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password-sign-in"))).get_attribute("validationMessage")
    assert validation_message == "Please fill in this field.", f"Unexpected validation message: {validation_message}"
    time.sleep(1)
    self.driver.close()
# 5
  def test_unregistered_email(self):
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.nav-dashboard-button.clickable label[for='sign-in']"))).click()
    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username-sign-in"))).send_keys("kalemat.reat197@gmail.com")
    password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password-sign-in")))
    password_field.click()
    password_field.send_keys("123456789")
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
    error_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#msg li"))).text
    assert "Your account is not recognized and cannot login at this time." in error_message
    time.sleep(1)
    self.driver.close()


  





  
