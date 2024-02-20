FROM python:latest

EXPOSE 5000

WORKDIR /server

COPY * /server/

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "./server.py"]