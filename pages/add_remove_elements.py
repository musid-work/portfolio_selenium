from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.settings import Settings
from config.routes import Routes


class SeleniumAddRemoveElements:
    def __init__(self, driver):
        self.driver = driver
        self.url = Settings.BASE_URL + Routes.ADD_REMOVE_ELEMENTS.value
        self.add_element = (By.CSS_SELECTOR, ".example button")
        self.delete_element = (By.CSS_SELECTOR, ".added-manually")

    def navigate(self):
        self.driver.get(self.url)

    def click_add_element(self):
        self.driver.find_element(*self.add_element).click()

    def get_delete_button(self, timeout=Settings.DEFAULT_TIMEOUT):
        # Using explicit waits to demonstrate professional synchronization skills
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.delete_element)
                )
            return True
        except TimeoutException:
            return False
