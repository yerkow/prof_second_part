MariaDB
internal: mariadb:3306
external: localhost:3308

Nginx
internal: nginx_prof:80
external: localhost:82

Backend (Django)
internal: backend_prof:8000/api
external: localhost:82/api
