import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def load_page(self, driver, url):
        driver.get(url)
        self.wait_until_complete(driver)

    def wait_until_complete(self, driver, timeout=120):
        WebDriverWait(driver, timeout).until(
            lambda this_driver: driver.execute_script("return document.readyState") == "complete")

    def wait_until_visible_single_element(self, driver, locator, timeout=120):
        return WebDriverWait(driver, timeout).until(ec.visibility_of_element_located(locator))

    def wait_until_visible_all_elements(self, driver, locator, timeout=120):
        return WebDriverWait(driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def wait_until_clickable_single_element(self, driver, locator, timeout=120):
        return WebDriverWait(driver, timeout).until(ec.element_to_be_clickable(locator))

    def switch_to_frame(self, driver, locator, timeout=120):
        driver.switch_to.frame(self.wait_until_visible_single_element(driver, locator, timeout))

    def switch_back(self, driver):
        driver.switch_to.default_content()

    def click(self, driver, locator, timeout=120):
        self.wait_until_clickable_single_element(driver, locator, timeout).click()
        time.sleep(2)

    def enter_text(self, driver, locator, text, timeout=120):
        self.wait_until_clickable_single_element(driver, locator, timeout).send_keys(text)
        time.sleep(2)

    def check_existence(self, driver, locator, timeout=120):
        element = self.wait_until_clickable_single_element(driver, locator, timeout)
        if element is not None:
            return True
        return False
