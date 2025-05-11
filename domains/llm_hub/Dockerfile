ARG BASE_IMAGE=python:3.11-slim-bullseye

FROM ${BASE_IMAGE}

WORKDIR /module

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR /module/src
COPY ./src /module/src
