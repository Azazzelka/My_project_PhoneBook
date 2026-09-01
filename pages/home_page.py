from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.add_contact_page import ContactPage
from pages.login_page import LoginPage


class HomePage(BasePage):
    URL = "https://telranedu.web.app/home"
    LOGIN_NAV_LINK = (By.XPATH, '//a[@href="/login"]')
    ADD_NAV_LINK = (By.CSS_SELECTOR, "[href = '/add']")

    def open(self) -> "HomePage":
        self.driver.get(self.URL)
        return self

    def open_login_page(self):
        self.click(self.LOGIN_NAV_LINK)
        return LoginPage(self.driver)

    def open_add_contact_form(self):
        self.click(self.ADD_NAV_LINK)
        return ContactPage(self.driver)

