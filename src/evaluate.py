from sklearn.metrics import mean_squared_error
import numpy as np
from preprocessing import preprocess
from statsmodels.tsa.arima.model import ARIMA

# Load data
df = preprocess()
data = df['price']

# Split data (train/test)
train_size = int(len(data) * 0.8)
train, test = data[:train_size], data[train_size:]

# Train model
model = ARIMA(train, order=(5,1,0))
model_fit = model.fit()

# Predict on test data
predictions = model_fit.forecast(steps=len(test))

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(test, predictions))

print("📊 Model Evaluation")
print("RMSE:", rmse)