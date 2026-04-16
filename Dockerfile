FROM python:3.13-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код
COPY . .

# По умолчанию запускаем API
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
