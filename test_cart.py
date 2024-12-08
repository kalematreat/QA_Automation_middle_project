import pytest
import time
import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# 4/5 subTest
class Test_cart(unittest.TestCase):
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
    def tearDown(self) :
        self.driver.quit()
    def wait_for_window(self, timeout = 2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()
# 1 /subTest
    def test_add_to_cart(self):
        self.driver.find_element(By.LINK_TEXT, "catalog").click()
        time.sleep(2)
        book_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Build a Large Language Model (From Scratch)")))
        book_link.click()
        # Wait for a new window to open and switch to it
        WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)
        self.vars["window_handles"] = self.driver.window_handles
        self.vars["root"] = self.driver.current_window_handle
        self.vars["new_window"] = [handle for handle in self.driver.window_handles if handle != self.vars["root"]][0]
        self.driver.switch_to.window(self.vars["new_window"])
        time.sleep(1)
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".hidden-xs .\\_add-to-cart-button")))
        add_to_cart_button.click()
        time.sleep(2)
        cart_count = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span#header-cart-count"))).text
        title_element_2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "title"))).text
        with self.subTest("Cart Count"):
            assert cart_count == "1", f"Expected cart count to be '1', but found '{cart_count}'"
        with self.subTest("Title Verification"):
            assert "Build a Large Language Model" in title_element_2, f"Expected title not found in: {title_element_2}"
        self.driver.close()
# good 2
    def test_change_quantity(self):
        self.driver.find_element(By.LINK_TEXT, "catalog").click()
        time.sleep(1)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "Build a Large Language Model (From Scratch)").click()
        self.vars["win2846"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win2846"])
        self.driver.find_element(By.CSS_SELECTOR, ".hidden-xs .\\_add-to-cart-button").click()
        time.sleep(3)
        dropdown=self.driver.find_element(By.CSS_SELECTOR, ".quantity-select-button")
        dropdown.find_element(By.XPATH, "//option[. = '2']").click()
        time.sleep(1)
        price =self.driver.find_element(By.CSS_SELECTOR, ".summary-column-grid span:nth-of-type(2)").text.strip()
        sale_discount  = self.driver.find_element(By.CSS_SELECTOR, ".summary-column-grid .summary-column-two-column-grid:nth-of-type(2) span:nth-of-type(2)").text.strip()
        price = float(price.replace('$', ''))
        sale_discount = float(sale_discount.replace('- $', ''))
        expected_total = price - sale_discount
        total_price =self.driver.find_element(By.CSS_SELECTOR, "#summary-total-row-cost").text.strip()
        time.sleep(3)
        total_price=float(total_price.replace('$', ''))
        time.sleep(3)
        assert round(float(expected_total), 2) == round(float(total_price), 2), f"price={price} sale_discount={sale_discount} total_price={total_price} expected_total= {expected_total} "
# good 3
    def test_remove_2(self):
        self.driver.find_element(By.LINK_TEXT, "catalog").click()
        self.vars["window_handles"] = self.driver.window_handles
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Build a Large Language Model (From Scratch)"))).click()
        self.vars["win2846"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win2846"])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".hidden-xs .\\_add-to-cart-button"))).click()
        cart_count_before = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@id='header-cart-count']"))).text
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Deep Learning with Python, 2nd ed."))).click()
        # Switch to the second product window
        self.vars["win2846"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win2846"])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".hidden-xs .\\_add-to-cart-button"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'product-remove cart-action')]"))).click()
        cart_count_after = int(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@id='header-cart-count']"))).text)
        page_source = self.driver.page_source
        time.sleep(2)
        if "class=static-header-cart-count" in page_source:
            cart_count_after == cart_count_before - 1
        else:
            cart_count_after=""
        assert cart_count_after == cart_count_before
        self.driver.close()
# good 4
    def test_remove_1(self):
        self.driver.find_element(By.LINK_TEXT, "catalog").click()
        time.sleep(1) 
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "Deep Learning with Python, 2nd ed.").click()
        # time.sleep(1)
        self.vars["win2846"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win2846"])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".hidden-xs .\\_add-to-cart-button"))).click()
        cart_count_before = self.driver.find_element(By.XPATH, "//span[@id='header-cart-count']").text
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.product-remove.cart-action"))).click()
        # time.sleep(2)
        cart_count_after = self.driver.find_element(By.CSS_SELECTOR, "#header-cart-count").text
        page_source = self.driver.page_source
        time.sleep(3)
        if "class=static-header-cart-count" in page_source:
            cart_count_after == cart_count_before - 1
        else:
            cart_count_after=""
        assert cart_count_after == cart_count_before  
        self.driver.close()
    
