# Используем базовый образ Python
FROM python:3.8

# Устанавливаем необходимые зависимости
RUN pip install flask numpy pandas scikit-learn

# Копируем python код в образ
COPY ./lab3 /app
WORKDIR /app

# Обработка данных и подготовка датасетов
COPY data.csv /app/data.csv
RUN python model_preprocessing.py

# Устанавливаем переменные окружения
ENV FLASK_APP=app.py

# Открываем порт для взаимодействия с API
EXPOSE 5000

# Запускаем микросервис
CMD ["flask", "run", "--host=0.0.0.0"]
