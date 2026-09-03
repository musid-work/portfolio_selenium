from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from config.settings import Settings
from config.routes import Routes

class SeleniumDropdownOptions:
    def __init__(self, driver):
        self.driver = driver
        self.url = Settings.BASE_URL + Routes.DROPDOWN.value
        #self.dropdown_options = self.driver.find_element(By.ID, 'dropdown')
        #self.dropdown = Select(self.dropdown_options)
        self.dropdown_options = None
        self.dropdown = None

    def navigate(self):
        self.driver.get(self.url)
        try:
            self.dropdown_options = WebDriverWait(self.driver, Settings.DEFAULT_TIMEOUT).until(
                EC.presence_of_element_located((By.ID, 'dropdown'))
            )
            self.dropdown_options = self.driver.find_element(By.ID, 'dropdown')
            self.dropdown = Select(self.dropdown_options)
        except TimeoutError:
            assert False, "Dropdown options not found on the page."

    def is_dropdown_option_1_selected(self):
        return self.dropdown.first_selected_option.text == "Option 1"

    def is_dropdown_option_2_selected(self):
        return self.dropdown.first_selected_option.text == "Option 2"

    def select_dropdown_option_1(self):
        self.dropdown.select_by_visible_text("Option 1")
        # self.dropdown.select_by_index(1)

    def select_dropdown_option_2(self):
        self.dropdown.select_by_visible_text("Option 2")
        # self.dropdown.select_by_index(2)