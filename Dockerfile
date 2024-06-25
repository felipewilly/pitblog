FROM python:3.11-alpine3.17
ENV PYTHONUNBUFFERED=1

COPY ./pitblog /pitblog


WORKDIR /pitblog

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY /pitblog /pitblog