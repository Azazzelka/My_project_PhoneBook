from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC




class ContactsPage(BasePage):
    CONTACTS_PAGE_LINK = (By.XPATH, '//a[@href="/contacts"]')
    CONTACT_CARD = (By.XPATH, '//div[@class="contact-item_card__2SOIM"]')
    EDIT_BUTTON_CONTACTS = (By.XPATH, "//button[text()='Edit']")
    EDIT_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    EDIT_LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    EDIT_PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    EDIT_EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='email']")
    EDIT_ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")
    EDIT_DESCRIPTION_INPUT = (By.CSS_SELECTOR, "input[placeholder='desc']")
    EDIT_SAVE_BTN = (By.XPATH, "//button[text()='Save']")
    CONTACT_DETAILS_CARD = (By.CLASS_NAME, "contact-item-detailed_card__50dTS")



    def open_contact_card_by_phone(self, phone):
        self.click((By.XPATH, f"//h3[text()='{phone}']/.."))


    def open_contact_card_by_name(self, name):
        self.click((By.XPATH, f"//h2[text()='{name}']/.."))

    def edit_field_in_contacts_form_by_phone(self, phone, locator, new_value):
        self.open_contact_card_by_phone(phone)
        self.click(self.EDIT_BUTTON_CONTACTS)
        self.input_field(locator, new_value)
        self.click(self.EDIT_SAVE_BTN)
        self.wait_until_edit_form_closed()

        return self

        #self.get_contact_details_card_updated(phone, new_value)


    def get_contact_name_by_phone(self, phone):
        name_locator = (By.XPATH, f"//h3[text()='{phone}']/../h2")
        return self.find(name_locator).text

    def wait_until_edit_form_closed(self):
        self.wait_until_form_closed(self.EDIT_SAVE_BTN)
        return self

    def get_contact_details_card_updated(self,phone, new_value):
        self.open_contact_card_by_phone(phone)
        self.wait.until(EC.text_to_be_present_in_element(self.CONTACT_DETAILS_CARD,new_value))

    def get_edit_contact_value(self, locator):
        self.click(self.EDIT_BUTTON_CONTACTS)
        return self.find(locator).get_attribute("value")

    def get_contact_details_card_updated_by_name(self,name, new_value):
        self.open_contact_card_by_name(name)
        self.wait.until(EC.text_to_be_present_in_element(self.CONTACT_DETAILS_CARD,new_value))








