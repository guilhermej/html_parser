#####################################
# Python para Pentesters            #
# https://solyd.com.br/treinamentos #
#####################################

from bs4 import BeautifulSoup
import requests

url = 'http://g1.com.br'

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.103 Safari/537.36'}

req = requests.get(url, headers=header)

html = req.text

soup = BeautifulSoup(html, 'html.parser')

dolar = soup.find(class_="moeda-valor moeda-principal-valor")

dolar_float = float(dolar.get_text()[3:].replace(',', '.'))

print dolar_float * 2
