syncdb:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py migrate words

install:
	pip install -r requirements.txt
	python manage.py collectstatic

develop:
	python manage.py runserver 0.0.0.0:8000

mk-config:
	python tools.py gen_production_setting

gunicorn:
	gunicorn sentence.wsgi