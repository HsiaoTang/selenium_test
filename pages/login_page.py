from pages.base_page import BasePage


class LoginPage(BasePage):

    def enter_username(self, driver, username_input, username):
        self.enter_text(driver, username_input, username)

    def enter_password(self, driver, password_input, password):
        self.enter_text(driver, password_input, password)
