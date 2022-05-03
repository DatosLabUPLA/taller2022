import requests
from bs4 import BeautifulSoup
import pandas as pd
datos = []
data = []
# Universidad Autónoma de Chile = 6219877915722792561
# Universidad Adolfo Ibáñez = 10448777709790852446
# Universidad de los Andes = 6615366460316766280
# Universidad del Desarrollo = 4794720163447555879
# Universidad Andrés Bello = 13542589241086358186
# Universidad San Sebastián	= 1812728570911196340
# Universidad Santo Tomás = 14018219609791295521
# Pontificia Universidad Católica de Chile = 7459009050823923954
# Pontificia Universidad Católica de Valparaíso	= 7698552169257898503
# Universidad Austral de Chile = 16206413231987421209
# Universidad Alberto Hurtado = 15469411678705648791
# Universidad Católica del Maule = 12968600147058256171
# Universidad Católica del Norte = 17255630398072300451
# Universidad Católica de la Santísima Concepción = 3702576657308349741
# Universidad Católica de Temuco = 12740943834737827853
# Universidad de Concepción = 4555896482842878823
# Universidad Diego Portales = 12216913016116922734
# Universidad Técnica Federico Santa María = 9225498103198054248
# Universidad de Antofagasta = 7010446216104013295
# Universidad del Bío-Bío = 8365100606562762008
# Universidad de Chile = 9232372474901007921
# Universidad de la Frontera = 13908003347799972066
# Universidad de los Lagos = 13824009975929506544
# Universidad de la Serena = 6030355530770144394
# Universidad de Magallanes = 14351944662178497517
# Universidad Arturo Prat = 18273373707046377092
# Universidad de Playa Ancha de Ciencias de la Educación = 8337597745079551909
# Universidad de Santiago de Chile = 605437563739143535
# Universidad de Tarapacá = 4727335469935944428
# Universidad de Talca = 7732664165981901274
# Universidad de Valparaíso = 17388732461633852730

instituciones = {
    'UAC':'6219877915722792561',
    'UAI':'10448777709790852446',
    'UA':'6615366460316766280',
    'UD':'4794720163447555879',
    'UAB':'13542589241086358186',
    'USS':'1812728570911196340',
    'UST':'14018219609791295521',
    'UCC':'7459009050823923954',
    'UCV':'7698552169257898503',
    'UACH':'16206413231987421209',
    'UAH':'15469411678705648791',
    'UCM':'12968600147058256171',
    'UCN':'17255630398072300451',
    'UCSC':'3702576657308349741',
    'UCT':'12740943834737827853',
    'UC':'4555896482842878823',
    'UDP':'12216913016116922734',
    'UTFSM':'9225498103198054248',
    'UDA':'7010446216104013295',
    'UBB':'8365100606562762008',
    'UCH':'9232372474901007921',
    'UF':'13908003347799972066',
    'UL':'13824009975929506544',
    'US':'6030355530770144394',
    'UM':'14351944662178497517',
    'UAP':'18273373707046377092',
    'UPLA':'8337597745079551909',
    'USCH':'605437563739143535',
    'UT':'4727335469935944428',
    'UDT':'7732664165981901274',
    'UV':'17388732461633852730'
}

'''instituciones = {
    'UAC':'6219877915722792561',
    'UAI':'10448777709790852446'
}'''

for id in instituciones.values():
    url="https://scholar.google.cl/citations?view_op=view_org&org=" + id 
    data.append(url)

#print(data)

for urls in data:
    
    response=requests.get(urls)

    soup=BeautifulSoup(response.text,'html.parser')

    autor=soup.findAll('div',class_='gs_ai_t')

    for autores in autor:
        persona = autores.find(class_='gs_ai_name').text
        universidad = autores.find(class_ = 'gs_ai_aff').text
        correo = autores.find(class_='gs_ai_eml').text
        intereses = autores.find(class_='gs_ai_int').text
        citas = autores.find(class_='gs_ai_cby').text
        datos.append([persona,universidad,correo,intereses,citas])
    #print(autores)

    datas =  pd.DataFrame(datos, columns=['Autor','Universidad','Correo','Intereses','Cant Citas'])
    datas.to_csv('autores.csv', index=False)
    print(datas)

