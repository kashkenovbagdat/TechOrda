# # Используем официальный образ Python
# FROM python:3.9-slim

# # Устанавливаем рабочую директорию
# WORKDIR /app

# # Скачиваем файл requirements.txt напрямую
# RUN apt-get update && apt-get install -y curl && \
#     curl -o requirements.txt https://raw.githubusercontent.com/kashkenovbagdat/TechOrda/docker/python/api/fastapi-final/requirements.txt && \
#     cat requirements.txt  # Проверяем содержимое requirements.txt для отладки

# # Скачиваем task_api.py
# RUN curl -o task_api.py https://raw.githubusercontent.com/kashkenovbagdat/TechOrda/docker/python/api/fastapi-final/task_api.py && \
#     cat task_api.py  # Проверяем содержимое task_api.py для отладки


# # Устанавливаем зависимости
# RUN pip install --no-cache-dir -r requirements.txt

# # Копируем остальные файлы проекта
# COPY . .

# # Указываем команду запуска FastAPI
# CMD ["uvicorn", "task_api:app", "--host", "0.0.0.0", "--port", "8080"]

# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем curl (для скачивания файлов) и обновляем систему
RUN apt-get update && apt-get install -y curl

# Скачиваем файл requirements.txt напрямую
RUN curl -o requirements.txt https://raw.githubusercontent.com/kashkenovbagdat/TechOrda/docker/python/api/fastapi-final/requirements.txt

# Скачиваем task_api.py
RUN curl -o task_api.py https://raw.githubusercontent.com/kashkenovbagdat/TechOrda/docker/python/api/fastapi-final/task_api.py

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду запуска FastAPI
CMD ["uvicorn", "task_api:app", "--host", "0.0.0.0", "--port", "8080"]
