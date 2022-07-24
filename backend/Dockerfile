# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN mkdir /LearnApp
WORKDIR /LearnApp
COPY ./LearnApp /LearnApp

COPY ./requirements.txt /requirements.txt
RUN pip install pytils
RUN pip install -r /requirements.txt


