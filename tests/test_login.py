import pytest
from selenium import webdriver
from pages.login_page import SeleniumLoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

def test_successful_login(driver):
    login_page = SeleniumLoginPage(driver)
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")  # Valid test data
    
    assert "You logged into a secure area!" in login_page.get_flash_message_text()