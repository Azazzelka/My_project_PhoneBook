from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage


class HomePage(BasePage):
    URL = "https://telranedu.web.app/home"
    LOGIN_NAV_LINK = (By.XPATH, '//a[@href="/login"]')

    def open(self) -> "HomePage":
        self.driver.get(self.URL)
        return self

    def open_login_page(self):
        self.click(self.LOGIN_NAV_LINK)
        return LoginPage(self.driver)