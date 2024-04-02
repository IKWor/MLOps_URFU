#!/bin/bash

# Предварительная обработка данных
python preprocess_data.py

# Обучение модели
python model_preparation.py

# Оценка модели
python model_evaluation.py

# Проверка модели на тестовых данных
python model_testing.py
