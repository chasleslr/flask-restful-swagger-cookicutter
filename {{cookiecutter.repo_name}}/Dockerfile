FROM python:3.8-slim

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install git -y

RUN pip install pipenv \
 && pipenv install --deploy --dev
