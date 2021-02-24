# This Dockerfile is meant to be run by Jenkins
FROM python:3.9.2

WORKDIR /usr/src/

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /usr/src/

WORKDIR /usr/src/tests/

CMD [ "python", "test.py" ]