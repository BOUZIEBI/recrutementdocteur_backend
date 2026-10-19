FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

RUN python manage.py collectstatic --noinput

CMD ["sh", "-c", "gunicorn recrutementdocteur.wsgi:application --bind 0.0.0.0:${PORT:-8080}"]