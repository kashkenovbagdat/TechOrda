#!/bin/bash

# Скачивание конфигурационного файла nginx.conf
curl -o nginx.conf https://raw.githubusercontent.com/kashkenovbagdat/TechOrda/main/docker/docker-bind/nginx.conf

# Запуск контейнера с параметрами
docker run -d \
    --name jusan-docker-bind \
    -p 7777:80 \
    -v "$(pwd)/nginx.conf:/etc/nginx/nginx.conf" \
    nginx:mainline

# Проверка запросом http://localhost:7777
curl http://localhost:7777

# Просмотр списка запущенных контейнеров
docker ps

# Просмотр логов контейнера
docker logs jusan-docker-bind