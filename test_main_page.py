from selenium.webdriver.common.by import By
import pytest

def test_check_add_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(buttons) == 1, "Кнопки 'Добавить в корзину' нет на странице"