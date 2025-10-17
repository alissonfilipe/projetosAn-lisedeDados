import yfinance as yf

# ^BVSP é o código do IBOV
bvsp = yf.Ticker("^BVSP")

# Histórico diário do último mês
dados = bvsp.history(period="1mo", interval="1d")

print(dados)
