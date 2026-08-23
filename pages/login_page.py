from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from models.login_data import LoginData
from models.registration_data import RegistrationData
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    LOGIN_BTN = (By.XPATH, '//button[@name="login"]')
    SIGN_OUT_BTN = (By.XPATH, '//*[text()="Sign Out"]')
    REGISTRATION_BTN = (By.XPATH, '//button[@name="registration"]')

    def fill_email(self,email):
        self.input_field(self.EMAIL_INPUT, email)

    def fill_password(self, password):
        self.input_field(self.PASSWORD_INPUT, password)

    def submit_login(self):
        self.click(self.LOGIN_BTN)

    def submit_registration(self):
        self.click(self.REGISTRATION_BTN)

    def is_logged(self) -> bool:
        try:
            self.visibility(self.SIGN_OUT_BTN)
            return True
        except TimeoutException:
            return False

    def fill_login_form(self, user: LoginData):
        self.fill_email(user.email)
        self.fill_password(user.password)
        self.submit_login()

    def fill_registration_form(self, user:RegistrationData):
        self.fill_email(user.email)
        self.fill_password(user.password)
        self.submit_registration()

