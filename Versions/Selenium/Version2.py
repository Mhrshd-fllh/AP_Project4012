#Digikala Mobile
import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
from googletrans import Translator, constants

translator = Translator()

driver = webdriver.Chrome()
driver.get('https://www.digikala.com/search/category-mobile-phone/product-list/')
time.sleep(5)
screen = driver.find_element(By.XPATH, '//html')
f = open('Digikala_Mobile_Prices.txt', 'w')
for i in range(1, 50):
   
    temp = unidecode(driver.find_element(By.XPATH, f'//*[@id="ProductListPagesWrapper"]/section[1]/div[2]/div[{i}]/a/div/article/div[2]/div[2]/div[4]/div[1]/div/span').text)
    if '%' in temp:
        temp = unidecode(driver.find_element(By.XPATH, f'//*[@id="ProductListPagesWrapper"]/section[1]/div[2]/div[{i}]/a/div/article/div[2]/div[2]/div[4]/div[1]/div[2]/span').text)
    elif temp == 'nmwjwd':
        continue
    else:
        temp_name = translator.translate(driver.find_element(By.XPATH, f'//*[@id="ProductListPagesWrapper"]/section[1]/div[2]/div[{i}]/a/div/article/div[2]/div[2]/div[2]/h3').text)
        print(temp_name)
        f.write(f'{temp_name.text}: {temp}\n')
    if i % 4 == 0:
        screen.send_keys(Keys.SPACE)
        screen.send_keys(Keys.SPACE)
        screen.send_keys(Keys.SPACE)
        time.sleep(4)  


