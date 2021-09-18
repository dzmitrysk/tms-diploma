# tms-diploma

Установить в систему PostgreSQL
```
$ sudo apt-get update
$ sudo apt-het install postgresql postgresql-contrib
```
Под пользователем `postgres` создать базу данных `tmsdiploma`
```
$ sudo -u postgres psql
create database tmsdiploma;
\q
```

