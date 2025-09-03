run:
	export $(shell cat .env);PYTHONPATH="depend" python -m fastapi dev entry.py
install:
	pip install -r requirements.txt -t depend --upgrade

