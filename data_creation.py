import pandas as pd
import numpy as np
import os

# Создание наборов данных
# Пример создания данных о изменении дневной температуры
np.random.seed(42)
days = np.arange(1, 31)
temperature = np.random.randint(20, 35, 30)

data = pd.DataFrame({'Day': days, 'Temperature': temperature})

# Добавление шумов и аномалий в данные
# Дополните этот код для создания различных наборов данных с шумами и аномалиями

# Разделение данных на train и test
train_data = data.iloc[:20]
test_data = data.iloc[20:]

# Сохранение данных в папки "train" и "test"
os.makedirs('train', exist_ok=True)
os.makedirs('test', exist_ok=True)

train_data.to_csv('train/train_data.csv', index=False)
test_data.to_csv('test/test_data.csv')
