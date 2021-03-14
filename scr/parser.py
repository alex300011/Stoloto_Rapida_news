import requests
from bs4 import BeautifulSoup

url = 'https://www.stoloto.ru/rapido2/archive'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes1= soup.find_all('div', class_='draw')
quotes = soup.find_all('span', class_='zone')

print(quotes)
print('-->',quotes1)