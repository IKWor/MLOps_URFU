import pandas as pd
from sklearn.preprocessing import StandardScaler

# Загрузка данных для предобработки
train_data = pd.read_csv('train/train_data.csv')

# Пример предобработки данных с использованием StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(train_data[['Temperature']])
