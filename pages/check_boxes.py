from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import Settings
from config.routes import Routes

class SeleniumCheckBoxes:
    def __init__(self, driver):
        self.driver = driver
        self.url = Settings.BASE_URL + Routes.CHECKBOXES.value
        self.checkbox_1 = (By.XPATH, "(//input[@type='checkbox'])[1]")
        self.checkbox_2 = (By.XPATH, "(//input[@type='checkbox'])[2]")

    def navigate(self):
        self.driver.get(self.url)

    def is_checkbox_1_selected(self):
        return self.driver.find_element(*self.checkbox_1).is_selected()

    def is_checkbox_2_selected(self):
        return self.driver.find_element(*self.checkbox_2).is_selected()

    def toggle_checkbox_1(self):
        self.driver.find_element(*self.checkbox_1).click()

    def toggle_checkbox_2(self):
        self.driver.find_element(*self.checkbox_2).click()