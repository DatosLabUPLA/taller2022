import requests
from bs4 import BeautifulSoup
import pandas as pd
datos = []

url="https://scholar.google.cl/citations?view_op=view_org&org=8337597745079551909&hl=es&oi=io"

response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')

autor=soup.findAll('div',class_='gs_ai_t')

for autores in autor:
    persona = autores.find(class_='gs_ai_name').text
    universidad = autores.find(class_ = 'gs_ai_aff').text
    correo = autores.find(class_='gs_ai_eml').text
    intereses = autores.find(class_='gs_ai_one_int').text
    citas = autores.find(class_='gs_ai_cby').text
    datos.append([persona,universidad,correo,intereses,citas])

data =  pd.DataFrame(datos, columns=['Autor','Universidad','Correo','Intereses','Cant Citas'])
data.to_csv('autores.csv', index=False)




