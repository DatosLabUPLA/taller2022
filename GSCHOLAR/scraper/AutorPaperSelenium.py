import re, sqlite3, requests, time, urllib.parse, os, lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
conn = sqlite3.connect('scholar.db')
cur = conn.cursor()

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}
proxies = {
  'http': os.getenv('HTTP_PROXY')
}
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

results = []
urls = []
with open(r'Autor.csv', 'r') as f:
    for line in f:
        urls.append(line)
        time.sleep(2)
    #url formato = 'https://scholar.google.com/citations?hl=en&user=gQb_tFMAAAAJ'

for url in urls:
    try:
        driver.get(url)
        response = requests.get(url)
        response.raise_for_status()
        #api_url = 'https://scholar.google.com/citations?hl=en&user={user}&cstart={start}&pagesize={pagesize}'
        #user_id = re.search(r'user=(.*)', url).group(1)
        start = 0
        time.sleep(1)
    except:
        pass
    while True:
        #soup = BeautifulSoup(requests.post(api_url.format(user=user_id, start=start, pagesize=1000)).content, 
        #"html.parser")
        soup = BeautifulSoup(driver.page_source, 'lxml')
        name = soup.find('div', attrs={'id': 'gsc_prf_in'}).text or ''
        name_attributes = soup.find_all('div', attrs={'class': 'gsc_prf_il'})
        affiliation = name_attributes[0].text or ''
        interests = name_attributes[2].text or ''
        article = soup.find('tr', {'class': 'gsc_a_tr'})
        research_article = soup.find_all('tr',{'class':'gsc_a_tr'})
        try:   
            elem = soup.find('a', href=re.compile('view_op=view_org&hl=en&oe=ASCII&org='))
            idu= (elem['href'])    
            id_u = idu.split('=')[-1] or ''
        except:
            id_u = ''
            pass
        try:
            email = name_attributes[1].text
            try:    
                verified, mail = email.split('Verified email at ')
                dom, cl = mail.split('.')
            except:
                d, c= email.split('Verified email at ')
                unod, dom, tresd =c.split('.')
        except:
            dom = ''
            pass
                     
        for i, article_info in enumerate(research_article, 1):
            try:
                pub_details = article_info.find('td', attrs={'class': 'gsc_a_t'})
                pub_ref = pub_details.a['href']
                pub_meta = pub_details.find_all('div')
                title_link = article_info.select_one('.gsc_a_at')['data-href']

                title = pub_details.a.text or ''
                authors = pub_meta[0].text or ''
                journal = pub_meta[1].text or ''
                cited_by = article_info.find('a', attrs={'class': 'gsc_a_ac'}).text or ''
                year = article_info.find('span', attrs={'class': 'gsc_a_h'}).text or ''
                linkpaper = urllib.parse.urljoin("https://scholar.google.com", title_link)
                #idp = linkpaper.split(':')[-1] or ''  # id paper
                idp_a = linkpaper.split('=')[-1] or ''  # id paper-autor
                # id_a = url.split('=')[-1]  
                id_a = idp_a.split(':')[-2] or '' # id autor
                linkperfil = urllib.parse.urljoin("https://scholar.google.com","/citations?hl=en&user="+ id_a)
                tablaautor = ([id_a, name, affiliation, dom, interests, linkperfil, id_u])
                tablaautorpaper = ([id_a, title, authors, journal, cited_by, year, linkpaper])
                results.append(tablaautor)
                #print(title)
                cur.execute("""INSERT OR IGNORE INTO Autor (Id_AutorGS, Nombre_Autor, Cargo, Dominio, 
                    Intereses, Link, Id_InstitucionGS) VALUES (?, ?, ?, ?, ?, ?,?)""", tablaautor)
                cur.execute("""INSERT OR IGNORE INTO Instituciones (Id_InstitucionGS) VALUES (?)""", [id_u])
                print(f'Data inserted: {id_a}')
                #id = cur.lastrowid
                cur.execute("""INSERT OR IGNORE INTO Autor_Paper (Id_AutorGS, Titulo_Paper, Autores_Paper, Revista, 
                    Citado_Por, Año, Link_Paper) VALUES ( ?, ?, ?, ?, ?, ?, ?)""",[id_a, title, authors, 
                    journal, cited_by, year, linkpaper])
                conn.commit()
            except:
                pass
        if len(research_article) != 100:
            break  
        start += 100        
    try:  
        for coautho in soup.find('ul', class_='gsc_rsb_a'):
            nameco = coautho.find('a', attrs={'tabindex': '-1'})
            coautor = nameco.text or ''
            l = nameco.get('href')
            c = l.split('=')[1]
            idco = c.split('&')[-2] or ''
            inst = coautho.find('span', attrs={'class': 'gsc_rsb_a_ext'}).text or ''
            try:
                dominioc = coautho.find(class_='gsc_rsb_a_ext gsc_rsb_a_ext2').get_text()
                verc, maic = dominioc.split('Verified email at ')
                doc, cc = maic.split('.')
            except:
                pass
            tablacoautor=([idco, coautor, inst, doc, id_a])
            cur.execute("""INSERT INTO Coautores (Id_Coautor, Nombre_Coautor, Cargo, Dominio,
                    Id_AutorGS) VALUES (?, ?, ?, ?, ?)""", tablacoautor)
            conn.commit()
    except:
        pass
    try:
           
        for cited_by_public_access in soup.select('.gsc_rsb'):
                year_since_text = cited_by_public_access.find_all('tr')[0]
                citations = cited_by_public_access.find_all('tr')[1]
                h_index = cited_by_public_access.find_all('tr')[2]
                i10_index = cited_by_public_access.find_all('tr')[3]
                
                h_index_all = h_index.find_all('td')[1].text or 0
                h_index_since = h_index.find_all('td')[2].text or 0
                citation_all = citations.find_all('td')[1].text or 0
                citation_since = citations.find_all('td')[2].text or 0
                i10_index_all = i10_index.find_all('td')[1].text or 0
                i10_index_since = i10_index.find_all('td')[2].text or 0
                tablaautorcitas = ([h_index_all, h_index_since, citation_all, citation_since, i10_index_since, 
                i10_index_all])
                #print(tablaautorcitas)

                for row in cur.execute('SELECT * FROM Autor'):
                    cur.execute('''UPDATE OR IGNORE Autor SET Hindex_Todo=?, Hindex_Desde=?, Citas_Todo=?, 
                    Citas_Desde=?, i10_Index_Todo=?, i10_Index_Desde=? WHERE Id_AutorGS= ?''', 
                    (h_index_all, h_index_since, citation_all, citation_since, i10_index_since, 
                    i10_index_all, id_a))
                    conn.commit()
    except:
        pass
    try:
        yearshist = soup.findAll('span', class_='gsc_g_t')
        citashist = soup.findAll('span', class_='gsc_g_al')
        for yearh, citah in zip(yearshist, citashist):
            yh = yearh.text or ''
            ch = citah.text or ''
                   # print(yh)
            cur.execute("""INSERT OR IGNORE INTO Citas (Id_AutorGS, Año_Historico, Citas_Historicas)
                    VALUES ( ?, ?, ?)""",[id_a, yh, ch])
            conn.commit()   
    except:
        pass