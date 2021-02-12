FROM python:latest

WORKDIR /python_work

RUN pip3 install requests bs4 mysql-connector-python

COPY *.py .