FROM python:3

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /usr/src/app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY ./Pipfile /usr/src/app/Pipfile

COPY . /usr/src/app/
