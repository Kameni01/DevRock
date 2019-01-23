#DevRock

- python 3.6
- Django 2.1
- postgres 11.3


#Установка

-pip install -r requirements.txt
-создаем базу данных DevRock (хост, логин и пароль прописаны в файле setting.py
  в параметре DATABASE. Можно заменить на свои или использовать
  предустановленные)
-открываем в консоли корневую директорию сайта
-python manage.py migrate
-python manage.py makemigrations
-python manage.py createsuperuser(Создание админа джанги(Админки))
-Вводим логин суперпользователя
-Вводим его почту
-Вводим пароль и подтверждаем
-python manage.py runserver
