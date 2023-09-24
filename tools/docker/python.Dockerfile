FROM python:3.12.0rc1-alpine3.18
ENV FLASK_APP /opt/python_home/main.py
RUN apk add bash
RUN mkdir -p /opt/python_home/
RUN pip install requests flask flask-restful 

WORKDIR /opt/python_home/