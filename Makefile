.PHONY: install run docker-build docker-run clean

install:
	pip install -r requirements.txt

run:
	streamlit run app.py

docker-build:
	docker compose build

docker-run:
	docker compose up -d

docker-stop:
	docker compose down

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
