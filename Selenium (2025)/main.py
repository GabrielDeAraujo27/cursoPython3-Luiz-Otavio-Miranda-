import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'Drivers' /  'chromedriver-win64' / 'chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))

#chrome_options.add_argument('--headless')

chrome_browser = webdriver.Chrome (service=chrome_service, options=chrome_options)

chrome_browser.get('https://youtube.com')


search_input = WebDriverWait(chrome_browser, 10).until(EC.presence_of_element_located((By.NAME, 'search_query')))

search_input.send_keys('Hello World!')
search_input.send_keys(Keys.RETURN)

time.sleep(5)

results = chrome_browser.find_element(By.CLASS_NAME, 'style-scope ytd-video-renderer')
links = results.find_elements(By.TAG_NAME, 'a')
links[0].click()

time.sleep(10)