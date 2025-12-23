FROM python:3.10

ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install dependencies first (leverages Docker layer cache)
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root --no-ansi

ENV PYTHONPATH=/app

# Copy application code
COPY ./scripts /app/scripts
COPY ./order_manager_api /app/order_manager_api
COPY ./tests /app/tests

CMD ["fastapi", "run", "--workers", "4", "order_manager_api/main.py"]