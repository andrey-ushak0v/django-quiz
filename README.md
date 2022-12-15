## django-quiz
### приложение с викторинами

## инструкция по запуску:

1) склонируйте репозиторий на локальный компьютер

```git clone https://github.com/andrey-ushak0v/django-quiz.git```

2) создайте и активируйте виртуальное окружение

```python3 -n venv venv```

```source venv/bin/activate```

3) установите зависимости

```pip install -r requirements.txt```

4) создайте и примените миграции

```python manage.py makemigrations```

```python manage.py migrate```

5) через админку наполните базу данных данными

6) главная страница проекта доступна по адресу 

```http://127.0.0.1:8000/```
