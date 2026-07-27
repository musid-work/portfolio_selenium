from selenium.webdriver.common.by import By
from config.settings import Settings
from config.routes import Routes

class SeleniumLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Settings.BASE_URL + Routes.LOGIN.value
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.flash_message = (By.ID, "flash")

    def navigate(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_flash_message_text(self):
        return self.driver.find_element(*self.flash_message).text