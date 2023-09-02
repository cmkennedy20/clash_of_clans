FROM python:3.12.0rc1-alpine3.18
RUN apk add bash
RUN mkdir -p /opt/python_home/
RUN pip install requests

WORKDIR /opt/python_home/