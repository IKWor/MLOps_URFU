#!/bin/bash

# Запуск скриптов для создания данных
python data_creation.py

# Предобработка данных
python model_preprocessing.py

# Подготовка модели
python model_preparation.py

# Оценка модели
python model_evaluation.py
