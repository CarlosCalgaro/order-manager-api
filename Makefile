.PHONY: dev install test clean

dev:
	fastapi dev order_manager_api/main.py --port 8003

install:
	poetry install

test:
	pytest

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
