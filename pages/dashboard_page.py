from selenium.webdriver.common.by import By
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    heading = (By.XPATH, "//*[text()='Test login']")

    def is_displayed(self):
        return self.driver.find_element(*self.heading).is_displayed()