import pytest
from selenium import webdriver
from pages.dynamic_loading_page import SeleniumDynamicLoadingPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_element_loads_dynamically(driver):
    dynamic_page = SeleniumDynamicLoadingPage(driver)
    dynamic_page.navigate()
    dynamic_page.click_start()
    
    # Asserting that the loader disappears and text displays correctly
    assert dynamic_page.get_finish_text() == "Hello World!"