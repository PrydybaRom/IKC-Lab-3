FROM nginx:latest
# Копіюємо html-файл у стандартну директорію
COPY index.html /usr/share/nginx/html/
# Відкриваємо порт 80
EXPOSE 80
# Команда за замовчуванням
CMD ["nginx", "-g", "daemon off;"]