from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from tests.test_base import TestBase


class TestLogin(TestBase):
    login_page_url = (
        "https://iiot.chte.cloud/keycloak/realms/movenpick/protocol/openid-connect/auth?client_id"
        "=frontend&redirect_uri=https%3A%2F%2Fmovenpick.chte.cloud%2Fiot%2FAboutIIoT&state=332466df"
        "-bcfa-49ba-b0f2-6ef254510056&response_mode=fragment&response_type=code&scope=openid&nonce"
        "=7394d94c-6748-40ae-93a7-2263f17edc1d")
    username_field = "movenpick"
    username_input = (By.ID, "username")
    password_field = "movenpick@cht"
    password_input = (By.ID, "password")
    sign_in_button = (By.NAME, "login")
    dashboard_tab_span = (By.XPATH, "//span[text()='儀表板']")

    @classmethod
    def perform_login(cls):
        login_page = LoginPage()
        login_page.load_page(cls.driver, cls.login_page_url)
        login_page.enter_username(cls.driver, cls.username_input, cls.username_field)
        login_page.enter_password(cls.driver, cls.password_input, cls.password_field)
        login_page.click(cls.driver, cls.sign_in_button)
        return login_page.check_existence(cls.driver, cls.dashboard_tab_span)

    @classmethod
    def test_login(cls):
        assert cls.perform_login(), "login failed!"
