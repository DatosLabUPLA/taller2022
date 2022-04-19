import requests
import csv
from bs4 import BeautifulSoup as bs
import pandas as pd

def main():
    url="https://www.scimagojr.com/countryrank.php"
    scimago=requests.get(url)

    sopa=bs(scimago.text, 'lxml')

    sopa.find('div', attrs={'class':'ranking_body'})

    cazuela=sopa.find_all('td', class_='tit')
    paises=list()

    for i in cazuela:
        paises.append(i.text)

    ramen=sopa.find_all('div', class_='dentro_td')

    ndocu=list()
    for i in ramen:
        ndocu.append(i.text)
    
    minestrone=sopa.find_all('td', class_='cel_orde')

    prueba=list()
    test=sopa.find_all('td')
    for i in test:
        prueba.append(i.text)


    citables=[]

    for i in range(4,2156,9):
        citables.append(prueba[i])

    citaciones=[]

    for i in range(5,2157,9):
        citaciones.append(prueba[i])

    auto=[]

    for i in range(6,2158,9):
        auto.append(prueba[i])

    citapd=[]

    for i in range(7,2159,9):
        citapd.append(prueba[i])

    index=[]

    for i in range(8,2160,9):
        index.append(prueba[i])

    data=pd.DataFrame({'Pais':paises,'Numero de documentos':ndocu, 'Documentos Citables':citables, 'Citaciones':citaciones, 'Autocitas':auto, 'Citas por Documento':citapd, 'H index':index}, index=list(range(1,241)))
    print(data)
    data.to_csv("DATA/listado_paises.csv")

if __name__ == "__main__":
    main()