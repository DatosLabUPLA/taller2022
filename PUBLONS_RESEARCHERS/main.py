from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from collections import defaultdict, deque

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

driver.get('https://publons.com/researcher/?country=123&order_by=name')

lista_autores=[]

while len(lista_autores) < 250:

    a = (By.CSS_SELECTOR, '.table-container')
    wait = WebDriverWait(driver,30)
    df = wait.until(EC.element_to_be_clickable(a))
    for i in df.find_elements_by_tag_name('span'):
        if i.text != "":
            print(i.text)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


df = pd.DataFrame(lista_autores,columns=['idd'])
df.to_csv("lista_autores_251.csv")

import shutil
source = r'D:\TI2022\github\taller2022\PUBLONS_RESEARCHERS\lista_autores_251.csv'
destination = r'D:\TI2022\github\taller2022\PUBLONS_RESEARCHERS\DATA\lista_autores_251.csv'

shutil.move(source,destination)
    
time.sleep(5)

driver.quit();

