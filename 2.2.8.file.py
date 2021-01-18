import os
import time
from selenium import webdriver

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser.get(link)

    texts = browser.find_elements_by_css_selector('[type="text"]')

    for text in texts:
        text.send_keys('Тест')

    load = browser.find_element_by_css_selector('[type="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'load.txt')           # добавляем к этому пути имя файла
    load.send_keys(file_path)

    btn = browser.find_element_by_css_selector('.btn')
    btn.click()
finally:
    time.sleep(30)
    browser.quit()
