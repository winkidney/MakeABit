syncdb:
	python manage.py makemigrations
	python manage.py migrate

install:
	pip install -r requirements.txt

develop:
	python manage.py runserver 0.0.0.0:8000

mk-config:
	python tools.py gen_production_setting