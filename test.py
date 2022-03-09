
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/usr/local/bin/chromedriver"
driver_path = '/Users/mb/Documents/TSI_Projekt/stock_rsi/chromedriver.exe'
driver = webdriver.Chrome("/Users/mb/Documents/TSI_Projekt/stock_rsi/.venv/lib/python3.8/site-packages/selenium/webdriver/chrome/chromedriver", chrome_options=options)
driver.get('https://www.google.com/')
breakpoint()