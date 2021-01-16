from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element_by_css_selector("div.first_block > div.first_class > input.first")
    input.send_keys('Тест')

    input2 = browser.find_element_by_css_selector("div.first_block > div.second_class > input.second")
    input2.send_keys('Тест2')

    input3 = browser.find_element_by_css_selector("div.first_block > div.third_class > input.third")
    input3.send_keys('Тест3')


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
    # номер моего решения Решение #349273427
