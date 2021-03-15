import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver


#driver = webdriver.Firefox(executable_path="C:\geckodriver.exe") #executable_path="C:\Program Files\Mozilla Firefox\firefox.exe"

#driver.get('https://www.stoloto.ru/rapido2/archive')

#button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[3]/span[1]")

#button.click()
def parser():
    url = 'https://www.stoloto.ru/rapido2/archive'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes1 = soup.find_all('div', class_='elem')
    quotes = soup.find_all('span', class_='zone')

    #print('-->',quotes1)
    #print(type(quotes1))

    paragraphs = []

    for x in quotes1:
        paragraphs.append([str(x)])

#print(paragraphs)
    #count =0
    #for i in paragraphs:
        #print(count,i)
        #count += 1
