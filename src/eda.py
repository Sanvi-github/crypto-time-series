import matplotlib.pyplot as plt
from preprocessing import preprocess

# Load data
df = preprocess()

# 📈 1. Price Trend
plt.figure()
plt.plot(df.index, df['price'])
plt.title("Bitcoin Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("dashboard/price_trend.png")
plt.show()

# 📊 2. Moving Average
df['MA_7'] = df['price'].rolling(window=7).mean()

plt.figure()
plt.plot(df.index, df['price'], label="Price")
plt.plot(df.index, df['MA_7'], label="7-day MA")
plt.legend()
plt.title("Price with Moving Average")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("dashboard/moving_average.png")
plt.show()

# 📉 3. Histogram
plt.figure()
plt.hist(df['price'], bins=20)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("dashboard/histogram.png")
plt.show()