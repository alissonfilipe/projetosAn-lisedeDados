import requests

url = 'https://finance.yahoo.com/quote/^BVSP'
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)

print(response.text[:600])  # Exibe os primeiros 600 caracteres do HTML retornado
