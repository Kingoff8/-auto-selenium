import time
import math
from selenium import webdriver

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)

    btn = browser.find_element_by_css_selector('.btn')
    btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)

    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)

    btn = browser.find_element_by_css_selector('.btn')
    btn.click()

finally:
    time.sleep(40)
    browser.quit()
