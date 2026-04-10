import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {"vs_currency": "usd", "days": "365"}

response = requests.get(url, params=params)
data = response.json()

prices = data['prices']

df = pd.DataFrame(prices, columns=['timestamp', 'price'])
df['date'] = pd.to_datetime(df['timestamp'], unit='ms')

df.to_csv('data/btc_data.csv', index=False)

print("✅ Data saved successfully")