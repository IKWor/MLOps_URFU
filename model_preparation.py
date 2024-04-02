from sklearn.linear_model import LinearRegression
import pandas as pd

# Загрузка предварительно обработанных данных
preprocessed_data = pd.read_csv('preprocessed_data.csv')

# Разделение данных на признаки и целевую переменную
X = preprocessed_data.drop('target', axis=1)
y = preprocessed_data['target']

# Обучение модели линейной регрессии
model = LinearRegression()
model.fit(X, y)

# Сохранение обученной модели для дальнейшего использования
import joblib

joblib.dump(model, 'trained_model.pkl')
