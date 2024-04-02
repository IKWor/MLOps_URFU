import pandas as pd
from sklearn.externals import joblib

# Загрузка тестовых данных
test_data = pd.read_csv('test/test_data.csv')

# Загрузка обученной модели
model = joblib.load('trained_model.pkl')

# Предсказание на тестовых данных
predictions = model.predict(test_data)

# Оценка качества модели
# Добавьте необходимый код для оценки модели на тестовых данных

# Вывод результатов
print(predictions)
