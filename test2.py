from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)


#    input1 = browser.find_elements_by_css_selector('required')
    #input1 = browser.find_element_by_xpath("//input[@required]")
    inputs = browser.find_elements_by_css_selector('input[required]')
    for input in inputs:
        input.send_keys("Тест")

    time.sleep(1)
    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    w = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == w
finally:
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
