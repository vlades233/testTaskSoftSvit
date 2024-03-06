1. Написати конфігурацію nginx згідно умов:
   - слухає порти 80,443 (http,https);
   - redirect http -> https;
   для статичного сайту (html,js):
   -  host testexample.com -> дивиться на /var/www/site
           testexample.com/admin -> дивиться на /var/www/site/admin. доступ лише з одного ip 172.30.1.2.
           testexample.com/cdn -> проксі на cdn зі статикою https://testcdn.s3.eu-central-1.amazonaws.com (публічний доступ)

2. Написати приклад Dockerfile,docker-compose для збірки та запуску локально базового проекта на vue.js (vue.js+nginx)

3. Написати приклад скрипту моніторінгу "load average" на linux-сервері (1cpu,1core)
- скрипт має перевіряти параметр “load average”
- відправляти в telegram повідомлення у разі load average > 1

4. Потрібно оновити версію Postgresql з 14 на 15, single node, база 50Гб з мінімальним даунтаймом. Під час оновлення можна збільшувати кількість, заміняти ноди. Який шлях оновлення оберете для aws rds postgresql та який для self-hosted postgresql?