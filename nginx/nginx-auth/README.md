# nginx-auth

### Задание

1. Настройте `server` блок, который слушает 8080 порт.
2. Установите `server_name` значению `example.com`.
3. Добавьте `location` блок для пути `/`, который обслуживает файл [index.html](https://stepik.org/media/attachments/lesson/686238/index.html)
4. Добавьте `location` блок для пути `/images`, который обслуживает файлы из архива [cats.zip](https://stepik.org/media/attachments/lesson/686238/cats.zip). Установите авторизованный вход для учетки: `design:SteveJobs1955`, т.е. логин `design`, пароль `SteveJobs1955`.
5. Добавьте `location` блок для пути `/gifs`, который обслуживает файлы из архива [gifs.zip](https://stepik.org/media/attachments/lesson/686238/gifs.zip). Установите авторизованный вход для учетки: `marketing:marketingP@ssword`.
6. Учетка `design` не должна иметь доступ на другие пути, тоже самое касается других учеток.

---
ответ:

установка паролей 
для design: echo "design:$(openssl passwd -1 SteveJobs1955
design:$1$QbbtVIBI$gTFsmkPp8jrSvzLSc.6MU0
для marketing: echo "marketing:$(openssl passwd -1 marketingP
marketing:$1$NDcfdIU2$QQgdKdl4uFO/9VKWhD9gu1
конфиг файл 
server {
    listen 8080;
    server_name example.com;

    # Обслуживание файла index.html для корневого пути /
    location / {
        root /usr/share/nginx/html;  # Путь к директории, где находится index.html
        index index.html;
    }

    # Настройка авторизованного доступа для пути /images
    location /images {
        auth_basic "Приватные изображения";  # Заголовок окна авторизации
        auth_basic_user_file /etc/nginx/conf.d/images_passwd;  # Путь к файлу паролей
        index index.html;
        alias /usr/share/nginx/html/images;  # Путь к директории для изображений
    }

    # Настройка авторизованного доступа для пути /gifs
    location /gifs {
        auth_basic "Приватные гифки";  # Заголовок окна авторизации
        auth_basic_user_file /etc/nginx/conf.d/gifs_passwd;  # Путь к файлу паролей

        alias /usr/share/nginx/html/gifs;  # Путь к директории для GIF
    }

    # Возвращение строки "jusan-nginx-locations" со статусом 201 для пути /secret_word
    location /secret_word {
        return 201 "jusan-nginx-locations";
    }
}
