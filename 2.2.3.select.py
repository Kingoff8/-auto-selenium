import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'

def sum(num1, num2):
    return str(int(num1) + int(num2))

try:
    browser.get(link)

    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    num3 = sum(num1, num2)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_visible_text(num3)

    btn = browser.find_element_by_css_selector('.btn')
    btn.click()


finally:
    time.sleep(120)
    browser.quit()
