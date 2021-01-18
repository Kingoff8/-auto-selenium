from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    button = WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    btn = browser.find_element_by_css_selector('.btn')
    btn.click()

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)

    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)

    sbm = browser.find_element_by_css_selector('[type="submit"]')
    sbm.click()

finally:
        time.sleep(3)
        browser.quit()
