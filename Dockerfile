# FROM mcr.microsoft.com/playwright/python:v1.47.0-noble
#
# WORKDIR /usr/workspace
#
# # Установка дополнительных зависимостей
# RUN apt-get update && apt-get install -y \
#     gcc \
#     && rm -rf /var/lib/apt/lists/*
#
# # Копируем и устанавливаем все зависимости из requirements.txt
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# RUN playwright install --with-deps
#
# COPY . .
#
# # Запуск всех тестов (API + UI)
# CMD ["pytest", "tests/", "-v", "--headed"]


FROM mcr.microsoft.com/playwright/python:v1.47.0-noble

WORKDIR /usr/workspace

# Установка зависимостей
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps chromium firefox webkit

COPY . .

# Переменные окружения по умолчанию
ENV BROWSER=chromium
ENV MARKER=smoke
ENV THREADS=1

# Запуск тестов с параметрами
CMD ["/bin/sh", "-c", "pytest tests/ -v -n $$THREADS -m $$MARKER --alluredir=allure-results"]
