FROM python:3.12.2-slim

RUN apt-get update

WORKDIR /app
RUN mkdir app imagetools static

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY app app
COPY imagetools imagetools
COPY manage.py .
COPY gunicorn.py .

RUN python manage.py migrate \
    && python manage.py collectstatic
