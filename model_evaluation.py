import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error

# Загрузка обученной модели
model = joblib.load('trained_model.pkl')

# Загрузка тестовых данных
test_data = pd.read_csv('test/test_data.csv')

# Предсказание с помощью модели
predictions = model.predict(test_data)

# Оценка модели с использованием среднеквадратичной ошибки
mse = mean_squared_error(true_values, predictions)
print(f'Mean Squared Error: {mse}')
