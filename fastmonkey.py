from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui

monkeytype_url = 'https://monkeytype.com/'
driver_path = 'chromedriver_win32/chromedriver'
driver = webdriver.Chrome(service= Service(driver_path))
driver.maximize_window()
driver.get(monkeytype_url)
words = driver.find_element(By.ID, 'words').get_attribute('innerHTML')
words = BeautifulSoup(words, 'html.parser').find_all('div', 'word')
words = [word.text for word in words]
pyautogui.click(500, 500)

for _ in range(2):
        for word in words:
            pyautogui.write(word + ' ')
            pyautogui.sleep(0.2)
        words = driver.find_element(By.ID, 'words').get_attribute('innerHTML')
        words = BeautifulSoup(words, 'html.parser').find_all('div', 'word')
        words = [word.text for word in words]

driver.quit()