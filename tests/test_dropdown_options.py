from tabnanny import check

import pytest
from selenium import webdriver
from pages.dropdown_options import SeleniumDropdownOptions

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

@pytest.mark.dropdown_options_initialization
def test_dropdown_options_initialization(driver):
    dropdown_options = SeleniumDropdownOptions(driver)
    dropdown_options.navigate()
    #chechkboxes = check_boxes.get_checkboxes()
    #assert len(chechkboxes) == 2, "There should be exactly two checkboxes on the page."

    assert not dropdown_options.is_dropdown_option_1_selected(), "Dropdown Option 1 should be initially not selected."
    assert not dropdown_options.is_dropdown_option_2_selected(), "Dropdown Option 2 should be initially not selected."

@pytest.mark.select_dropdown_option_1
def test_select_dropdown_option_1(driver):
    dropdown_options = SeleniumDropdownOptions(driver)
    dropdown_options.navigate()

    # Select Dropdown Option 1
    dropdown_options.select_dropdown_option_1()
    assert dropdown_options.is_dropdown_option_1_selected(), "Dropdown Option 1 should be selected after selection."

@pytest.mark.select_dropdown_option_2
def test_select_dropdown_option_2(driver):
    dropdown_options = SeleniumDropdownOptions(driver)
    dropdown_options.navigate()

    # Select Dropdown Option 2
    dropdown_options.select_dropdown_option_2()
    assert dropdown_options.is_dropdown_option_2_selected(), "Dropdown Option 2 should be selected after selection."

