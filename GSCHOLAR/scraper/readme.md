1. Se corre primero el archivo AutorLink_csv.py, este ocupa el archivo de instituciones.csv, que es donde se encuentran todas las instituciones.
2. Luego va a quedar un archivo Autor.csv con todos los links de los perfiles de los autores.
3. Teniendo el archivo de Autor.csv se puede correr el de AutorPaper.py, que es el que guardará todos los datos en la bd.

*AutorPaper.py Y AutorPaperSelenium.py cumplen la misma función y hacen practicamente los mismo... la única diferencia es que el 1°
solo ocupa bs4 y el 2° ocupa tanto bs4 como selenium, pero demora un poco mas y necesita el archivo chromedriver.exe para correr
(este fue el primer scraper que se hizo).
