import time
from selenium.webdriver.common.by import By

from pages.dashboard_page import DashboardPage
from tests.test_base import TestBase
from tests.test_login import TestLogin


class TestDashboard(TestBase):
    dashboard_tab_span = (By.XPATH, "//span[text()='儀表板']")
    map_frame = (By.XPATH, "//iframe[contains(@src, '/iot/productMapWidget')]")
    north_area_group = (By.XPATH, "//div[contains(@class, 'leaflet-container')]//div[contains(@class, 'leaflet-map-pane')]//div["
                                  "contains(@class, 'leaflet-marker-pane')]//div[contains(@class, 'leaflet-marker-icon')]/div/span[text("
                                  ")='6']")
    product_list_tab_spane = (By.XPATH, "//span[text()='產品列表']")

    @classmethod
    def perform_map_checking(cls):
        # login
        login_success = TestLogin.perform_login()
        assert login_success, "login failed"

        # map
        dashboard_page = DashboardPage()
        dashboard_page.click(cls.driver, cls.dashboard_tab_span)
        dashboard_page.switch_to_frame(cls.driver, cls.map_frame)
        return dashboard_page.check_existence(cls.driver, cls.north_area_group)

    @classmethod
    def test_map(cls):
        assert cls.perform_map_checking(), "map does not exist"

