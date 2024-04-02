# data_creation.py

import numpy as np
import pandas as pd
import os

# Создание различных наборов данных, описывающих процесс (например, изменения ежедневной температуры) с аномалиями или шумом

# Создание и сохранение наборов данных в папках train и test
train_data = pd.DataFrame(np.random.randn(100, 3), columns=['feature1', 'feature2', 'feature3'])
test_data = pd.DataFrame(np.random.randn(50, 3), columns=['feature1', 'feature2', 'feature3'])

os.makedirs('train', exist_ok=True)
os.makedirs('test', exist_ok=True)

train_data.to_csv('train/train_data.csv', index=False)
test_data.to_csv('test/test_data.csv', index=False)
