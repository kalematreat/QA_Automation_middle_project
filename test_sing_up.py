import pytest
import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#4/subTest
class Test_sing_up(unittest.TestCase):
  def setup_method(self, method):
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
# 1
  def test_existing_email(self):
    # tooltip/validationMessage
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.nav-dashboard-button.clickable label[for='sign-in']"))).click()
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "showRegistration"))).click()
    first_name_input = self.driver.find_element(By.ID, "firstName")
    first_name_input.send_keys("kaleamt")
    last_name_input = self.driver.find_element(By.ID, "lastName")
    last_name_input.send_keys("reat")
    email_input = self.driver.find_element(By.ID, "username")
    email_input.send_keys("kalematreat@gmail.com")
    password_input = self.driver.find_element(By.ID, "password")
    password_input.send_keys("kk20242025")
    submit_button = self.driver.find_element(By.NAME, "signInBtn")
    submit_button.click()
    self.driver.get_screenshot_as_file("message_email_already_exists_!!.png")
    msg = self.driver.find_element(By.ID, "username").get_attribute("validationMessage")
    assert  msg == "An account with this email address already exists. Please try signing in or request a password reset email."
    time.sleep(1)
    self.driver.close()
# 2 /subTest
  def test_registration_form_visibility(self):
      WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.nav-dashboard-button.clickable label[for='sign-in']"))).click()
      time.sleep(1)
      WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "showRegistration"))).click()
      time.sleep(1)
      first_name_field = self.driver.find_element(By.XPATH, "//input[@id='firstName']")
      last_name_field = self.driver.find_element(By.XPATH, "//input[@id='lastName']")
      email_field = self.driver.find_element(By.XPATH, "//input[@id='username']")
      password_field = self.driver.find_element(By.XPATH, "//input[@id='password']")
      create_account_button = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='create account']")))
      with self.subTest("first_name_field"):
        assert first_name_field.is_displayed(), "First Name field is not visible"
      with self.subTest("last_name_field"):
        assert last_name_field.is_displayed(), "Last Name field is not visible"
      with self.subTest("email_field"):
        assert email_field.is_displayed(), "Email field is not visible"
      with self.subTest("password_field"):
        assert password_field.is_displayed(), "Password field is not visible"
      with self.subTest("create_account_button"):
        assert create_account_button.is_displayed(), "Create Account button is not visible"
      self.driver.close()
# good 3 incorrectly email --> kalematreat@
  def test_incorrectly_email_1(self):
      WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.nav-dashboard-button.clickable label[for='sign-in']"))).click()
      WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "showRegistration"))).click()
      first_name_input = self.driver.find_element(By.ID, "firstName")
      first_name_input.send_keys("kaleamt")
      last_name_input = self.driver.find_element(By.ID, "lastName")
      last_name_input.send_keys("reat")
      email_input = self.driver.find_element(By.ID, "username")
      email_input.send_keys("kalematreat@")
      password_input = self.driver.find_element(By.ID, "password")
      password_input.send_keys("kk20242025")
      time.sleep(1)
      submit_button = self.driver.find_element(By.NAME, "signInBtn")
      submit_button.click()
      # self.driver.get_screenshot_as_file("incorrectly_email.png")
      msg = self.driver.find_element(By.ID, "username").get_attribute("validationMessage")
      assert  msg == "Please enter a part following '@'. 'kalematreat@' is incomplete."
      time.sleep(1)
      self.driver.close()
# bad 4 incorrectly email --> kalemat.try@gml.cm / chang the email!!
  def test_incorrectly_email_2(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.nav-dashboard-button.clickable label[for='sign-in']"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "showRegistration"))).click()
        first_name_input = self.driver.find_element(By.ID, "firstName")
        first_name_input.send_keys("kaleamt")
        last_name_input = self.driver.find_element(By.ID, "lastName")
        last_name_input.send_keys("reat")
        email_input = self.driver.find_element(By.ID, "username")
        email_input.send_keys("userqas@gml.cm")
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("qa20242025")
        submit_button = self.driver.find_element(By.NAME, "signInBtn")
        submit_button.click()
        time.sleep(1)
        self.driver.get_screenshot_as_file("incorrectly_email_@gml.cm.png")
        msg = self.driver.find_element(By.ID, "username").get_attribute("validationMessage")
        assert  msg == "Please enter a valid email address"
        time.sleep(1)
        self.driver.close()

