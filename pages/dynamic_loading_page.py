from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumDynamicLoadingPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/dynamic_loading/1"
        self.start_button = (By.CSS_SELECTOR, "#start button")
        self.finish_text = (By.CSS_SELECTOR, "#finish h4")

    def navigate(self):
        self.driver.get(self.url)

    def click_start(self):
        self.driver.find_element(*self.start_button).click()

    def get_finish_text(self, timeout=10):
        # Using explicit waits to demonstrate professional synchronization skills
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.finish_text)
        )
        return element.text