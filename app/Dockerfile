FROM python:3.9.2-alpine

WORKDIR /usr/src/requirements

COPY ./requirements/requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /usr/src/app