import pytest
import time
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
# 4
class Test_my_wish_list_copy():
    def setup_method(self):
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
        

    def login(self):
        self.driver.find_element(By.CSS_SELECTOR, "div.nav-dashboard-button.clickable label[for='sign-in']").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username-sign-in"))).send_keys("kalematreat@gmail.com")
        password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "password-sign-in")))
        password_field.click()
        password_field.send_keys("kk20242025")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "submit"))).click()

    def click_on_harte(self):
        wishlist_container = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".wishlist-container")))
        add_button = wishlist_container.find_element(By.CSS_SELECTOR, ".wishlist-toggle.wishlist-add")
        remove_button = wishlist_container.find_element(By.CSS_SELECTOR, ".wishlist-toggle.wishlist-remove")
        time.sleep(2)
        wishlist_container = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.wishlist-container")))
        if "on-wishlist" in wishlist_container.get_attribute("class"):
            print("The book is already in the wish list. No action needed.")
        else:
            print("The book is not in the wish list. Adding it now...")
            add_button.click()

# 1
    def test_mylis_empty(self):
        self.login()
        # time.sleep(1)
        wish_list_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".hidden-xs > .btn")))
        wish_list_button.click()
        message_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'You have nothing in your wish list')]")))
        message_text = message_element.text.strip()
        assert "You have nothing in your wish list" in message_text, f"Expected message not found! Found: {message_text}"
        time.sleep(1)
        self.driver.close()
# 2
    def test_add_to_my_wish_list(self):
        self.login()
        self.driver.find_element(By.LINK_TEXT, "catalog").click()
        time.sleep(1)
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-catalog-product-root:nth-child(1) .\\_circle-button"))).click()
        self.vars["window_handles"] = self.driver.window_handles
        product_book = self.driver.find_element(By.LINK_TEXT, "Build a Large Language Model (From Scratch)")
        title_1 = self.driver.find_element(By.CSS_SELECTOR, "div._title-container a._title").text.strip()
        product_book.click()
        self.vars["win1212"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win1212"])
        self.click_on_harte()
        # time.sleep(1)
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.CSS_SELECTOR, ".nav-dashboard-button > label").click()
        time.sleep(1)
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".account-block:nth-child(1) > .caption"))).click()
        # time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".hidden-xs > .btn").click()
        title_2 = self.driver.find_element(By.CSS_SELECTOR,"div.product-title").text.strip()
        assert title_2 == title_1
        time.sleep(1)
        self.driver.close()
# 3  
    def test_remove(self):
        self.login()
        self.driver.find_element(By.LINK_TEXT, "catalog").click()
        time.sleep(1)
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-catalog-product-root:nth-child(1) .\\_circle-button"))).click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "Build a Large Language Model (From Scratch)").click()
        self.vars["win1212"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win1212"])
        self.click_on_harte()
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "Deep Learning with Python, 2nd ed.").click()
        self.vars["win991"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win991"])
        self.click_on_harte()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.CSS_SELECTOR, ".nav-dashboard-button > label").click()
        time.sleep(2)
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".account-block:nth-child(1) > .caption"))).click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".hidden-xs > .btn").click()
        time.sleep(1)
        title_element_1 = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .product-title").text
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn:nth-child(2) > .fas").click()
        self.driver.refresh()
        title_element_2 = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .product-title").text
        time.sleep(2)
        assert title_element_1!= title_element_2, f"Text was found on the page, but it should not be title_element_1 {title_element_1} title_element_2 {title_element_2}."
# 4 
    def test_remove_button_is_displayed(self):
        self.login()
        self.driver.find_element(By.LINK_TEXT, "catalog").click()
        time.sleep(1)
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-catalog-product-root:nth-child(1) .\\_circle-button"))).click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "Build a Large Language Model (From Scratch)").click()
        self.vars["win1212"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win1212"])
        self.click_on_harte()
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.CSS_SELECTOR, ".nav-dashboard-button > label").click()
        time.sleep(1)
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".account-block:nth-child(1) > .caption"))).click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".hidden-xs > .btn").click()
        time.sleep(1)
        button = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn:nth-child(2) > .fas")
        assert button.is_displayed(), "The button is not visible on the page."