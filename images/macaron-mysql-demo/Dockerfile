FROM mysql:8.0.33

COPY init.sql /docker-entrypoint-initdb.d/

COPY timezone.cnf /etc/mysql/conf.d/

EXPOSE 3306
