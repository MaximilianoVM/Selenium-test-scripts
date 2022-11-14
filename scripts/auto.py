# selenium 3
from ast import Bytes
from turtle import title
from unicodedata import name
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.google.com')
driver.find_element(By.XPATH , "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("auxilio")

time.sleep(200)
