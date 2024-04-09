
import os.path

import pytest
from selenium import webdriver


class TestBase:
    chromedriver_path = os.path.join(os.getcwd(), "drivers", "chromedriver")
    chrome_options = webdriver.ChromeOptions()
    chrome_options._binary_location = chromedriver_path
    driver=webdriver.Chrome(options=chrome_options)

    @pytest.fixture
    def setup(cls):
        cls.driver.maximize_window()
        yield cls.driver
        cls.driver.quit()
