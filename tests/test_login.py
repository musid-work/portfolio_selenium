import pytest
from selenium import webdriver
from pages.login_page import SeleniumLoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

@pytest.mark.successful_login
def test_successful_login(driver):
    login_page = SeleniumLoginPage(driver)
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")  # Valid test data
    
    assert "You logged into a secure area!" in login_page.get_flash_message_text()

@pytest.mark.login_invalid_user_valid_password
def test_login_invalid_user_valid_password(driver):
    login_page = SeleniumLoginPage(driver)
    login_page.navigate()
    login_page.login("InvalidUser", "SuperSecretPassword!")  # Invalid test data
    
    assert "Your username is invalid!" in login_page.get_flash_message_text()

@pytest.mark.login_valid_user_invalid_password
def test_login_valid_user_invalid_password(driver):
    login_page = SeleniumLoginPage(driver)
    login_page.navigate()
    login_page.login("tomsmith", "InvalidPassword")  # Invalid test data

    assert "Your password is invalid!" in login_page.get_flash_message_text()

@pytest.mark.login_invalid_user_invalid_password
def test_login_invalid_user_invalid_password(driver):
    login_page = SeleniumLoginPage(driver)
    login_page.navigate()
    login_page.login("InvalidUser", "InvalidPassword")  # Invalid test data

    assert "Your username is invalid!" in login_page.get_flash_message_text()
