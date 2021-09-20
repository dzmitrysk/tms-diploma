# TeachMeSkills
## Online course: "Python developer"
### Graduate work
### Author: Kolyago Dmitry

<br><br>
To run application in Docker container (while building Docker image
the Django-superuser(*) and random initial data for Employees and Equipments will be created):

```
docker build -t dip .
docker run -d -p 9200:9200 dip
```

To run application locally:
```
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
```
To create Django-superuser and random initial data for Employees and Equipments:
```
python manage.py shell
>>> exec(open('create_admin.py').read())
>>> exec(open('create_sample_data.py').read())
>>> exit()
```

Run application:
```
python manage.py runserver
```
(*) Automatically created Django-superuser has `username/password == admin/123123abc`

--------------------------------------------------------------------------------
### <u>Цели работы</u>
<b>1. Демонстрация базовых навыков программирования на Python:</b>
* циклы
* условные операторы
* использование списков (одномерными, двухмерными)
* использование кортежей
* форматирование строк
* вывод в консоль
* обработка исключений
* функции
* классы (наследование)
* использование библиотек

<b>2. Применение HTML/СSS</b>
* HTML разметка на основе классов
* каскадные таблицы стилей CSS
* псевдоклассы (`:hover`)

<b>3. Использование фрэймворка Django:</b>
* модель `MVT (MVC)` для веб-приложения
* настройка проекта: `settings.py`
* использование Django ORM для создания баз данных
* создание моделей представления данных: `models.py`
* настройка `Django Administration`, `superuser`
* создание и выполнения миграций: `makemigrations, migrate`
* разработка `views` и `templates`, привязка к `URL`, `views.py`, `urls.py`
* HHTP-запросы `GET, POST, PUT, DELETE, PATCH`; `requests` и `responses`

<b>4. Использование Django REST framework:</b>
* Web APIs
* сериализаторы моделей, `JSON`
* APIViews

<b>5. Использование pytest </b>
* Unit-тестирование

<b>6. Использование Docker </b>
* контейнеризация (`Dockerfile`)
* создание образа (`docker build`)
* запуск приложения в контейнере (`docker run`)

<b>7. Использование AWS (Amazon Web Services):</b>
* запуск виртуальной машины EC2 (Elastic compute cloud)
* подготовка к запуску приложения (настройка Security Groups, обновление ОС, клонирование репозитория проекта, установка Docker)
* запуск приложения в Docker-контейнере