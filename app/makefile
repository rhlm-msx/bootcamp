DEPEND="../depend"
DEPEND_DEV="../depend_dev"

run:		
	export $(shell cat .env);PYTHONPATH="$(DEPEND)" python -m fastapi dev entry.py	

test:
	export $(shell cat .env);PYTHONPATH="$(DEPEND_DEV):." python -m pytest -v
install:
	pip install -r requirements.txt -t depend --upgrade

