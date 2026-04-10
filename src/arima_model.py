from statsmodels.tsa.arima.model import ARIMA
from preprocessing import preprocess
import matplotlib.pyplot as plt

# Load data
df = preprocess()

# Use only price column
data = df['price']

# Train ARIMA model
model = ARIMA(data, order=(5,1,0))
model_fit = model.fit()

print("✅ Model trained successfully")

# Forecast next 7 days
forecast = model_fit.forecast(steps=7)

print("\n📊 Forecasted Prices:")
print(forecast)

# Plot results
plt.figure()
plt.plot(data, label="Actual Price")
plt.plot(forecast, label="Forecast", linestyle='dashed')
plt.legend()
plt.title("ARIMA Forecast")
plt.xticks(rotation=45)
plt.tight_layout()

# Save graph
plt.savefig("dashboard/arima_forecast.png")

plt.show()