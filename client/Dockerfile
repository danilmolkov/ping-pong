FROM python:latest

LABEL version="1.0"
LABEL maintaner="Daniel Molkov"
LABEL promoted="true"

EXPOSE 5000

WORKDIR /client

COPY * /client

RUN pip install -r requirements.txt
