FROM python:3.9.2-alpine

WORKDIR /usr/src/tests

ARG PIP_FILE_NAME=requirements-tests.txt

# Meant to be run from parent context
COPY /requirements/${PIP_FILE_NAME} .

RUN pip install -r ${PIP_FILE_NAME}