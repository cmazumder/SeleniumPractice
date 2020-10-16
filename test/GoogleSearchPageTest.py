from selenium import webdriver

from logger import logger_object
from pages.GoogleSearchPage import GoogleSearchPage


class GoogleSearchPageTest:
    # ChromeDriver = None
    # EdgeDriver = None
    # OperaDriver = None
    # IEDriver = None
    # FirefoxDriver = None
    ChromeDriver = r"SeleniumDrivers\chromedriver.exe"
    EdgeDriver = r"SeleniumDrivers\msedgedriver.exe"
    OperaDriver = r"SeleniumDrivers\operadriver.exe"
    IEDriver = r"SeleniumDrivers\IEDriverServer.exe"
    FirefoxDriver = r"SeleniumDrivers\geckodriver.exe"
    write_log = logger_object.get_instance()
    search_text = None

    def __init__(self, search_text="Learn Selenium!"):
        self.search_text = search_text
        # self.ChromeDriver = webdriver.Chrome(executable_path=r"SeleniumDrivers\chromedriver.exe")
        # self.EdgeDriver = webdriver.Edge(executable_path=r"SeleniumDrivers\msedgedriver.exe")
        # self.OperaDriver = webdriver.Opera(executable_path=r"SeleniumDrivers\operadriver.exe")
        # self.IEDriver = webdriver.Ie(executable_path=r"SeleniumDrivers\IEDriverServer.exe")
        # self.FirefoxDriver = webdriver.Firefox(executable_path=r"SeleniumDrivers\geckodriver.exe")

    def __del__(self):
        pass

    def perform_google_search(self, browser):
        result = None
        try:
            browser.load_page()
            browser.set_search_text(self.search_text)
            browser.click_search_button()
            # time.sleep(3)
            result = browser.get_result_stats()
        except Exception as err:
            self.write_log.error(err)
        finally:
            browser.close_page()
            return result

    def write_browser_performance_info(self, browser_name, result_stats):
        self.write_log.info(
            "Browser: {} | Searched text: \"{}\" | results_count: {} | Time (sec): {}".format(browser_name,
                                                                                                self.search_text,
                                                                                                result_stats.split()[
                                                                                                    1],
                                                                                                result_stats.split()[
                                                                                                    3][1:]))

    def run_on_chrome(self):
        chrome_browser = GoogleSearchPage(driver=webdriver.Chrome(executable_path=self.ChromeDriver))
        result_stats = self.perform_google_search(browser=chrome_browser)
        if result_stats:
            self.write_browser_performance_info(browser_name="Chrome ", result_stats=result_stats)
            return float(result_stats.split()[3][1:])
        else:
            self.write_log.error("Issue with Chrome browser")
            return None

    def run_on_edge(self):
        edge_browser = GoogleSearchPage(driver=webdriver.Edge(executable_path=self.EdgeDriver))
        result_stats = self.perform_google_search(browser=edge_browser)
        if result_stats:
            self.write_browser_performance_info(browser_name="Edge   ", result_stats=result_stats)
            return float(result_stats.split()[3][1:])
        else:
            self.write_log.error("Issue with Edge browser")
            return None

    def run_on_firefox(self):
        firefox_browser = GoogleSearchPage(driver=webdriver.Firefox(executable_path=self.FirefoxDriver))
        result_stats = self.perform_google_search(browser=firefox_browser)
        if result_stats:
            self.write_browser_performance_info(browser_name="Firefox", result_stats=result_stats)
            return float(result_stats.split()[3][1:])
        else:
            self.write_log.error("Issue with Firefox browser")
            return None

    def run_on_ie(self):
        ie_browser = GoogleSearchPage(driver=webdriver.Ie(executable_path=self.IEDriver))
        result_stats = self.perform_google_search(browser=ie_browser)
        if result_stats:
            self.write_browser_performance_info(browser_name="IE     ", result_stats=result_stats)
            return float(result_stats.split()[3][1:])
        else:
            self.write_log.error("Issue with IE browser")
            return None

    def run_on_opera(self):
        opera_browser = GoogleSearchPage(driver=webdriver.Opera(executable_path=self.OperaDriver))
        result_stats = self.perform_google_search(browser=opera_browser)
        if result_stats:
            self.write_browser_performance_info(browser_name="Opera  ", result_stats=result_stats)
            return float(result_stats.split()[3][1:])
        else:
            self.write_log.error("Issue with Opera browser")
            return None
