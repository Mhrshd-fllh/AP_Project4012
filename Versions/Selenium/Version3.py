from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv


driver = webdriver.Chrome()
driver.get('https://meghdadit.com/productlist/mobile/?im=true')
price_list = []
j = 1
page = 1
f = open('Meghdadit.csv', 'w')
for i in range(1, 114):
    price_String = driver.find_element(By.XPATH, f'/html/body/form/div[3]/div/div[3]/div/div[2]/article/div[1]/ul/li[{j}]/div/div[4]/div[2]/div/div/span').text
    price_tmp = []
    for s in price_String:
        if s.isdigit() or s ==',':
            if s == ',':
                price_tmp.append('.')
            price_tmp.append(s)
    for m in price_tmp:
        writer = csv.writer(f)
        writer.writerow(m)
    print()
    j+=1
    if i % 24 == 0:
        page += 1
        driver.get(f'https://meghdadit.com/productlist/mobile/?im=true&page={page}')
        j = 1