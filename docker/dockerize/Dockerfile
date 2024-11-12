# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Скачиваем файл requirements.txt напрямую
RUN apt-get update && apt-get install -y curl && \
    curl -o requirements.txt https://raw.githubusercontent.com/kashkenovbagdat/TechOrda/docker/python/api/fastapi-final/requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Указываем команду запуска FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
