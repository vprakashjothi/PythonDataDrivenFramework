from base.base_test import BaseTest
from pages.dashboard_page import DashboardPage
from utils.logger import get_logger
from utils.screenshot import take_screenshot

#logger = get_logger()


class TestDashboard(BaseTest):

    def test_dashboard_loaded(self):
        dashboard = DashboardPage(self.driver)

        try:
            assert dashboard.is_displayed()
        except Exception as e:
            take_screenshot(self.driver, "dashboard_fail")
#            logger.error(str(e))
            raise