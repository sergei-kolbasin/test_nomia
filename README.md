# Динамическая анкета с авторизацией

Веб-приложение предназначено для проведения опросов с динамическим отображением вопросов, зависящих от ответов пользователя.
Данное приложение сформировано под конкретный опросник от компании Nomia.
В случае настройки опроса под себя необходимо поменять в файле config изменить ответы под себя и внести изменения в БД через админку

Схема сценария анкеты с учётом авторизации - https://miro.com/welcomeonboard/UDRqWFBNdWtJQndMaUhqcVJVOU1PTWpQNjRKWlkyb0lCYTRrNVFhdFgwRVNZY241cXVCZTJSVEdvUlhROFNBMnwzNDU4NzY0NTg0NDU0NTY0OTg4fDI=?share_link_id=604127412494
## На что стоит обратить внимание:

1. В проекте присутствует MakeFile. Если вы разворачивате приложение на Linux,
то он вам упростит работу. Для Windows необходимо скачать "make" дополнительно
2. Из gitgnore удален db.sqlite3, чтобы проще было протестировать приложение с готовой БД
3. Создано приложение auth_user для авторизации. Суперюзер уже создан в БД. 
Логин: sergei Пароль: Qawsed123
5. Админка настроена и переведена на русский язык. Для входа нужно зайти на http://localhost:8000/admin
6. В приложении реализована сессия с формами, поэтому Goоgle будет навязчиво вам предлагать сохранить данные, не слушайтесь
7. Проект покрыт тестами. Для проверки необходимо зайти в директорию с приложением и выполнить команды:
```
python manage.py test questionnaire.tests
python manage.py test auth_user.tests
```
8. Логирование настроено на сохранение логов в корне проекта в файле AllLogs.log в формате '%(asctime)s [%(levelname)s] %(name)s: %(message)s' на все уровни логирования и автоудалением через 7 дней 
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
python manage.py makemigrations
python manage.py migrate
```
либо на Linux:
```
make migrate
```

4. Запустить сервер :
```
python manage.py runserver
```
либо на Linux:
```
make run
```
5. После запуска сервера перейдите по адресу http://localhost:8000/login и введи логин и пароль от суперюзера

## Структура проекта:

- Сам проект находится в папке [Nomia](https://github.com/skolbasin/test_nomia/tree/main/Nomia), которая в свою очередь состоит из 3 директорий: [Nomia](https://github.com/skolbasin/test_nomia/tree/main/Nomia/Nomia)(основные настройки проекта), [auth_user](https://github.com/skolbasin/test_nomia/tree/main/Nomia/auth_user)(авторизация пользователя), [questionnaire](https://github.com/skolbasin/test_nomia/tree/main/Nomia/questionnaire)(древовидная анкета)
- Весь фронтенд реализован в папке questionnaire/templates. По умолчанию любая статика(за исключением иконок ответов на вопросы) будет сохраняться в static/
- url описаны в файле urls.py
- В проекте реализовано 4 модели в файле models.py:
  - Institution(заведение) В процессе заполнения анкеты в данную модель поэтапно сохраняются данные о заведении
  - Question(вопрос)
  - Answer(ответ)
  - Survey(опрос) Состоит из одного вопроса и нескольки ответов

- Для отправки данных из анкеты на сервер, используются DjangoForms в файле forms.py
- Тесты находятся в файле tests.py
- В файле config содержаться все вопросы из анкеты. Они затем импортируются в views.py для работы с БД
