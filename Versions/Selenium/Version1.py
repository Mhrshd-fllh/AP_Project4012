import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

#Mobile Scraping
driver.get('https://www.mobile.ir/phones/prices.aspx')
time.sleep(5)

dictionary = {}
This_Page = True
i = 1
page = 1
f = open('mobile_prices.txt', 'w')
while This_Page:
    try:
        name = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[{i}]/td[2]/a').text
        price = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[{i}]/td[3]/a').text
        link = driver.find_element(By.XPATH, f'//*[@id="price_table"]/tbody/tr[{i}]/td[2]/a').get_attribute('href')
        #dictionary[name] = price
        f.write(f'{name}: {price}: {link} \n')
        i+=1
        if i % 50 == 0:
            page += 1
            driver.get(f'https://www.mobile.ir/phones/prices.aspx?page={page}')
            i = 1
            time.sleep(3)
        
    except:
        break
f.close()
#print(dictionary)