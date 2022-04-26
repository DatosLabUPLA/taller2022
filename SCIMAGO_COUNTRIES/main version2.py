import requests
import csv
from bs4 import BeautifulSoup as bs
import pandas as pd

def main():
    url_abs1="https://www.scimagojr.com/countryrank.php?area=1100&category=1101"
    url_abs2="https://www.scimagojr.com/countryrank.php?area=1100&category=1102"
    url_abs3="https://www.scimagojr.com/countryrank.php?area=1100&category=1103"
    url_abs4="https://www.scimagojr.com/countryrank.php?area=1100&category=1104"
    url_abs5="https://www.scimagojr.com/countryrank.php?area=1100&category=1105"
    url_abs6="https://www.scimagojr.com/countryrank.php?area=1100&category=1106"
    url_abs7="https://www.scimagojr.com/countryrank.php?area=1100&category=1107"
    url_abs8="https://www.scimagojr.com/countryrank.php?area=1100&category=1108"
    url_abs9="https://www.scimagojr.com/countryrank.php?area=1100&category=1109"
    url_abs10="https://www.scimagojr.com/countryrank.php?area=1100&category=1110"
    url_abs11="https://www.scimagojr.com/countryrank.php?area=1100&category=1111"
    scimago_abs1=requests.get(url_abs1)
    scimago_abs2=requests.get(url_abs2)
    scimago_abs3=requests.get(url_abs3)
    scimago_abs4=requests.get(url_abs4)
    scimago_abs5=requests.get(url_abs5)
    scimago_abs6=requests.get(url_abs6)
    scimago_abs7=requests.get(url_abs7)
    scimago_abs8=requests.get(url_abs8)
    scimago_abs9=requests.get(url_abs9)
    scimago_abs10=requests.get(url_abs10)
    scimago_abs11=requests.get(url_abs11)

    sopa1=bs(scimago_abs1.text, 'lxml')
    sopa2=bs(scimago_abs2.text, 'lxml')
    sopa3=bs(scimago_abs3.text, 'lxml')
    sopa4=bs(scimago_abs4.text, 'lxml')
    sopa5=bs(scimago_abs5.text, 'lxml')
    sopa6=bs(scimago_abs6.text, 'lxml')
    sopa7=bs(scimago_abs7.text, 'lxml')
    sopa8=bs(scimago_abs8.text, 'lxml')
    sopa9=bs(scimago_abs9.text, 'lxml')
    sopa10=bs(scimago_abs10.text, 'lxml')
    sopa11=bs(scimago_abs11.text, 'lxml')

    sopa1.find('div', attrs={'class':'ranking_body'})

    pais=sopa1.find_all('td', class_='tit')


    paises=list()

    for i in pais:
        paises.append(i.text)

    area_code=[]
    for i in range(1,221):
        area_code.insert(i,1100)

    category_code=[]
    for i in range(1,221):
        category_code.insert(i,1101)
    documents=sopa1.find_all('div', class_='dentro_td')
    ndocu=list()
    for i in documents:
        ndocu.append(i.text)

    prueba=list()
    test=sopa1.find_all('td')
    for i in test:
        prueba.append(i.text)

    citables=[]

    for i in range(4,1976,9):
        citables.append(prueba[i])

    citaciones=[]

    for i in range(5,1977,9):
        citaciones.append(prueba[i])

    auto=[]

    for i in range(6,1978,9):
        auto.append(prueba[i])

    citapd=[]

    for i in range(7,1979,9):
        citapd.append(prueba[i])

    index=[]

    for i in range(8,1980,9):
        index.append(prueba[i])

    data_abs=pd.DataFrame({'Pais':paises, 'Area':area_code, 'Categoria':category_code, 'Numero de Documentos':ndocu, 'Documentos citables':citables, 'Citaciones':citaciones, 'Autocitas':auto, 'Citas por documento':citapd, 'H index':index})

    sopa2.find('div', attrs={'class':'ranking_body'})
    pais2=sopa2.find_all('td', class_='tit')
    paises2=list()

    for i in pais2:
        paises2.append(i.text)

    area_code2=[]

    for i in range(1,212):
        area_code2.insert(i,1100)

    category_code2=[]
    for i in range(1,212):
        category_code2.insert(i,1102)

    documents2=sopa2.find_all('div', class_='dentro_td')

    ndocu2=list()
    for i in documents2:
        ndocu2.append(i.text)

    prueba2=list()
    test2=sopa2.find_all('td')
    for i in test2:
        prueba2.append(i.text)

    citables2=[]

    for i in range(4,1895,9):
        citables2.append(prueba2[i])

    citaciones2=[]

    for i in range(5,1896,9):
        citaciones2.append(prueba2[i])

    auto2=[]

    for i in range(6,1897,9):
        auto2.append(prueba2[i])

    citapd2=[]

    for i in range(7,1898,9):
        citapd2.append(prueba2[i])

    index2=[]

    for i in range(8,1899,9):
        index2.append(prueba2[i])
    
    data_abs2=pd.DataFrame({'Pais':paises2, 'Area':area_code2, 'Categoria':category_code2, 'Numero de Documentos':ndocu2, 'Documentos citables':citables2, 'Citaciones':citaciones2, 'Autocitas':auto2, 'Citas por documento':citapd2, 'H index':index2})

    sopa3.find('div', attrs={'class':'ranking_body'})
    pais3=sopa3.find_all('td', class_='tit')

    paises3=list()

    for i in pais3:
        paises3.append(i.text)

    area_code3=[]

    for i in range(1,228):
        area_code3.insert(i,1100)

    category_code3=[]
    for i in range(1,228):
        category_code3.insert(i,1103)

    documents3=sopa3.find_all('div', class_='dentro_td')

    ndocu3=list()
    for i in documents3:
        ndocu3.append(i.text)

    prueba3=list()
    test3=sopa3.find_all('td')
    for i in test3:
        prueba3.append(i.text)

    citables3=[]

    for i in range(4,2039,9):
        citables3.append(prueba3[i])

    citaciones3=[]

    for i in range(5,2040,9):
        citaciones3.append(prueba3[i])

    auto3=[]

    for i in range(6,2041,9):
        auto3.append(prueba3[i])

    citapd3=[]

    for i in range(7,2042,9):
        citapd3.append(prueba3[i])

    index3=[]

    for i in range(8,2043,9):
        index3.append(prueba3[i])

    data_abs3=pd.DataFrame({'Pais':paises3, 'Area':area_code3, 'Categoria':category_code3, 'Numero de Documentos':ndocu3, 'Documentos citables':citables3, 'Citaciones':citaciones3, 'Autocitas':auto3, 'Citas por documento':citapd3, 'H index':index3})

    sopa4.find('div', attrs={'class':'ranking_body'})
    pais4=sopa4.find_all('td', class_='tit')

    paises4=list()

    for i in pais4:
        paises4.append(i.text)
    print(pd.DataFrame(paises4))
    area_code4=[]
    for i in range(1,227):
        area_code4.insert(i,1100)
    
    category_code4=[]
    for i in range(1,227):
        category_code4.insert(i,1104)
    
    documents4=sopa4.find_all('div', class_='dentro_td')

    ndocu4=list()
    for i in documents4:
        ndocu4.append(i.text)
    
    
    prueba4=list()
    test4=sopa4.find_all('td')
    for i in test4:
        prueba4.append(i.text)


    citables4=[]

    for i in range(4,2030,9):
        citables4.append(prueba4[i])
    citaciones4=[]

    for i in range(5,2031,9):
        citaciones4.append(prueba4[i])
    auto4=[]

    for i in range(6,2032,9):
        auto4.append(prueba4[i])
    
    citapd4=[]

    for i in range(7,2033,9):
        citapd4.append(prueba4[i])

    index4=[]

    for i in range(8,2034,9):
        index4.append(prueba4[i])


    data_abs4=pd.DataFrame({'Pais':paises4, 'Area':area_code4, 'Categoria':category_code4, 
    'Numero de Documentos':ndocu4, 'Documentos citables':citables4, 'Citaciones':citaciones4, 'Autocitas':auto4, 'Citas por documento':citapd4, 'H index':index4})

    sopa5.find('div', attrs={'class':'ranking_body'})
    pais5=sopa5.find_all('td', class_='tit')
    paises5=list()

    for i in pais5:
        paises5.append(i.text)

    area_code5=[]
    for i in range(1,233):
        area_code5.insert(i,1100)

    category_code5=[]
    for i in range(1,233):
        category_code5.insert(i,1105)

    documents5=sopa5.find_all('div', class_='dentro_td')

    ndocu5=list()
    for i in documents5:
        ndocu5.append(i.text)

    prueba5=list()
    test5=sopa5.find_all('td')
    for i in test5:
        prueba5.append(i.text)

    citables5=[]

    for i in range(4,2084,9):
        citables5.append(prueba5[i])

    citaciones5=[]

    for i in range(5,2085,9):
        citaciones5.append(prueba5[i])

        auto5=[]

    for i in range(6,2086,9):
        auto5.append(prueba5[i])

    citapd5=[]

    for i in range(7,2087,9):
        citapd5.append(prueba5[i])

    index5=[]

    for i in range(8,2088,9):
        index5.append(prueba5[i])

    data_abs5=pd.DataFrame({'Pais':paises5, 'Area':area_code5, 'Categoria':category_code5, 'Numero de Documentos':ndocu5, 'Documentos citables':citables5, 'Citaciones':citaciones5, 'Autocitas':auto5, 'Citas por documento':citapd5, 'H index':index5})

    sopa6.find('div', attrs={'class':'ranking_body'})
    pais6=sopa6.find_all('td', class_='tit')
    paises6=list()

    for i in pais6:
        paises6.append(i.text)

    area_code6=[]
    for i in range(1,214):
        area_code6.insert(i,1100)

    category_code6=[]
    for i in range(1,214):
        category_code6.insert(i,1106)

    documents6=sopa6.find_all('div', class_='dentro_td')

    ndocu6=list()
    for i in documents6:
        ndocu6.append(i.text)

    prueba6=list()
    test6=sopa6.find_all('td')
    for i in test6:
        prueba6.append(i.text)

    citables6=[]

    for i in range(4,1913,9):
        citables6.append(prueba6[i])

    citaciones6=[]

    for i in range(5,1914,9):
        citaciones6.append(prueba6[i])

    auto6=[]

    for i in range(6,1915,9):
        auto6.append(prueba6[i])

    citapd6=[]

    for i in range(7,1916,9):
        citapd6.append(prueba6[i])

    index6=[]

    for i in range(8,1917,9):
        index6.append(prueba6[i])

    data_abs6=pd.DataFrame({'Pais':paises6, 'Area':area_code6, 'Categoria':category_code6, 'Numero de Documentos':ndocu6, 'Documentos citables':citables6, 'Citaciones':citaciones6, 'Autocitas':auto6, 'Citas por documento':citapd6, 'H index':index6})

    sopa7.find('div', attrs={'class':'ranking_body'})
    pais7=sopa7.find_all('td', class_='tit')

    paises7=list()

    for i in pais7:
        paises7.append(i.text)
    area_code7=[]
    for i in range(1,209):
        area_code7.insert(i,1100)
    category_code7=[]
    for i in range(1,209):
        category_code7.insert(i,1107)
    documents7=sopa7.find_all('div', class_='dentro_td')
    ndocu7=list()
    for i in documents7:
        ndocu7.append(i.text)
    prueba7=list()
    test7=sopa7.find_all('td')
    for i in test7:
        prueba7.append(i.text)
    citables7=[]

    for i in range(4,1868,9):
        citables7.append(prueba7[i])

    citaciones7=[]

    for i in range(5,1869,9):
        citaciones7.append(prueba7[i])

    auto7=[]

    for i in range(6,1870,9):
        auto7.append(prueba7[i])

    citapd7=[]

    for i in range(7,1871,9):
        citapd7.append(prueba7[i])

    index7=[]
    for i in range(8,1872,9):
        index7.append(prueba7[i])

    data_abs7=pd.DataFrame({'Pais':paises7, 'Area':area_code7, 'Categoria':category_code7, 'Numero de Documentos':ndocu7, 'Documentos citables':citables7, 'Citaciones':citaciones7, 'Autocitas':auto7, 'Citas por documento':citapd7, 'H index':index7})
    
    sopa8.find('div', attrs={'class':'ranking_body'})
    pais8=sopa8.find_all('td', class_='tit')

    paises8=list()

    for i in pais8:
        paises8.append(i.text)

    area_code8=[]
    for i in range(1,203):
        area_code8.insert(i,1100)

    category_code8=[]
    for i in range(1,203):
        category_code8.insert(i,1108)

    documents8=sopa8.find_all('div', class_='dentro_td')

    ndocu8=list()
    for i in documents8:
        ndocu8.append(i.text)

    prueba8=list()
    test8=sopa8.find_all('td')
    for i in test8:
        prueba8.append(i.text)

    citables8=[]

    for i in range(4,1814,9):
        citables8.append(prueba8[i])

    citaciones8=[]

    for i in range(5,1815,9):
        citaciones8.append(prueba8[i])

    auto8=[]

    for i in range(6,1816,9):
        auto8.append(prueba8[i])

    citapd8=[]

    for i in range(7,1817,9):
        citapd8.append(prueba8[i])

    index8=[]

    for i in range(8,1818,9):
        index8.append(prueba8[i])

    data_abs8=pd.DataFrame({'Pais':paises8, 'Area':area_code8, 'Categoria':category_code8, 'Numero de Documentos':ndocu8, 'Documentos citables':citables8, 'Citaciones':citaciones8, 'Autocitas':auto8, 'Citas por documento':citapd8, 'H index':index8})

    sopa9.find('div', attrs={'class':'ranking_body'})
    pais9=sopa9.find_all('td', class_='tit')
    paises9=list()

    for i in pais9:
        paises9.append(i.text)

    area_code9=[]
    for i in range(1,215):
        area_code9.insert(i,1100)

    category_code9=[]
    for i in range(1,215):
        category_code9.insert(i,1109)

    documents9=sopa9.find_all('div', class_='dentro_td')

    ndocu9=list()
    for i in documents9:
        ndocu2.append(i.text)

    prueba9=list()
    test9=sopa9.find_all('td')
    for i in test9:
        prueba9.append(i.text)

    citables9=[]

    for i in range(4,1922,9):
        citables9.append(prueba9[i])

    citaciones9=[]

    for i in range(5,1923,9):
        citaciones9.append(prueba9[i])

    auto9=[]

    for i in range(6,1924,9):
        auto9.append(prueba9[i])

    citapd9=[]

    for i in range(7,1925,9):
        citapd9.append(prueba9[i])

    index9=[]

    for i in range(8,1926,9):
        index9.append(prueba9[i])

    data_abs9=pd.DataFrame({'Pais':paises9, 'Area':area_code9, 'Categoria':category_code9, 'Numero de Documentos':ndocu9, 'Documentos citables':citables9, 'Citaciones':citaciones9, 'Autocitas':auto9, 'Citas por documento':citapd9, 'H index':index9})


    sopa10.find('div', attrs={'class':'ranking_body'})
    pais10=sopa10.find_all('td', class_='tit')

    paises10=list()

    for i in pais10:
        paises10.append(i.text)

    area_code10=[]
    for i in range(1,221):
        area_code10.insert(i,1100)

    category_code10=[]
    for i in range(1,221):
        category_code10.insert(i,1110)
    documents10=sopa10.find_all('div', class_='dentro_td')

    ndocu10=list()
    for i in documents10:
        ndocu10.append(i.text)

    prueba10=list()
    test2=sopa10.find_all('td')
    for i in test2:
        prueba10.append(i.text)

    citables10=[]

    for i in range(4,1976,9):
        citables10.append(prueba10[i])

    citaciones10=[]

    for i in range(5,1977,9):
        citaciones10.append(prueba10[i])

    auto10=[]

    for i in range(6,1978,9):
        auto10.append(prueba10[i])

    citapd10=[]

    for i in range(7,1979,9):
        citapd10.append(prueba10[i])

    index10=[]

    for i in range(8,1980,9):
        index10.append(prueba10[i])

    data_abs10=pd.DataFrame({'Pais':paises10, 'Area':area_code10, 'Categoria':category_code10, 'Numero de Documentos':ndocu10, 'Documentos citables':citables10, 'Citaciones':citaciones10, 'Autocitas':auto10, 'Citas por documento':citapd10, 'H index':index10})

    sopa11.find('div', attrs={'class':'ranking_body'})
    pais11=sopa11.find_all('td', class_='tit')

    paises11=list()

    for i in pais11:
        paises11.append(i.text)

    area_code11=[]
    for i in range(1,206):
        area_code11.insert(i,1100)

    category_code11=[]
    for i in range(1,206):
        category_code11.insert(i,1111)
    documents11=sopa11.find_all('div', class_='dentro_td')
    ndocu11=list()
    for i in documents11:
        ndocu11.append(i.text)

    prueba11=list()
    test11=sopa11.find_all('td')
    for i in test11:
        prueba11.append(i.text)

    citables11=[]

    for i in range(4,1841,9):
        citables11.append(prueba11[i])

    citaciones11=[]

    for i in range(5,1842,9):
        citaciones11.append(prueba11[i])

    auto11=[]

    for i in range(6,1843,9):
        auto11.append(prueba11[i])

    citapd11=[]

    for i in range(7,1844,9):
        citapd11.append(prueba11[i])

    index11=[]

    for i in range(8,1845,9):
        index11.append(prueba11[i])

    data_abs11=pd.DataFrame({'Pais':paises11, 'Area':area_code11, 'Categoria':category_code11, 'Numero de Documentos':ndocu11, 'Documentos citables':citables11, 'Citaciones':citaciones11, 'Autocitas':auto11, 'Citas por documento':citapd11, 'H index':index11})
    
    abs=pd.concat([data_abs, data_abs2, data_abs3, data_abs4, data_abs5, data_abs6, data_abs7, data_abs8, data_abs9, data_abs10, data_abs11], axis=0)

    url_vet='https://www.scimagojr.com/countryrank.php?area=3400&category=3401'
    url_vet2='https://www.scimagojr.com/countryrank.php?area=3400&category=3402'
    url_vet3='https://www.scimagojr.com/countryrank.php?area=3400&category=3403'
    url_vet4='https://www.scimagojr.com/countryrank.php?area=3400&category=3404'

    scimago_vet=requests.get(url_vet)
    scimago_vet2=requests.get(url_vet2)
    scimago_vet3=requests.get(url_vet3)
    scimago_vet4=requests.get(url_vet4)

    sopavet=bs(scimago_vet.text, 'lxml')
    sopavet2=bs(scimago_vet2.text, 'lxml')
    sopavet3=bs(scimago_vet3.text, 'lxml')
    sopavet4=bs(scimago_vet4.text, 'lxml')

    sopavet.find('div', attrs={'class':'ranking_body'})
    sopavet2.find('div', attrs={'class':'ranking_body'})
    sopavet3.find('div', attrs={'class':'ranking_body'})
    sopavet4.find('div', attrs={'class':'ranking_body'})

    paisvet=sopavet.find_all('td', class_='tit')
    paisvet2=sopavet2.find_all('td', class_='tit')
    paisvet3=sopavet3.find_all('td', class_='tit')
    paisvet4=sopavet4.find_all('td', class_='tit')

    paisesvet=list()
    paisesvet2=list()
    paisesvet3=list()
    paisesvet4=list()

    for i in paisvet:
        paisesvet.append(i.text)

    for i in paisvet2:
        paisesvet2.append(i.text)

    for i in paisvet3:
        paisesvet3.append(i.text)

    for i in paisvet4:
        paisesvet4.append(i.text)

    paisesvetfinal=paisesvet+paisesvet2+paisesvet3+paisesvet4

    area_codevet=[]
    for i in range(1,647):
        area_codevet.insert(i,3400)

    category_codevet=[]
    for i in range(1,220):
        category_codevet.insert(i,3401)

    category_codevet2=[]
    for i in range(1,118):
        category_codevet2.insert(i,3402)

    category_codevet3=[]
    for i in range(1,184):
        category_codevet3.insert(i,3403)

    category_codevet4=[]
    for i in range(1,128):
        category_codevet4.insert(i,3404)

    category_codevetfinal=category_codevet+category_codevet2+category_codevet3+category_codevet4

    documentsvet=sopavet.find_all('div', class_='dentro_td')
    documentsvet2=sopavet2.find_all('div', class_='dentro_td')
    documentsvet3=sopavet3.find_all('div', class_='dentro_td')
    documentsvet4=sopavet4.find_all('div', class_='dentro_td')

    ndocuvet=list()
    for i in documentsvet:
        ndocuvet.append(i.text)

    ndocuvet2=list()
    for i in documentsvet2:
        ndocuvet2.append(i.text)

    ndocuvet3=list()
    for i in documentsvet3:
        ndocuvet3.append(i.text)

    ndocuvet4=list()
    for i in documentsvet4:
        ndocuvet4.append(i.text)

    ndocuvetfinal=ndocuvet+ndocuvet2+ndocuvet3+ndocuvet4


    pruebavet=list()
    testvet=sopavet.find_all('td')
    for i in testvet:
        pruebavet.append(i.text)

    pruebavet2=list()
    testvet2=sopavet2.find_all('td')
    for i in testvet2:
        pruebavet2.append(i.text)

    pruebavet3=list()
    testvet3=sopavet3.find_all('td')
    for i in testvet3:
        pruebavet3.append(i.text)

    pruebavet4=list()
    testvet4=sopavet4.find_all('td')
    for i in testvet4:
        pruebavet4.append(i.text)

    citablesvet=[]

    for i in range(4,1967,9):
        citablesvet.append(pruebavet[i])

    citablesvet2=[]

    for i in range(4,1049,9):
        citablesvet2.append(pruebavet2[i])

    citablesvet3=[]

    for i in range(4,1643,9):
        citablesvet3.append(pruebavet3[i])

    citablesvet4=[]

    for i in range(4,1139,9):
        citablesvet4.append(pruebavet4[i])

    citablesvetfinal=citablesvet+citablesvet2+citablesvet3+citablesvet4

    citacionesvet=[]

    for i in range(5,1968,9):
        citacionesvet.append(pruebavet[i])

    citacionesvet2=[]

    for i in range(5,1050,9):
        citacionesvet2.append(pruebavet2[i])

    citacionesvet3=[]

    for i in range(5,1644,9):
        citacionesvet3.append(pruebavet3[i])

    citacionesvet4=[]

    for i in range(5,1140,9):
        citacionesvet4.append(pruebavet4[i])

    citacionesfinal=citacionesvet+citacionesvet2+citacionesvet3+citacionesvet4

    autovet=[]

    for i in range(6,1969,9):
        autovet.append(pruebavet[i])

    autovet2=[]

    for i in range(6,1051,9):
        autovet2.append(pruebavet2[i])

    autovet3=[]

    for i in range(6,1645,9):
        autovet3.append(pruebavet3[i])

    autovet4=[]

    for i in range(6,1141,9):
        autovet4.append(pruebavet4[i])

    autofinal=autovet+autovet2+autovet3+autovet4

    citapdvet=[]

    for i in range(7,1970,9):
        citapdvet.append(pruebavet[i])

    citapdvet2=[]

    for i in range(7,1052,9):
        citapdvet2.append(pruebavet2[i])

    citapdvet3=[]

    for i in range(7,1646,9):
        citapdvet3.append(pruebavet3[i])

    citapdvet4=[]

    for i in range(7,1142,9):
        citapdvet4.append(pruebavet4[i])

    citapdfinal=citapdvet+citapdvet2+citapdvet3+citapdvet4

    indexvet=[]

    for i in range(8,1971,9):
        indexvet.append(pruebavet[i])

    indexvet2=[]

    for i in range(8,1053,9):
        indexvet2.append(pruebavet2[i])

    indexvet3=[]

    for i in range(8,1647,9):
        indexvet3.append(pruebavet3[i])

    indexvet4=[]

    for i in range(8,1143,9):
        indexvet4.append(pruebavet4[i])

    indexfinal=indexvet+indexvet2+indexvet3+indexvet4

    data_vet=pd.DataFrame({'Pais':paisesvetfinal, 'Area':area_codevet, 'Categoria':category_codevetfinal, 'Numero de Documentos':ndocuvetfinal, 'Documentos citables':citablesvetfinal, 'Citaciones':citacionesfinal, 'Autocitas':autofinal, 'Citas por documento':citapdfinal, 'H index':indexfinal})



if __name__ == "__main__":
    main()