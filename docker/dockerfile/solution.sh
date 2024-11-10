#!/bin/bash

#
cd "$(dirname "$0")"
# скачать конф
curl -o jusan-dockerfile.conf https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.conf

# скачать и разархивировать
curl -o jusan-dockerfile.zip https://stepik.org/media/attachments/lesson/686238/jusan-dockerfile.zip
unzip -o jusan-dockerfile.zip

#сборка образа
docker build -t nginx:jusan-dockerfile .

#проверка наличие образа
docker images | grep nginx

#запуск контейнера
docker run -d \
  -p 6060:80 \
  --name jusan-dockerfile \
  nginx:jusan-dockerfile