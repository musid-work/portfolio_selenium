from tabnanny import check

import pytest
from selenium import webdriver
from pages.check_boxes import SeleniumCheckBoxes

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

@pytest.mark.checkboxes_initialization
def test_checkboxes_initialization(driver):
    check_boxes = SeleniumCheckBoxes(driver)
    check_boxes.navigate()
    #chechkboxes = check_boxes.get_checkboxes()
    #assert len(chechkboxes) == 2, "There should be exactly two checkboxes on the page."

    assert not check_boxes.is_checkbox_1_selected(), "Checkbox 1 should be initially unchecked."
    assert check_boxes.is_checkbox_2_selected(), "Checkbox 2 should be initially checked."

@pytest.mark.toggle_checkbox_1
def test_toggle_checkbox_1(driver):
    check_boxes = SeleniumCheckBoxes(driver)
    check_boxes.navigate()

    # Toggle Checkbox 1
    check_boxes.toggle_checkbox_1()
    assert check_boxes.is_checkbox_1_selected(), "Checkbox 1 should be checked after toggling."

    # Toggle Checkbox 1 again to uncheck it
    check_boxes.toggle_checkbox_1()
    assert not check_boxes.is_checkbox_1_selected(), "Checkbox 1 should be unchecked after toggling again."


@pytest.mark.toggle_checkbox_2
def test_toggle_checkbox_2(driver):
    check_boxes = SeleniumCheckBoxes(driver)
    check_boxes.navigate()

    # Toggle Checkbox 2
    check_boxes.toggle_checkbox_2()
    assert not check_boxes.is_checkbox_2_selected(), "Checkbox 2 should be unchecked after toggling."

    # Toggle Checkbox 2 again to check it
    check_boxes.toggle_checkbox_2()
    assert check_boxes.is_checkbox_2_selected(), "Checkbox 2 should be checked after toggling again."