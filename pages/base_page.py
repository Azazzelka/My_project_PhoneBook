from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Locator = tuple[str, str]
class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)


    def find(self, locator: Locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def visibility(self, locator: Locator, timeout: int | None = None):
        wait = (self.wait if timeout is None else WebDriverWait(self.driver, timeout))
        return wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: Locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_field(self, locator: Locator, text: str):
        element = self.visibility(locator)
        element.clear()
        element.send_keys(text)

    def get_alert_text(self):
        return self.wait.until(EC.alert_is_present()).text

    def alert_accept(self):
        self.driver.switch_to.alert.accept()

    def wait_until_form_closed(self, locator:Locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
        return self
