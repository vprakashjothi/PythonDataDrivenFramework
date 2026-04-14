from selenium import webdriver
from utils.config_reader import get_config


class BaseTest:
    def setup_method(self):
        browser = get_config("browser")

        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()

        self.driver.maximize_window()
        self.driver.get(get_config("url"))

    def teardown_method(self):
        self.driver.quit()