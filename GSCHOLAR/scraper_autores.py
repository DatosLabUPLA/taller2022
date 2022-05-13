from multiprocessing.connection import wait
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions as SE
import time,datetime,csv
from bs4 import BeautifulSoup

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

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver= webdriver.Chrome(executable_path='chromedriver.exe',options=options)

button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
wait = WebDriverWait(driver,2)

data= []
for id in instituciones.values():
    url="https://scholar.google.cl/citations?view_op=view_org&org=" + id 
    data.append(url)

for url in data:
    driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
    except: 
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID,'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source,'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)

            for autores in posts:
                foto = autores.find('a',class_='gs_ai_pho')
                link = foto.get('href')
                print(link)

            with open(r'test.csv','a',encoding="utf-8", newline='') as s:
                    writer = csv.writer(s)
                    writer.writerow([link])

            button_link = wait.until(EC.element_to_be_clickable((By.XPATH,button_locators)))
            button_link.click()

        except SE.TimeoutException:
            print('Funciono')
            break
driver.quit()




