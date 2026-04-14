import allure
import pytest
from base.base_test import BaseTest
from pages.login_page import LoginPage
from utils.excel_reader import get_data
from utils.logger import get_logger
from utils.screenshot import take_screenshot

#logger = get_logger()


class TestLogin(BaseTest):

    @pytest.mark.parametrize("username,password", get_data("login"))
    def test_login(self, username, password):
        login_page = LoginPage(self.driver)

        try:
#           logger.info(f"Testing login with {username}")
            login_page.login(username, password)
            assert "logged-in-successfully" in self.driver.current_url
        except Exception as e:
            take_screenshot(self.driver, "login_fail")
            screenshot = self.driver.get_screenshot_as_png()
            allure.attach(screenshot,name="Failure Screenshot",attachment_type=allure.attachment_type.PNG)
#           logger.error(str(e))
            raise

