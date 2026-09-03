import pytest
from selenium import webdriver
from pages.add_remove_elements import SeleniumAddRemoveElements

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.add_remove_element
def test_add_remove_element(driver):
    add_remove_element_page = SeleniumAddRemoveElements(driver)
    add_remove_element_page.navigate()
    add_remove_element_page.click_add_element()
    
    # Asserting that the loader disappears and text displays correctly
    assert add_remove_element_page.get_delete_button()