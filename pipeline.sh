#!/bin/bash

# Предварительная обработка данных
python model_preprocessing.py

# Обучение модели
python model_preparation.py

# Оценка модели
python model_evaluation.py

# Проверка модели на тестовых данных
python model_testing.py
