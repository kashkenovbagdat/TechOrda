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
