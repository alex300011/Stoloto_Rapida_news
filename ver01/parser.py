import requests
from bs4 import BeautifulSoup

class Parser:

    def get_data(self):
        self.url = 'https://www.stoloto.ru/rapido2/archive'
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'lxml')
        self.quotes1 = self.soup.find_all('div', class_='elem')
        #quotes = soup.find_all('span', class_='zone')

        #print('-->',quotes1)
        #print(type(quotes1))

        paragraphs = []

        for x in self.quotes1:
            paragraphs.append([str(x)])
        return paragraphs


