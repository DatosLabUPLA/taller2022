#imprime links de autores solamente

from bs4 import BeautifulSoup
from selenium import webdriver
import time, requests, datetime, csv, urllib.parse, os, lxml
from selenium.common import exceptions as SE
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from csv import writer

USER_AGENT = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/61.0.3163.100 Safari/537.36'}
chrome_options = Options()  
chrome_options.add_argument("--headless")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--allow-running-insecure-content')

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), options=chrome_options)  

button_locators = "//button[@class='gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx']"
wait = W(driver, 2)

urls = []
with open(r"instituciones.csv", 'r') as f:
    for line in f:
        urls.append(line)

for url in urls:
    driver.get(url)
    try:
        button_link = wait.until(EC.element_to_be_clickable((By.XPATH, button_locators)))
    except:
        pass
    start_time = time.time()
    start_timing = datetime.datetime.now()
    response = requests.get(url, headers=USER_AGENT)
    response.raise_for_status()

    while button_link:
        try:
            wait.until(EC.visibility_of_element_located((By.ID, 'gsc_sa_ccl')))
            soup = BeautifulSoup(driver.page_source, 'lxml')
            posts = soup.find_all('div', attrs={'class': 'gsc_1usr'})
            time.sleep(2)
        
            for post in posts:
                linkfoto = post.find('a', attrs={'class': 'gs_ai_pho'})
                l = linkfoto.get('href')
                link = urllib.parse.urljoin("https://scholar.google.com", l)
                print(link)
                
                with open(r'Autor.csv', 'a', encoding="utf-8", newline='') as s:
                    writer = csv.writer(s)
                    writer.writerow([link])

            button_link = wait.until(EC.element_to_be_clickable((By.XPATH, button_locators)))
            button_link.click()
            
        except SE.TimeoutException:
            print(f'Página parseada {url}')
            break
    end_time = time.time()
    print("This page took: " + str(end_time - start_time) + " seconds!")

    with open('resultadoslinkautores.txt', 'a', encoding="utf-8", newline='') as fd:
        writer = csv.writer(fd)
        writer.writerow([f'Página {url}  tomó: ' + str(end_time - start_time) + "segundos"])


print("*** {} urls scraped ***".format(len(urls)))
driver.quit()