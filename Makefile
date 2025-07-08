deps:
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt

dev:
	fastapi dev ./api/main.py
