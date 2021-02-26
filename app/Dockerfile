FROM python:3.9.2-alpine

WORKDIR /usr/src/app

ARG PIP_FILE_NAME=requirements.txt

# Meant to be run from parent context
COPY /requirements/${PIP_FILE_NAME} .

RUN pip install -r ${PIP_FILE_NAME}