# Динамическая анкета с авторизацией

Веб-приложение предназначено для проведения опросов с динамическим отображением вопросов, зависящих от ответов пользователя.
Данное приложение сформировано под конкретный опросник от компании Nomia.
В случае настройки опроса под себя необходимо поменять в переменной question атрибут title в views.py.

## На что стоит обратить внимание:

1. В проекте присутствует MakeFile. Если вы разворачивате приложение на Linux,
то он Вам упростит работу. Для Windows и MacOS необходимо скачать "make"
2. Из gitgnore удален db.sqlite3, чтобы проще было протестировать приложение с готовой БД
3. Создано приложение auth_user для авторизации. Суперюзер уже создан в БД
Логин: sergei Пароль:Qawsed123
4. Картинки с ответами будут сохранятся в answers_pictures/{filename} благодаря функции answer_image_directory_path
5. Админка настроена и переведена на русский язык

## Как запустить проект 

Для запуска проекта необходимо:

1. Клонировать репозиторий:
```
git clone https://github.com/skolbasin/test_nomia.git
```
2. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
3. Выполнить миграции для создания структуры базы данных:
```
python manage.py migrate
```

4. Запустить сервер разработки:
```
python manage.py runserver
```
5. После запуска сервера перейдите по адресу http://localhost:8000/
