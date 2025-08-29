run:
	export $(shell cat .env); PYTHONPATH="depend" python main.py
install:
	pip install -r requirements.txt -t depend --upgrade

