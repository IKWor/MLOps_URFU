import pandas as pd  # Добавьте этот импорт
import joblib

# Загрузка обученной модели
model = joblib.load('trained_model.pkl')

# Пример использования модели для предсказания на новых данных
new_data = pd.DataFrame([[1, 2, 3]], columns=['feature1', 'feature2', 'feature3'])
prediction = model.predict(new_data)

print(f'Prediction for new data: {prediction}')
