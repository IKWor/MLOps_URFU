import pandas as pd
from sklearn.linear_model import LinearRegression

# Загрузка обработанных данных
from sklearn.metrics import mean_squared_error

# Подготовка модели
X_train = scaled_data
y_train = train_data['Day']

model = LinearRegression()
model.fit(X_train, y_train)

# Оценка модели на тренировочных данных
train_predictions = model.predict(X_train)
train_mse = mean_squared_error(y_train, train_predictions)
print(f'Training Mean Squared Error: {train_mse}')
