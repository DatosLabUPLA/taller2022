#!/usr/bin/env python
# coding: utf-8

# In[19]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_instituciones = []

#Página base
from requests_html import AsyncHTMLSession
asession = AsyncHTMLSession()
r = await asession.get("https://publons.com/institution/?order_by=num_researchers")
await r.html.arender(sleep=5) # Este llamado ejecuta los JS que se encuentran en la página

soup = BeautifulSoup(r.html.raw_html, 'html.parser') #parse (analizador)

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




