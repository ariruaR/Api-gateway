FROM python:3.11-slim


# системные переменные
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
# сначала зависимости (это ускоряет docker cache)
COPY req.txt .



RUN pip install --no-cache-dir -r req.txt

# потом код приложения
COPY . .

# запуск сервера
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

