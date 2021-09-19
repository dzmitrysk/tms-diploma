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