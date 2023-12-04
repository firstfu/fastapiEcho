FROM python:latest

# 設定 python 環境變數
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install iputils-ping -y
RUN apt-get install vim -y

RUN mkdir -p /app
WORKDIR /app

COPY ./ /app/


RUN pip3 install -r requirements.txt
