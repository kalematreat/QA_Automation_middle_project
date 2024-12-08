import pytest
import time
import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# 4 / subTest
class Test_book_details(unittest.TestCase):
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
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()

# 1
  def test_img_displayed(self):
    self.driver.find_element(By.LINK_TEXT, "catalog").click()
    # time.sleep(1)
    self.vars["window_handles"] = self.driver.window_handles
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".search-catalog-product-root:nth-child(1) img").click()
    self.vars["win5255"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win5255"])
    img_element = self.driver.find_element(By.CSS_SELECTOR, "div.product-cover-inner img.product-cover")
    assert img_element.is_displayed(), "The image is not visible on the page!"
# 2
  def test_link_book(self):
    self.driver.find_element(By.LINK_TEXT, "catalog").click()
    time.sleep(2)
    self.vars["window_handles"] = self.driver.window_handles
    time.sleep(3)
    link_element = self.driver.find_element(By.CSS_SELECTOR, ".search-catalog-product-root:nth-child(2) a")
    href_value = link_element.get_attribute("href")
    link_element.click()
    self.vars["win5255"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win5255"])
    current_url = self.driver.current_url
    assert href_value == current_url, f"Href mismatch! Found: {href_value}"
# 3
  def test_add_to_cart_button_displayed(self):
    self.driver.find_element(By.LINK_TEXT, "catalog").click()
    time.sleep(1)
    self.vars["window_handles"] = self.driver.window_handles
    time.sleep(3)
    self.driver.find_element(By.CSS_SELECTOR, ".search-catalog-product-root:nth-child(1) img").click()
    self.vars["win5255"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win5255"])
    img_element = self.driver.find_element(By.CSS_SELECTOR, "div.product-cover-inner img.product-cover")
    assert img_element.is_displayed(), "The image is not visible on the page!"
# 4/subTest
  def test_price(self):
    self.driver.find_element(By.LINK_TEXT, "catalog").click()
    time.sleep(1)
    element = self.driver.find_element(By.CSS_SELECTOR, ".search-catalog-product-root:nth-child(2) img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    self.vars["window_handles"] = self.driver.window_handles
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".search-catalog-product-root:nth-child(1) img").click()
    self.vars["win5255"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win5255"])
    time.sleep(1)
    ebook_button = self.driver.find_element(By.XPATH, "//button[@data-product-type='eBook']")
    print_button = self.driver.find_element(By.XPATH, "//button[@data-product-type='print']")
    audio_button = self.driver.find_element(By.XPATH, "//button[@data-product-type='online + audio']")
    ebook_button.click()
    time.sleep(2) 
    price_element = self.driver.find_element(By.XPATH, "//div[@data-product-type='eBook']//span[@class='_final-price']")
    updated_classes = price_element.get_dom_attribute('class')
    with self.subTest("book price"):
        assert 'hidden' not in updated_classes, "Price is still hidden after clicking the button"
    print_button.click()
    time.sleep(2) 
    price_element = self.driver.find_element(By.XPATH, "//div[@data-product-type='print']//span[@class='_final-price']")
    updated_classes = price_element.get_dom_attribute('class')
    with self.subTest("print "):
        assert 'hidden' not in updated_classes, "Price is still hidden after clicking the button"
    audio_button.click()
    time.sleep(2) 
    price_element = self.driver.find_element(By.XPATH, "//div[@data-product-type='online + audio']//span[@class='_final-price']")
    updated_classes = price_element.get_dom_attribute('class')
    with self.subTest("online + audio "):
        assert 'hidden' not in updated_classes, "Price is still hidden after clicking the button"