#!/bin/bash
# запускаем контейнер
docker run -d \
  --name jusan-docker-exec \
  -p 8181:80 \
  nginx:mainline
  # создание конфига внути контейнера
docker exec -it jusan-docker-exec bash -c "cat << EOF > /etc/nginx/conf.d/jusan-docker-exec.conf
server {
    listen 80;
    server_name jusan.singularity;

    location / {
        return 200 'Hello, from jusan-docker-exec';
    }
    location /home {
        return 201 'This is my home!';
    }
    location /about {
        return 202 'I am just an exercise!';
    }
}
EOF"

  #
docker exec -it jusan-docker-exec nginx -s reload
# вывод смс об успешном запуске
echo "Контейнер настроен и перезагружен успешно."