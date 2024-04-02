import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib

# Загрузка данных для оценки модели
test_data = pd.read_csv('test/test_data.csv')

# Пример предобработки данных для тестового набора
# Дополните этот код для предобработки тестовых данных

# Загрузка сохраненной модели
model = joblib.load('model.pkl')

X_test = scaled_test_data
y_test = test_data['Day']

# Оценка модели на тестовых данных
test_predictions = model.predict(X_test)
test_mse = mean_squared_error(y_test, test_predictions)
print(f'Test Mean Squared Error: {test_mse}')
