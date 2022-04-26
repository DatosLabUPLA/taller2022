import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    start_time = time.time()

    url = 'https://investigadores.anid.cl/es/login'
    researcher_url = "https://investigadores.anid.cl/es/public_search/researcher?id="
    df = pd.DataFrame(columns=['Name', 'Position', 'University', 'Place', 'Code', 'Investigation_Line', 'Education',
                               'Academic_Experience', 'Professional_Experience'])

    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
    driver.get(url)

    driver.find_element(by=By.NAME, value='q[institution]').send_keys('Universidad de Playa Ancha de Ciencias de la Educación')
    time.sleep(2)
    driver.find_element(by=By.CLASS_NAME, value='btn-info').click()
    time.sleep(2)

    find_all = driver.find_elements(by=By.CLASS_NAME, value='researcher-link')

    for element in find_all:
        # element.click()

        researcher_id = element.get_attribute('href')
        url_code = researcher_url + str(researcher_id[62:])
        anid = requests.get(url_code)

        if anid.status_code == 200:
            anid_soup = BeautifulSoup(anid.text, 'lxml')
            tab_panel = anid_soup.find('div', attrs={'class': 'tab-pane fade active in'})
            a = anid_soup.find('div', attrs={'class': 'col-sm-6'}).get_text()
            a = a.split("\n")
            b = []

            for i in range(len(a)):
                if len(a[i]) > 0:
                    b.append(a[i])

            # Linea de Investigacion
            line = tab_panel.find('p').get_text()

            d = []
            # Descripcion Profecional
            for elem in tab_panel.find_all('ul', attrs={'class': 'list-unstyled'}):
                d.append(elem.get_text().strip().removesuffix('\n').replace('\n', '').replace('\xa0', ' - '))

            # Informacion Principal
            if len(b) == 3:
                df = df.append(
                    {'Name': b[0], 'Position': b[1], 'University': b[2], 'Place': '', 'Code': researcher_id[62:],
                     'Investigation_Line': line, 'Education': d[0], 'Academic_Experience': d[1],
                     'Professional_Experience': d[2]}, ignore_index=True)

            elif len(b) == 4:
                df = df.append(
                    {'Name': b[0], 'Position': b[1], 'University': b[2], 'Place': b[3], 'Code': researcher_id[62:],
                     'Investigation_Line': line, 'Education': d[0], 'Academic_Experience': d[1],
                     'Professional_Experience': d[2]}, ignore_index=True)

            df.to_csv('DATA/investigadores.anid.cl.csv', index=False, encoding='utf-8')

    driver.close()
    print(f'Execution time: {time.time() - start_time}')


if __name__ == "__main__":
    main()
