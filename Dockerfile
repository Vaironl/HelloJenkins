# This Dockerfile is meant to be run by Jenkins
FROM python:3.9.2

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt