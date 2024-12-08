import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
import time
# 5/subTest
class Test_search(unittest.TestCase):
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
        self.mylist = ["chapter_id_2", "chapter_id_3", "chapter_id_4"]
    def wait_for_window(self, timeout = 2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()      
    def tearDown(self) :
        self.driver.quit()
# 1
    def test_audio_checkbox(self):
        catalog = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "catalog")))
        catalog.click()
        audio_checkbox = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, '//label[span[text()="audio"]]/input[@type="checkbox"]')))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", audio_checkbox)
        # Check if the audio checkbox is not selected and click it if necessary
        if not audio_checkbox.is_selected():
            audio_checkbox.click()
        filtered_results = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.liveaudio-corner[title="has audio"]')))
        for result in filtered_results:
            title = result.get_attribute("title")
        assert title == "has audio", f"Title attribute is not 'has audio', found: {title} result {filtered_results} "
# 2 
    def test_author_search(self):
        self.driver.find_element(By.LINK_TEXT, "catalog").click()
        time.sleep(1)
        search_box = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_search-box-wrapper']/input[@type='text']")))
        search_box.click()
        search_box.send_keys("Benjamin Tan Wei Hao")
        search_box.send_keys(Keys.ENTER)
        # search_box.send_keys("Daniel Zingaro")
        authors_element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='_authors-date-container']/span[@class='_authors-container']")))
        for result in authors_element:
            author = result.find_element(By.XPATH, "..//..//..//span[@class='_authors-container']").text.strip()
            authors_list = author.split(', ')
            expected_author = "Benjamin Tan Wei Hao"
        assert expected_author in authors_list, f"Expected author to be '{expected_author}', but found '{author}'"
# 3
    def test_returns_relevant_results(self):
        search = self.driver.find_element(By.NAME, "q")
        search.send_keys("python program")
        suggestion = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'autocomplete-suggestion-root-n')]//span[text()='python program']")))
        suggestion.click()
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-product-title")))
        assert self.driver.find_element(By.XPATH, "//div[@class='search-product-title']/strong[text()='Python Program']").text == "Python Program"
        time.sleep(1)
        self.driver.close()
# 4
    def test_word_in_book(self):
        search_input = self.driver.find_element(By.NAME, "q")
        search_input.send_keys("mysql")      
        suggestion = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'autocomplete-suggestion-root-n')]//span[text()='mysql']")))
        suggestion.click()
        time.sleep(2)
        action_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_action-button-containers']//button")))
        action_button.click()
        search_result = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='search-result']/span[@class='search-result' and text()='MySQL']")))
        time.sleep(2)
        assert search_result.text == "MySQL"
        self.driver.close()
# 5 --subTest
    def test_chapter(self):
        self.driver.find_element(By.LINK_TEXT, "catalog").click()
        self.vars["window_handles"] = self.driver.window_handles
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".search-catalog-product-root:nth-child(1) img").click()
        time.sleep(3)
        self.vars["win5593"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win5593"])
        self.driver.find_element(By.CSS_SELECTOR, ".fas:nth-child(2)").click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".livebook-viewer-product-page-root")))
        time.sleep(3)
        for chapter_id in self.mylist:  
            self.driver.find_element(By.CSS_SELECTOR, f"#{chapter_id} .unit-link").click()
            heading_element_chapter = self.driver.find_element(By.XPATH, f"//h2[@id='{chapter_id}']//span[@class='unit-link chap-link']").text.lower()
            time.sleep(2)
            element_1 = self.driver.find_element(By.XPATH, "//span[@class='chapter-title-numbering']/span[@class='num-string']").text
            element_2 = self.driver.find_element(By.CSS_SELECTOR, "span.chapter-title-text").text
            heading_element_title=f"{element_1} {element_2}"   
            with self.subTest(chapter_id):
                assert heading_element_chapter == heading_element_title.lower()
            time.sleep(1)
