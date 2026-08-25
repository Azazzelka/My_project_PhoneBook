from selenium.webdriver.common.by import By

from models.contact import Contact
from pages.base_page import BasePage


class ContactPage(BasePage):
    ADD_NAV_LINK = (By.CSS_SELECTOR, "[href = '/add']")
    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='email']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "input[placeholder='description']")
    SAVE_BTN = (By.XPATH, "//button[b[text()='Save']]")



    def fill_name(self, name):
        self.input_field(self.NAME_INPUT, name)

    def fill_last_name(self, last_name):
        self.input_field(self.LAST_NAME_INPUT, last_name)

    def fill_phone(self, phone):
        self.input_field(self.PHONE_INPUT, phone)

    def fill_email_input(self, email):
        self.input_field(self.EMAIL_INPUT, email)

    def fill_address(self, address):
        self.input_field(self.ADDRESS_INPUT, address)

    def fill_description(self, description):
        self.input_field(self.DESCRIPTION_INPUT, description)

    def fill_add_contact_form(self, user: Contact):
        self.fill_name(user.name)
        self.fill_last_name(user.last_name)
        self.fill_phone(user.phone)
        self.fill_email_input(user.email)
        self.fill_address(user.address)
        self.fill_description(user.description)

        element = self.visibility(self.SAVE_BTN)
        element.click()

