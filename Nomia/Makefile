run:
	python manage.py runserver

pep8:
	flake8 --statistics --count

superuser:
	./manage.py create_repair_superuser superuser super@luser.io

migrate:
	python3 manage.py makemigrations $(APP) && python3 manage.py migrate