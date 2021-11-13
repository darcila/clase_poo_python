import requests
from bs4 import BeautifulSoup


class ScrappingCelulares:
    __url = 'https://celulares.mercadolibre.com.co/#menu=categories'

    def procesar(self):
        return self.__extraccion_datos(self.__consulta())

    def __consulta(self):
        page = requests.get(self.__url)
        return page.text

    def __extraccion_datos(self, content):
        soup = BeautifulSoup(content, "html.parser")
        elements = soup.findAll('li', {'class': 'ui-search-layout__item'})

        celulares = []
        for element in elements:
            pass
            # no se que mas hacer aca.
