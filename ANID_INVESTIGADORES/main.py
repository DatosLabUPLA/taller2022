import requests
import pandas as pd
from bs4 import BeautifulSoup


def main():
    min = 10000
    max = 42683
    url = "https://investigadores.anid.cl/es/public_search/researcher?id="

    df = pd.DataFrame(columns=['Name', 'Position', 'University', 'Place', 'Code'])

    for code in range(min, max + 1):
        url_code = url + str(code)
        anid = requests.get(url_code)

        if len(anid.text) != 728:

            if anid.status_code == 200:
                anid_soup = BeautifulSoup(anid.text, 'lxml')
                a = anid_soup.find('div', attrs={'class': 'col-sm-6'}).get_text()
                a = a.split("\n")
                b = []

                for i in range(len(a)):
                    if len(a[i]) > 0:
                        # print(a[i])
                        b.append(a[i])

                if len(b) == 3:
                    df = df.append({'Name': b[0], 'University': b[1], 'Place': b[2], 'Code': code}, ignore_index=True)
                elif len(b) == 4:
                    df = df.append({'Name': b[0], 'Position': b[1], 'University': b[2], 'Place': b[3], 'Code': code},
                                   ignore_index=True)

                df.to_csv('DATA/investigadores.anid.csv', index=False, encoding='utf-8')

    print(df)


if __name__ == "__main__":
    main()
