# mv this file ../

all:
	../env/bin/python manage.py runserver localhost:8009
rm:
	rm -rf django-crud main django env && python3 -mvenv env && source env/bin/activate
install-clean:
	#:r!deactivate && rm -rf main django env && python3 -mvenv env && source env/bin/activate:
	env/bin/pip install django
	env/bin/django-admin startproject config
	mv config django
	#cd django
	env/bin/python django/manage.py startapp main
	env/bin/python django/manage.py migrate
	env/bin/python django/manage.py runserver 0.0.0.0:8000
	
install-crud:	
	env/bin/pip install django
	git clone https://github.com/boutsko/django-crud.git
	mv django-crud django
	env/bin/python django/manage.py migrate
	env/bin/python django/manage.py runserver 0.0.0.0:8001

