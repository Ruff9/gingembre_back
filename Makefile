dev:
	pipenv shell \
	python manage.py runserver

deploy:
	git push scalingo main