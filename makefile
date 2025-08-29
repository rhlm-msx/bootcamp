run:
	PYTHONPATH="depend" python -m fastapi dev main.py
install:
	pip install -r requirements.txt -t depend --upgrade

