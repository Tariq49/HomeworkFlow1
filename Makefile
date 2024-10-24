dev-start:
	python3 manage.py runserver --settings=config.settings.dev
dev-startapp:
	cd apps && python3 ../manage.py startapp $(app) --settings=config.settings.dev
dev-m:
	python3 manage.py migrate --settings=config.settings.dev
dev-makem:
	python3 manage.py makemigrations --settings=config.settings.dev
dev-showm:
	python3 manage.py showmigrations --settings=config.settings.dev
dev-shell:
	python3 manage.py shell --settings=config.settings.dev
dev-shell-plus:
	python3 manage.py shell_plus --settings=config.settings.dev
dev-install:
	pip install -r requirements/dev.txt
dev-test:
	python3 manage.py test --settings=config.settings.dev
dev-super:
	python3 manage.py createsuperuser --settings=config.settings.dev