FROM python:3.11
ENV PYTHONUNBUFFERED=1

WORKDIR /app
EXPOSE 8000

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
