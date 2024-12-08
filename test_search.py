import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
import time
class Test4441:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.manning.com/")
        self.driver.set_window_size(1552, 880)  # Set window size
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.window_handles) > len(self.vars.get("window_handles", []))
        )
        new_window = set(self.driver.window_handles).difference(set(self.vars.get("window_handles", []))).pop()
        return new_window
# 1
# gooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooood
    def test_audio_checkbox(self):
        self.driver.get("https://www.manning.com/")
        catalog_link = self.driver.find_element(By.LINK_TEXT, "catalog")
        actions = ActionChains(self.driver)
        actions.move_to_element(catalog_link).perform()
        catalog_link.click()
        time.sleep(5)
        audio_checkbox= self.driver.find_element(By.XPATH, '//label[span[text()="audio"]]/input[@type="checkbox"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", audio_checkbox)
        if not audio_checkbox.is_selected():
            audio_checkbox.click()
        self.driver.current_window_handle
        time.sleep(5)
        filtered_results = self.driver.find_elements(By.CSS_SELECTOR, 'div.liveaudio-corner[title="has audio"]')
        for result in filtered_results:
            title = result.get_attribute("title")
            assert title == "has audio", f"Title attribute is not 'has audio', found: {title}"

# 2
# good but there is alert
    def test_author_search(self):
        self.driver.get("https://www.manning.com/")
        self.driver.set_window_size(1552, 880)
        element = self.driver.find_element(By.CSS_SELECTOR, ".nav-cart-button > svg")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "catalog").click()
        time.sleep(1)
        search_box = self.driver.find_element(By.XPATH, "//div[@class='_search-box-wrapper']/input[@type='text']")
        search_box.click() 
        search_box.send_keys("Benjamin Tan Wei Hao") 
        # search_box.send_keys("Daniel Zingaro")
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)
        authors_element = self.driver.find_elements(By.XPATH, "//div[@class='_authors-date-container']/span[@class='_authors-container']")
        for result in authors_element:
            author = result.find_element(By.XPATH, "..//..//..//span[@class='_authors-container']").text.strip()
            authors_list = author.split(', ')
            # expected_author = "Benjamin Tan Wei Hao"
            expected_author = "Benjamin Tan Wei Hao"
            print(f"expected_author '{author}'")
            # print(f"expected_author '{expected_author}' ---> authors_list '{authors_list}'")
            assert expected_author in authors_list, f"Expected author to be '{expected_author}', but found '{author}'"
            # assert author in expected_author, f"Expected author to be '{expected_author}', but found '{author}'"

# 3
# # good but there is alert
    def test_that_it_returns_relevant_results(self):
        self.driver.get("https://www.manning.com/")
        self.driver.set_window_size(1552, 880)
        search = self.driver.find_element(By.NAME, "q")
        search.send_keys("python program")
        # alert!!!!!!!!!!!!!!
        time.sleep(2)
        suggestion = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'autocomplete-suggestion-root-n')]//span[text()='python program']")))
        suggestion.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "search-product-title")))    
        assert self.driver.find_element(By.XPATH, "//div[@class=\'search-product-title\']/strong[text()=\'Python Program\']").text == "Python Program"
        time.sleep(1)

# 4
# # good but there is alert+ capital/small letters
    def test_search_SQL(self):
        search_input = self.driver.find_element(By.NAME, "q")
        search_input.send_keys("mysql")
        # alert!!!!!!!!!!!!!!
        time.sleep(2)
        suggestion = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'autocomplete-suggestion-root-n')]//span[text()='mysql']")))
        suggestion.click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class=\'_action-button-containers\']//button")))
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@class=\'_action-button-containers\']//button").click()
        time.sleep(5)
        search_result = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='search-result']/span[@class='search-result' and text()='MySQL']")))
        assert search_result.text == "MySQL"
        time.sleep(1)
        self.driver.close()

