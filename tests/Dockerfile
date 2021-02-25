FROM python:3.9.2-alpine

WORKDIR /usr/src/tests

# Meant to be run from parent context
COPY /requirements/requirements.txt .

RUN pip install -r requirements.txt

COPY tests/ .