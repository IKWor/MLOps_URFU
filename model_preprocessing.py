from sklearn.preprocessing import StandardScaler
import pandas as pd

# Загрузка данных
train_data = pd.read_csv('train/train_data.csv')

# Выполнение предварительной обработки, например, с использованием StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(train_data)
