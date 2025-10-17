import requests 
from bs4 import BeautifulSoup
import pandas

response = requests.get('https://finance.yahoo.com/quote/%5EBVSP/history/?guccounter=1')

soup = BeautifulSoup(response.text,features='html.parser')
print(soup.prettify()[:1000])

print('pandas :')

url_dados = pandas.read_html('https://finance.yahoo.com/quote/%5EBVSP/history/?guccounter=1')
print(url_dados[0].head(10))
