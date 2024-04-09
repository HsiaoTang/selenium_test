import time
from datetime import datetime

from selenium.webdriver.common.by import By

from notification.line_broadcaster import LineBroadcaster
from pages.product_list_page import ProductListPage
from tests.test_base import TestBase
from tests.test_dashboard import TestDashboard


class TestProductList(TestBase):
    product_list_tab_span = (By.XPATH, "//span[text()='產品列表']")
    products_button = (By.XPATH, "//*[@id='app']/div[2]/div/main/div/div/div[2]/div/div[1]/div/div")
    sensor_data_span = (By.XPATH, "//span[text()='即時值']")
    sensor_item_span = (By.XPATH, "//span[@class='font-weight-bold']")
    sensor_item_time = (By.XPATH, "//div[@class='flex-grow-1 px-2 mb-0 d-inline-flex align-items-center']")
    sensor_history_modal = (By.XPATH, "//div[@class='text-right px-2 mb-0']//button[@class='border-0']")
    sensor_history_time = (By.XPATH, "//*[@id='app']/div[2]/div/main/div/div/div[2]/div[3]/div/div/div/div/div["
                                     "2]/div[2]/div/div[1]/div[1]/div/div/div/div/div[5]/div/div/div["
                                     "1]/table/tbody/tr[1]/td[2]")


    @classmethod
    def perform_product_list_checking(cls):
        map_load_success = TestDashboard.perform_map_checking()
        assert map_load_success, "failed to load map"

        product_list_page = ProductListPage()
        product_list_page.switch_back(cls.driver)
        product_list_page.click(cls.driver, cls.product_list_tab_span)
        product_list_page = ProductListPage()
        products = product_list_page.wait_until_visible_all_elements(cls.driver, cls.products_button)
        for product in products:
            print(products)
            print(len(products))
            product.click()
            product_list_page.click(cls.driver, cls.sensor_data_span)
            sensor_items_time = product_list_page.wait_until_visible_all_elements(cls.driver, cls.sensor_item_time)
            now = datetime.now()
            temperature_time = datetime.strptime(sensor_items_time[5].text, "%Y-%m-%d %H:%M:%S.%f")
            humidity_time = datetime.strptime(sensor_items_time[10].text, "%Y-%m-%d %H:%M:%S.%f")
            temperature_time_diff = now - temperature_time
            if temperature_time_diff.total_seconds() < 600:
                line_boardcastor = LineBroadcaster()
                line_boardcastor.send_notification("test line")
            humidity_time_diff = now - humidity_time

        # products[0].click()
        # product_list_page.click(cls.driver, cls.sensor_data_span)
        # sensor_items = product_list_page.wait_until_visible_all_elements(cls.driver, cls.sensor_item_span)
        # for sensor_item in sensor_items:
        #     print(sensor_item.text)
        # sensor_items_time = product_list_page.wait_until_visible_all_elements(cls.driver, cls.sensor_item_time)
        # for sensor_time in sensor_items_time:
        #     print(sensor_time.text)
        # sensor_history_modals = product_list_page.wait_until_visible_all_elements(cls.driver, cls.sensor_history_modal)
        # print(len(sensor_history_modals))
        # sensor_history_modals[0].click()
        # latest_sensor_data_time = product_list_page.wait_until_visible_single_element(cls.driver, cls.sensor_history_time)
        # print(latest_sensor_data_time.text)
        # time.sleep(10)

    @classmethod
    def test_product_list(cls):
        cls.perform_product_list_checking()
