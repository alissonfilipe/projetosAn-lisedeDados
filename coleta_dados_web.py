import requests
from bs4 import BeautifulSoup

url = 'https://python.org.br/web'
requisicao = requests.get(url)

extracao = BeautifulSoup(requisicao.text, features='html.parser')
"""
print(extracao.text.strip())
"""

# exemplo dele
"""
for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.text.strip()    
    print('Titulo:', titulo)
"""

# filtrar tags h2 e p
# contar quantos h2 e p existem
count = 0
for linha_texto in extracao.find_all("h2"):
    # primeira fase
    subtitulos = linha_texto.text.strip()
    print(subtitulos)
    for paragrafo in extracao.find_all("p"):
        p = paragrafo.text.strip()
        print(p)
        count = count+1
print(f"quantidade de p e h2 {count}")
