# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from logger import logger_object


class GoogleSearchPage:
    textbox_search_google = r'//*[@id="tsf"]/div/div/div/div/div/input'  # xpath
    button_search = "btnK"  # name
    result_stats = "result-stats"  # id
    wait = None
    write_log = logger_object.get_instance()
    page_url = r"https://www.google.com/"

    def __init__(self, driver):
        """

        :rtype: None
        """
        self.driver = driver  # type: webdriver
        self.wait = WebDriverWait(self.driver, 10)

    def __del__(self):
        pass

    def load_page(self):
        self.driver.get(self.page_url)

    def close_page(self):
        self.driver.close()

    def set_search_text(self, search_text):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.textbox_search_google))).send_keys(
            search_text.decode(encoding="UTF-8", errors='strict'))

    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.button_search))).send_keys(
            Keys.ENTER)
        # also can use button.click() since now waiting for the element ot be clickable

    def get_result_stats(self):
        # element = self.driver.find_element(By.ID, self.result_stats).text
        element = self.wait.until(EC.presence_of_element_located((By.ID, self.result_stats))).text
        try:
            assert "About" in element
            return element
        except AssertionError:
            self.write_log.error("AssertionError: 'About' not found in {}".format(element))
            return None
