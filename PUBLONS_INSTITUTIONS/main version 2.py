#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

lista_instituciones = []

#Página base
options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options, executable_path='geckodriver')
driver.get("https://publons.com/institution/?order_by=num_researchers")

SCROLL_PAUSE_TIME = 1.5
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
print('Scrolling hasta el final de la pagina...', end='')
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    print('.', end='')

print('\n')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


#Bloque donde se encuentra cada institución
inst = soup.findAll('div', attrs={"class":'flex-row'})

#iteración para obtener los datos que queremos extraer
for institucion in inst:
    try:
        nombre = institucion.find('a', attrs={"class":"inst"}).get_text(strip=True)
        investigadores = institucion.find('div', attrs={"class":"total-researchers"}).get_text(strip=True)
        verificado = institucion.find('div', attrs={"class":"top-reviewers"}).get_text(strip=True)
        publicacion = institucion.find('div', attrs={"class":"total-reviews"}).get_text(strip=True)

        lista_instituciones.append([nombre,investigadores,verificado,publicacion])
        print([nombre,investigadores,verificado,publicacion])
    except:
        pass

#Generar dataframe
lista = pd.DataFrame(lista_instituciones, columns=['Nombre Institución', 'Investigadores', 'Número de Reseñas Verificadas', 'Número de Publicaciones'])

lista.to_csv('DATA/instituciones.csv', index=False)


# In[ ]:




